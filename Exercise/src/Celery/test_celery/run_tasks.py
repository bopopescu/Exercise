from .tasks import longtime_add

if __name__=='__main__':
	result=longtime_add.delay(1,2)
	print('Task finished ',result.ready())

	print('Task result ',result.result)
	time.sleep(10)
	print('Task finished?',result.ready())
	print('Task result',result.result)



'''
Here, we call the task longtime_add using the delay method, which is needed if we want to process the task asynchronously. In addition, we keep the results of the task and print some information. The ready method will return True if the task has been finished, otherwise False. The result attribute is the result of the task (“3” in our case). If the task has not been finished, it returns None.
'''
