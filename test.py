from utils import timer_with_log_identifier

@timer_with_log_identifier(log_identifier="TIMER")
def add(a,b):
    return a+b

if __name__ == "__main__":
    add(3,4)
