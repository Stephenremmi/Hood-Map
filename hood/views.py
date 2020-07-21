from django.shortcuts import render
import folium
from django.contrib.gis.geos import Point
from djanfo.contrib.auth.decorators import login_required

longitude = 36.8018676
latitude = -1.2614308

user_location = Point(longitude, latitude, srid=4326)
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    m = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([profile.home_location.y,profile.home_location.x],
                    popup='<h4>Neighbour hood.</h4>',
                    tooltip='My Home',
                    icon=folium.Icon(icon='glyphicon-home', color='darkgreen')).add_to(m),  
    folium.Marker([profile.work_location.y,profile.work_location.x],
                    popup='<h4>Neighbour hood</h4>',
                    tooltip='My workplace',
                    icon=folium.Icon(icon='glyphicon-wrench')).add_to(m)