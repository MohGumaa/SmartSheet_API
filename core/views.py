from django.shortcuts import render
import smartsheet
from decouple import config


# Initialize client and make sure we don't miss any errors
user =  smartsheet.Smartsheet(config('API_KEY'))

def index(request):
    user_profile = user.Users.get_current_user()

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'core/index.html', context)

def view_sheet(request):

    return "hello"
