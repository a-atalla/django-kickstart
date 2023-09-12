from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def tenant_index(request):
    return render(request, "tenant_index.html", {"tenant_name": request.tenant})

