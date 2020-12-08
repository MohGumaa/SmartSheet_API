from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
import smartsheet

# Initialize client and make sure we don't miss any errors
user =  smartsheet.Smartsheet(config('API_KEY'))
user.errors_as_exceptions(True)


def index(request):
    user_profile = user.Users.get_current_user()

    # Get all sheets
    sheets = user.Sheets.list_sheets(include="attahments,source", include_all=True).data

    context = {
        "sheets": sheets
    }
    return render(request, "core/index.html", context)

def view_sheet(request, id):
    sheet = user.Sheets.get_sheet(id)
    cols = [col.title for col in sheet.columns]
    print(cols)
    return JsonResponse(cols,safe=False)
