from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.auth.decorators import login_required

 
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from .models import Neighbourhood,Post,Business,Profile
from .forms import CommunityModelForm, PostModelForm,CommentForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm,BusinessModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!,You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'django_registraton/registration_form.html',{'form': form})


@login_required(login_url='/login/')
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'c_form': CommunityModelForm()
    }

    return render(request, 'profile.html', context)


# Create your views here.
@login_required(login_url='/login/')
def search_results(request):
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_bsn = Business.search_by_bsn(search_term)
        # user = User.objects.get(username=searched_user)
        # user_images = Profile.objects.get(user=searched_user)
        message = f"{search_term}"
        context = {
            'message': message, 
            'searched_bsns': searched_bsn
        }
        return render(request, 'hood/search.html', context)

    else:
        messages.success(request, f"You haven't searched for any term")

        return render(request, 'hood/search.html',{"message":message})

def singlebsnview(request,post_id):
    post = get_object_or_404(Business,pk=post_id)
    return render(request, 'hood/business_detail.html',locals())



# class PostListView(ListView):
#     context_object_name = 'post_list'
#     template_name= 'neiba/post_list.html' # <app>/<model>_<view_type>.html
    
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         queryset = Post.objects.filter(location__name=**kwargs)
#         return context
@login_required(login_url='/login/')
def post_listview(request):
    all_communities = Neighbourhood.objects.all()

    try:
        location = get_object_or_404(Neighbourhood, pk=request.user.profile.community.id)
        all_profiles = Profile.objects.filter(community=location)
        form = CommentForm()
        posts = Post.objects.filter(location=location)
        bsn_posts = Business.objects.filter(bsn_community=location)
        print(all_communities)
        print('fffffffffffffffffffffffff')

    except:
        messages.success(request, f'Kindly join a location or update it via your profile!')

    return render(request,'hood/post_list.html', locals())

def join(request,new_community):
    # get_usr = get_object_or_404(User,pk=request.user.id)
    try:
        new_communit = get_object_or_404(Neighbourhood, pk=new_community)

        request.user.profile.community = new_communit
        request.user.profile.save()
        print('pppppppppppp')
        return redirect('home')
            
    except:
        return redirect('home')

@login_required(login_url='/login/')
def business_listview(request):
    location = get_object_or_404(Neighbourhood, pk=request.user.profile.community.id)
    all_profiles = Profile.objects.filter(community=location)

    try:
        posts = Post.objects.filter(location=location)
        bsn_posts = Business.objects.filter(bsn_community=location)
        print('fffffffffffffffffffffffff')
        print(bsn_posts)
        print('fffffffffffffffffffffffff')

    except:
        posts = Post.objects.get(location=location)
        bsn_posts = Business.objects.get(bsn_community=location)

    return render(request,'hood/business_list.html', locals())
def change_user_role(request,user_id):
    fuser = get_object_or_404(Profile, pk=user_id)
    if fuser.is_police is False and request.user.username==request.user.profile.community.created_by:
        fuser.is_police = True
    else:
        messages.success(request, f'Try again!')
    return (request,'hood/post_list.html')
# def business_listview(request):
#     location = get_object_or_404(Neighbourhood, pk=request.user.profile.community.id)
#     try:
#         posts = Business.objects.filter(location=location)
#     except:
#         posts = Business.objects.get(location=location)
#     return render(request,'neiba/post_list.html', locals())


class PostCreateView(CreateView):
    form_class = PostModelForm
    template_name = 'neiba/create_post.html'
 
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.user_profile= self.request.user.profile
        form.instance.location = self.request.user.profile.community
        return super().form_valid(form)




class BusinessCreateView(CreateView):
    form_class = BusinessModelForm
    template_name = 'hood/create_business.html'
 
    def form_valid(self, form):
        form.instance.bsn_user = self.request.user
        form.instance.bsn_community = self.request.user.profile.community
        return super().form_valid(form)


class CommunityCreateView(CreateView):
    form_class = CommunityModelForm
    template_name = 'community.html'
 
    try:
        def form_valid(self, form):
            form.instance.created_by = self.request.user
            # form.instance.user_profile= self.request.user.profile
            return super().form_valid(form)
    except:
        messages.success(request, f'Community with that name already exists.!')

def add_comment(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('home')

def left(request):
    location = get_object_or_404(Neighbourhood, pk=request.user.profile.community.id)
    if request.user.profile.community == location:
        request.user.profile.community= None
        request.user.profile.save()
    return redirect('home') 