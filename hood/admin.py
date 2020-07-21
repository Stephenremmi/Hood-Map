from django.contrib import admin
from .models import Neighbourhood,Profile,Post,Business
# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)