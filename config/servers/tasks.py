from celery import shared_task

from .models import Server
from .services import check_server


@shared_task
def check_all_servers():

    servidores = Server.objects.filter(activo=True)

    for servidor in servidores:
        check_server(servidor)