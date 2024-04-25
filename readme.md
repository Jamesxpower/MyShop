RUN rabbitMQ :

    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

RUN celery
    celery -A myshop worker -l info

    for windows platform 需要加上 -P eventlet 的參數
    celery -A myshop worker -l info -P eventlet


RUN readis
    docker run -it --rm --name redis -p 6379:6379 redis

gettext on Windows 下載連結
https://mlocati.github.io/articles/gettext-iconv-windows.html


Strip CLI 測試

    stripe listen --forward-to localhost:8000/payment/webhook/

Stripe 信用卡測試連結
    https://docs.stripe.com/testing



第 11 章 Adding Internationalization to Your Shop 
    https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter11

