from django.shortcuts import render


def home_page(request):
    return render(request, "omotee_beauty/index.html")