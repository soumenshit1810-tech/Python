import inspect

def demo(a, b=5, *args, **kwargs):
    pass

print(inspect.signature(demo))
