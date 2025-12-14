import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {('none' if not args else args)}")
        logger.info(f"keyword parameters: {('none' if not kwargs else kwargs)}")
        logger.info(f"return: {result}")
        logger.info("======================")
    return wrapper

@logger_decorator
def fn1():
    print("function that takes no parameters and returns nothing")

@logger_decorator
def fn2(*args):
    print("function that takes a variable number of positional arguments and returns True")
    return True

@logger_decorator
def fn3(**kwargs):
    print("function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator")
    return logger_decorator

fn1()
fn2("ddd", 1, 2, True)
fn3(txt = "test string 4", num = 1234)
