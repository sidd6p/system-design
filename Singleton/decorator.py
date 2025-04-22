def singleton(cls):
    instances = {}
    def get_instance(*args, **kargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kargs)
        return instances[cls]
    return get_instance

@singleton
class Singleton:
    def __init__(self):
    print("Singleton instance created")

# Testing the Singleton pattern
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True, both refer to the same instance