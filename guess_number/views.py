from django.shortcuts import render
import random

def index(request):
    lucky_number = random.randint(1, 10)
    context = {"lucky_number": lucky_number}
    return render(request, "index.html", context)
