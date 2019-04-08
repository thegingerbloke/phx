from django_cron import CronJobBase, Schedule

from .models import Social


class SocialCronPost(CronJobBase):
    RUN_AT_TIMES = [
        '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
        '17:00', '18:00', '19:00', '20:00', '21:00'
    ]
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
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
