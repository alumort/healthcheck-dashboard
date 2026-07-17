import requests
import time

from .models import Server, HealthCheck


def check_server(server: Server):
    inicio = time.perf_counter()

    try:
        response = requests.get(server.url, timeout=5)

        tiempo_ms = int((time.perf_counter() - inicio) * 1000)

        status = (
            HealthCheck.Status.UP
            if response.ok
            else HealthCheck.Status.DOWN
        )

        HealthCheck.objects.create(
            server=server,
            status=status,
            status_code=response.status_code,
            response_time=tiempo_ms,
        )

    except requests.Timeout:
        HealthCheck.objects.create(
            server=server,
            status=HealthCheck.Status.TIMEOUT,
            response_time=5000,
        )

    except requests.RequestException:
        HealthCheck.objects.create(
            server=server,
            status=HealthCheck.Status.DOWN,
            response_time=0,
        )