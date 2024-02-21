from django.shortcuts import render

# Create your view;s here.
def Index(request):
    return render(request,"index.html")