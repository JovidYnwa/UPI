from celery import shared_task

from time import sleep

@shared_task
def sleep_task(total_time):

    sleep(total_time)
    print('ahahaha')
    return 'love for Foli'