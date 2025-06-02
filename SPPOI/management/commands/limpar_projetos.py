from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from SPPOI.models import Projeto

class Command(BaseCommand):
    help = 'Remove projetos com mais de 24 horas de criação'

    def handle(self, *args, **kwargs):
        limite = timezone.now() - timedelta(hours=24)
        deletados, _ = Projeto.objects.filter(criado_em__lt=limite).delete()
        self.stdout.write(self.style.SUCCESS(f'{deletados} projetos apagados.'))