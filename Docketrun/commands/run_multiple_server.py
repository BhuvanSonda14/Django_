# myapp/management/commands/run_multiple_servers.py
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Run Django server on multiple ports'

    def handle(self, *args, **kwargs):
        ports = [8000, 8001, 8002,8443,8080]
        for port in ports:
            os.system(f'python manage.py runserver {port} &')
