# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#These are the assumed chatrooms that are available here.
chatrooms=['Python Basics','Intermediate Python','Advanced Python','Data Science With Python','Python With Web','Python For Hacking']
def index(request):
    return render(request,'chatrooms/chatroom.html',{'chatrooms':chatrooms})

