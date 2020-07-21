from django.conf.urls import url
from . import views
from .views import PostCreateView,CreateView,BusinessCreateView

urlpatterns=[
    url(r'^$',views.post_listview,name='home'),
    url(r'^change_user_role/(?P<pk>[0-9]+)$',views.change_user_role,name='change'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    url(r'^new/business/$', BusinessCreateView.as_view(), name='business-create'),
    # url(r'^signout/$', views.signout, name='signout'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^add_neihbourhood/',views.CommunityCreateView.as_view(), name='add_community'),
    url(r'^comment/(?P<post_id>\d+)', views.add_comment, name='comment'),
    url(r'^business/$', views.business_listview, name='business'),
    url('business/(?P<post_id>\d+)/', views.singlebsnview, name='business-detail'),
    url(r'^leavecomminity/$', views.left, name='left'),
    url(r'^joincomminity/(?P<new_community>\d+)/$', views.join, name='join'),

]