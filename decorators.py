# Decorators
from time import time

def my_decorator(func):
	def wrap_func():
		print('*'*15)
		func()
		print('*'*15)
	return wrap_func

@my_decorator
def hello():
	print('helloooo')

@my_decorator
def bye():
	print('see ya later')

hello()
bye()

# Decorators with args
def my_decorator2(func):
	def wrap_func2(*args, **kwargs):
		print('*'*15)
		func(*args, **kwargs)
		print('*'*15)
	return wrap_func2

@my_decorator2
def hello_again(greeting, emoji=':)'):
	print(greeting, emoji)

hello_again('hiii')

# time 

def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f'took {t2-t1} ms')
		return result
	return wrapper

@performance
def long_time():
	for i in range(10000000):
		i*5

long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
	def wrapper(*args, **kwargs):
		if args[0]['valid']:
			return fn(*args, **kwargs)
	return wrapper


   

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

