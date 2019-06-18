from __future__ import absolute_import
from test_celery.celery import app
import time

@app.task
def longtime_add(x,y):
	print('Long time task begins')
	time.sleep(5)
	print('Long time task finished')

	return x+y


'''
You can see that we import the app defined in the previous celery module and use it as a decorator for our task method. Note that app.task is just a decorator. In addition, we sleep 5 seconds in our longtime_add task to simulate a time-expensive task:)
'''
