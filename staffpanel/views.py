from django.shortcuts import render
from django.views import View
from accounts.models import User
# Create your views here.


class StaffDetailView(View):
    def get(self,request):
        user = User.objects.get(id=request.user.id)
        return render(request,'staffpanel/index.html',{'user':user})