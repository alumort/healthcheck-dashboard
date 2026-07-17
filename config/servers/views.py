from django.shortcuts import redirect, render, get_object_or_404

from .forms import ServerForm
from .models import Server
from .services import check_server

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
            return redirect("server_list")

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

    checks = server.health_checks.order_by("-checked_at")[:10]

    last_check = checks.first()

    return render(
        request,
        "servers/server_detail.html",
        {
            "server": server,
            "last_check": last_check,
            "checks": checks,
        },
    )


def server_update(request, pk):
    server = get_object_or_404(Server, pk=pk)

    if request.method == "POST":
        form = ServerForm(request.POST, instance=server)

        if form.is_valid():
            form.save()
            return redirect("server_detail", pk=server.pk)

    else:
        form = ServerForm(instance=server)

    return render(
        request,
        "servers/server_update.html",
        {
            "form": form,
            "server": server,
        },
    )


def server_delete(request, pk):
    server = get_object_or_404(Server, pk=pk)
    if request.method == "POST":
        server.delete()
        return redirect("server_list")

    return render(
        request,
        "servers/server_delete.html",
        {
            "server": server
        },
    )

def server_check(request, pk):
    server = get_object_or_404(Server, pk=pk)

    check_server(server)

    return redirect("server_detail", pk=pk)