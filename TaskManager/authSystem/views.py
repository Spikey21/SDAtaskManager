from django.shortcuts import render

# Create your views here.

# czy hasła sa takie same
# czy username wolny
# czy email wolny
# walidacja hasła


def register(request):

    return render(request, 'register.html')