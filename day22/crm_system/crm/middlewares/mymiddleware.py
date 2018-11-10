from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
from django.contrib import auth

class Auth(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ['/crm/login/']:
            return None
        if request.path_info in ['/crm/index/']:

            return redirect('/crm/login/')





