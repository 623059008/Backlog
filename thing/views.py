from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404

from thing.models import Thing
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from thing.serializers import UserSerializer, GroupSerializer, ThingSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class ThingViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows thing to be viewed or edited.
    '''
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

def index(request):
    latest_thing_list = Thing.objects.order_by('-id')[:5]
    template = loader.get_template('thing/index.html')
    context = Context({
        'latest_thing_list': latest_thing_list,
    })
    return render(request, 'thing/index.html',context)

def detail(request, thing_id):
    try:
        thing = Thing.objects.get(pk=thing_id)
    except Thing.DoesNotExist:
        raise Http404
    return render(request, 'thing/detail.html', {'thing': thing})

def results(request, thing_id):
    context = Context({
        'details_info': "name,detail,time,status"
    })
    return render(request, 'thing/detail.html', context)

def vote(request, thing_id):
    return HttpResponse("You're voting on user %s." % thing_id)
