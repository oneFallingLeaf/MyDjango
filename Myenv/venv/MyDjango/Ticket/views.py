from django.shortcuts import render
from .forms import UserAccountForm
# Create your views here.
def home(request):
    userForm = UserAccountForm
    context = {
        'user_form':userForm

    }
    return render(request,'base.html',context)
