from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
     Task to send an e-mail notification when an order is
     successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'訂單編號. {order.id}'
    message = f'親愛的 {order.first_name}, \n\n ' \
              f'您的訂單已經成立，您的訂單編號是 {order.id} '
    mail_send = send_mail(subject=subject,
                          message=message,
                          from_email='admin@myshop.com',
                          recipient_list=[order.email])
    return mail_send
