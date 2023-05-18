import json
import pika
import django
import os
import sys
import time
from django.core.mail import send_mail
from pika.exceptions import AMQPConnectionError

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presentation_mailer.settings")
django.setup()


def process_approval(ch, method, properties, body):
    message = json.loads(body)
    presenter_email = message["presenter_email"]
    presenter_name = message["presenter_name"]
    presentation_title = message["title"]

    send_mail(
        "Your presentation has been accepted",
        f"{presenter_name}, we're happy to tell you that your presentation {presentation_title} has been accepted",
        "admin@conference.go",
        [presenter_email],
    )


def process_rejection(ch, method, properties, body):
    message = json.loads(body)
    presenter_email = message["presenter_email"]
    presenter_name = message["presenter_name"]
    presentation_title = message["title"]

    send_mail(
        "Your presentation has been rejected",
        f"{presenter_name}, we regret to inform you that your presentation {presentation_title} has been rejected",
        "admin@conference.go",
        [presenter_email],
    )


while True:
    try:
        parameters = pika.ConnectionParameters(host="rabbitmq")
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue="presentation_approvals")
        channel.basic_consume(
            queue="presentation_approvals",
            on_message_callback=process_approval,
            auto_ack=True,
        )
        channel.queue_declare(queue="presentation_rejections")
        channel.basic_consume(
            queue="presentation_rejections",
            on_message_callback=process_rejection,
            auto_ack=True,
        )
        channel.start_consuming()
    except AMQPConnectionError:
        print("Could not connect to RabbitMQ")
        time.sleep(2.0)
