import time
from spinLoop import spinLoop

def timeExe(n):
    start = time.clock()
    spinLoop(n)
    runtime = time.clock() - start
    return runtime

print(timeExe(10 ** 9))