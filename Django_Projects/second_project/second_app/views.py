from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
# Create your views here.

def index(request):
    #return HttpResponse('<em>My Second App</em>')
    return render(request, 'second_app/index.html')

def help(request):
    my_dict = {'help_page':'This is from help.html'}
    return render(request, 'second_app/help.html', context=my_dict)

def user(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'user_records':users_list}
    return render(request, 'second_app/user.html', context=user_dict)
