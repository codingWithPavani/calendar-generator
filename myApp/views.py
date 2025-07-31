from django.shortcuts import render
import calendar
from calendar import month_name

def view_cal(request):
    cal_output = None
    year = None
    month = None
    month_name_display = None

    if request.method == 'POST':
        year = request.POST.get('year')
        month = request.POST.get('month')
        if year and month:
            try:  
                year = int(year)
                month = int(month)
                if 1 <= month <= 12:
                    cal = calendar.HTMLCalendar().formatmonth(year, month)
                    cal_output = cal
                    month_name_display = month_name[month]
                else:
                    cal_output = "<div class='error-message'>Invalid month. Please enter a value between 1 and 12.</div>"
            except ValueError:
                cal_output = "<div class='error-message'>Invalid input. Please enter valid numbers for both month and year.</div>"
                 
    return render(request, 'myApp/index.html', {
        'calendar': cal_output, 
        'year': year, 
        'month': month,
        'month_name': month_name_display
    })