from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.
class RegisterUser(View):
    def get(self, request):
        return JsonResponse({"message": "working"}, status=201)
