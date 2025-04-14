from django_cron import CronJobBase, Schedule
from .models import Sistema
from django.utils import timezone
from datetime import timedelta

class ClearExpiredDataCronJob(CronJobBase):
    schedule = Schedule(run_every_mins=1440)  # Corre uma vez por dia (1440 minutos)
    code = 'app.clear_expired_data'

    def do(self):
        expiration_time = timezone.now() - timedelta(hours=24)
        expired_data = Sistema.objects.filter(updated_at__lte=expiration_time)

        # Exclui os dados expirados
        expired_data.delete()
