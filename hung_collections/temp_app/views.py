from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'temp_app/index.html')

def testcube(request):
    return render(request, 'temp_app/testcube.html')