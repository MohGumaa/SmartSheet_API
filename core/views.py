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
        'user_profile':  user_profile,
        "sheets": sheets,
    }
    return render(request, "core/index.html", context)

def view_sheet(request, id):
    sheet = user.Sheets.get_sheet(id)
    column_map = {column.title : column.id for column in sheet.columns}
    data = []

    # Get cells values
    for row in sheet.rows:
        cells = [row.get_column(col_id).value for col_id in column_map.values()]
        data.append(cells)

    # Get all Task column value
    for row in sheet.rows:
        for col_title, col_id in column_map.items():
            if col_title == 'Task':
                print(row.get_column(col_id).display_value)


    return JsonResponse({"column_map": column_map, "rows": data},safe=False)
