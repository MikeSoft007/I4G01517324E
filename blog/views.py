from django.shortcuts import render

def home_view(request):
    food = "Vegatable"
    return render(
        request,
        "home.html",
        {"food": food}
    )
