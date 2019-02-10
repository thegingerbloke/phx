from django_cron import CronJobBase, Schedule

from .models import Social


class SocialCron(CronJobBase):
    RUN_AT_TIMES = ['10:00', '16:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'phx.social.cron'

    def do(self):
        social = Social()
        social.repost()
