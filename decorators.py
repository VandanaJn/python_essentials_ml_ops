from time import sleep


def find(key):
    items={"1":"tomatoes","2":"potatoes","3":"onions","4":"cabbage"}
    return items.get(key)

def findall(find):
    keys=["1","3","7"]
    return [find(it) for it in keys if find(it) is not None]

print(findall(find=find))
print("closure")
#Closures are functions that contain other nested functions with state from outer function.
def outer(n1):
    def inner(n2):
        return n1+n2
    return inner

add_2=outer(2)
print(add_2(5))

def timed(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args,**kargs):
        import time
        start=time.time()
        func(*args,**kargs)
        end=time.time()
        print(f"{func.__name__} took {end-start} sec")
    return wrapper

@timed
def dummy(sec):
    sleep(sec)

dummy(1)
print(dummy.__name__)

def log_args(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kargs):
        for arg in args:
            print(arg)
        for key,value in kargs.items():
            print(f"{key}->{value}")
        func(*args, ** kargs)
    return wrapper
@log_args
def say_hello(name):
    print(f"Hello {name}")

say_hello("Alice")
say_hello(name="John")

def log(level, message):
     print(f"[{level.upper()}] {message}")
log("Info","user_logged in")
log("Error","something went wrong")
from functools import partial
log_info=partial(log,level="Info")
log_error=partial(log,"Error")
log_info(message="in progress")
log_error("try again")

def log_with_currying(level):
    def log_message(message):
        print(f"[{level.upper()}] {message}")
    return log_message
log_info_new=log_with_currying("info")
log_info_new("still in progress")

def find_max(*nums):
    return max(nums)
    
print(find_max(*[6,2,9,11,7]))
print(find_max(6,4,3))