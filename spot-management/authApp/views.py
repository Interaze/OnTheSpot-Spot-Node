import json
import os
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

import replay_mission

from authApp.loadData import loadMap, loadMission

@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    return JsonResponse({"details": "CSRF cookie set"})


@require_POST
def login_view(request):
    """
    This will be `/api/login/` on `urls.py`
    """
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        return JsonResponse({
            "errors": {
                "__all__": "Please enter both username and password"
            }
        }, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Success"})
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )

def load_map(request):
    mapPath = request.GET['mapPath']

    return JsonResponse(loadMap(mapPath))

def load_mission(request):
    missionPath = request.GET['missionPath']

    return JsonResponse(loadMission(missionPath))

def run_mission(request):
    mapPath = request.GET['mapPath']
    os.system("python3 ./replay_mission.py ${SPOT_IP} autowalk '"+mapPath+"'")
    return JsonResponse(loadMap(mapPath))