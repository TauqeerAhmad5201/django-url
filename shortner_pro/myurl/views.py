from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import UrlPro
import uuid 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = UrlPro(link =link, uuid = uid)
        new_url.save()
        return HTTPResponse(uid)

def go(request, pk):
    url_details = UrlPro.objects.get(uuid=pk)
    return redirect('https://'+ url_details.link)