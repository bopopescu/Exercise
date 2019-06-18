from __future__ import absolute_import
from celery import Celery

app=Celery('test_celery',
	    broker='amqp://navaneeth:navaneeth_host@localhost/navaneeth_host',
	    backened='amqp',
	    include=['test_celery.tasks'])

#transport://userid:password@hostname:port/virtual_host

'''
Here, we initialize an instance of Celery called app, which is used later for creating a task.

The first argument of Celery is just the name of the project package, which is “test_celery”.

The broker argument specifies the broker URL, which should be the RabbitMQ we started earlier. Note that the format of broker URL should be:
transport://userid:password@hostname:port/virtual_host

For RabbitMQ, the transport is amqp.

The backend argument specifies a backend URL. A backend in Celery is used for storing the task results. So if you need to access the results of your task when it is finished, you should set a backend for Celery.

rpc means sending the results back as AMQP messages, which is an acceptable format for our demo. More choices for message formats can be found here.

The include argument specifies a list of modules that you want to import when Celery worker starts. We add the tasks module here so that the worker can find our task.
'''


