from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@shared_task
def payment_completed(order_id):
    """
     Task to send an e-mail notification when an order is
     successfully paid.
    """
    order = Order.objects.get(id=order_id)

    # create invoice e-mail
    subject = f'我的商店 - 訂單編號 {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@myshop.com',
                         [order.email])
    # generate PDF
    html = render_to_string(template_name='orders/order/pdf.html', context={'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(target=out, stylesheets=stylesheets)

    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')

    # send e-mail
    email.send()


