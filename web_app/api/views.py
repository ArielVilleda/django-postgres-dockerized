from django.shortcuts import render
from django.http import HttpResponse
import os


def test_view(request, *args, **kwargs):
    env_msg_test = os.environ.get('ENV_MSG_TEST', '.env variable not read')
    return HttpResponse('<h1>Test v1.0.0, ' + env_msg_test + '</h1>')
