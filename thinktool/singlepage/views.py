from django.shortcuts import render,redirect
from django.views.generic import View
from .models import contact


# Create your views here.
class ContactAdd(View):
    def get(self, request):
        return render(request, 'singlepage/contact.html')
    def post(self, request):
        contactI =contact()
        contactI.title = request.POST.get("title")
        contactI.contact = request.POST.get("contact")
        contactI.content = request.POST.get("content")
        contactI.save()
        return redirect(to='frameList')
