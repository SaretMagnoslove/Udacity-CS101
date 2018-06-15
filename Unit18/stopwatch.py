import time

def timeExe(code):
    start = time.clock()
    result = eval(code)
    runtime = time.clock() - start
    return result, runtime

