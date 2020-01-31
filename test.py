# %%
import sys
import numpy

print(sys.executable)


def greeting(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greeting("world"))
