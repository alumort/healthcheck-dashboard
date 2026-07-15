from django.shortcuts import render


def dashboard(request):
    return render(request, "servers/dashboard.html")

def server_list(request):
    return render(request, "servers/server_list.html")

def server_create(request):
    return render(request, "servers/server_create.html")

def server_detail(request, pk):
    return render(request, "servers/server_detail.html")

def server_update(request, pk):
    return render(request, "servers/server_update.html")

def server_delete(request, pk):
    return render(request, "servers/server_delete.html")