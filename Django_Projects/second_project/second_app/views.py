from django.shortcuts import render
#from django.http import HttpResponse
#from second_app.models import User
from second_app.forms import NewUserForm
# Create your views here.

def index(request):
    #return HttpResponse('<em>My Second App</em>')
    return render(request, 'second_app/index.html')

def help(request):
    my_dict = {'help_page':'This is from help.html'}
    return render(request, 'second_app/help.html', context=my_dict)

def user(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')


    return render(request, 'second_app/users.html', {'form':form})



    '''users_list = User.objects.order_by('first_name')
    user_dict = {'user_records':users_list}
    return render(request, 'second_app/users.html', context=user_dict)'''
