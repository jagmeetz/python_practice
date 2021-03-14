import time
def x():
    start_time = time.time()
    for i in range(0,1000000000):
        pass
    end_time = time.time()
    return end_time-start_time

n = 5
print("  and required time to calculate is :",x())