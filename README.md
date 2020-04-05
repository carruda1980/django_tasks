# django_tasks
This repository is about leaning how to use Celery and RabbitMQ

## Installation

1- Installing Celery
- [x] pip3 install Celery

2- Installing RabbitMQ
- [x] apt-get install -y erlang
- [x] apt-get install rabbitmq-server

3- Enable rabbitmq
- [x] systemctl enable rabbitmq-server
- [x] systemctl start rabbitmq-server

4- Checking status
- [x] systemctl status rabbitmq-server

5- Checking the tasks on celery
- [x] celery -A tasks worker -l info
