from celery import shared_task

from time import sleep

from transactions.models import Transaction

@shared_task
def sleep_task(total_time):
    sleep(total_time)
    return 'lo lo lo'


@shared_task
def transactions_amount():
    query = Transaction.objects.count()
    print(f"the total amount of transactions equals to {query}")
    return query