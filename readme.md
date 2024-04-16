RUN rabbitMQ :

    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

RUN celery

    celery -A myshop worker -l info

Strip CLI 測試

    stripe listen --forward-to localhost:8000/payment/webhook/

Stripe 信用卡測試連結
    https://docs.stripe.com/testing