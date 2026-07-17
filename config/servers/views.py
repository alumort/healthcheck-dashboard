from django.shortcuts import redirect, render, get_object_or_404

from .forms import ServerForm
from .models import Server

def dashboard(request):
    servidores = Server.objects.all()

    return render(
        request,
        "servers/dashboard.html",
        {
            "servidores": servidores
        }
    )

def server_list(request):
    servidores = Server.objects.all()
    return render(request, "servers/server_list.html", {"servidores": servidores,})

def server_create(request):

    if request.method == "POST":
        form = ServerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = ServerForm()

    return render(
        request,
        "servers/server_create.html",
        {
            "form": form
        }
    )


def server_detail(request, pk):
    server= get_object_or_404(Server, pk=pk)
    return render(request, "servers/server_detail.html", {"server": server},)

def server_update(request, pk):
    return render(request, "servers/server_update.html")

def server_delete(request, pk):
    return render(request, "servers/server_delete.html")