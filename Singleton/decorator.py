def singleton(cls):
    # This is a decorator function that implements the Singleton pattern.
    # It takes a class 'cls' as input and modifies its instantiation behavior.
    instances = (
        {}
    )  # This dictionary will store the single instance of each decorated class.
    # The class itself will be the key, and the instance will be the value.

    def get_instance(*args, **kargs):
        # This is the inner function that will replace the original class constructor.
        # It takes arbitrary positional (*args) and keyword (**kargs) arguments,
        # allowing it to handle the arguments that would normally be passed to the class's '__init__'.
        if cls not in instances:
            # Check if an instance of the decorated class 'cls' has already been created
            # and stored in the 'instances' dictionary.
            instances[cls] = cls(*args, **kargs)
            # If no instance exists, create a new instance of the class 'cls' by calling it
            # with the provided arguments. This new instance is then stored in the 'instances'
            # dictionary with the class 'cls' as the key.
        return instances[cls]
        # Regardless of whether a new instance was just created or an existing one was retrieved,
        # this function returns the single instance of the class stored in the 'instances' dictionary.

    return (
        get_instance  # The 'singleton' decorator returns the 'get_instance' function,
    )
    # which will be used as the new way to "instantiate" the decorated class.


@singleton
class Singleton:
    # This is a class decorated with the '@singleton' decorator.
    # This means that the 'singleton' function will control the creation of its instances.
    def __init__(self):
        # The '__init__' method is called only once, the first time an instance is created
        # by the 'get_instance' function within the 'singleton' decorator.
        print("Singleton instance created")


# Testing the Singleton pattern
obj1 = Singleton()
# When we try to create 'obj1', the 'get_instance' function (returned by 'singleton') is called.
# Since 'Singleton' is not yet in 'instances', a new instance is created, the '__init__' method is executed,
# and the instance is stored in 'instances'. 'obj1' refers to this instance.

obj2 = Singleton()
# When we try to create 'obj2', 'get_instance' is called again.
# This time, 'Singleton' is already a key in 'instances', so a new instance is NOT created.
# Instead, the existing instance that was created for 'obj1' is retrieved from 'instances'.
# 'obj2' refers to the same instance in memory as 'obj1'.

print(obj1 is obj2)  # Output: True, both 'obj1' and 'obj2' refer to the same instance.
