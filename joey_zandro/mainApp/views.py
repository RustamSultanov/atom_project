from django.shortcuts import render


def mainpage(request):
    return render(request, 'mainApp/templates/mainpage.html')


def about_page(request):
    return render(request, 'mainApp/templates/about.html')
