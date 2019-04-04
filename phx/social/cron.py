from django_cron import CronJobBase, Schedule

from .models import Social


class SocialCronPost(CronJobBase):
    RUN_EVERY_MINS = 60
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'phx.social.cron_post'

    def do(self):
        social = Social()
        social.post()


class SocialCronRePost(CronJobBase):
    RUN_AT_TIMES = ['10:00', '16:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'phx.social.cron_repost'

    def do(self):
        social = Social()
        social.repost()
