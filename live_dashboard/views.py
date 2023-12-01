from django.shortcuts import render

def dashboard(request):
    return render(request, 'live_dashboard/dashboard.html')
