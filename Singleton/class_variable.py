class Singleton:
    # This is a class implementing the Singleton design pattern.
    # The goal is to ensure that only one instance of this class can ever exist.
    _instance = None  # This class-level variable will hold the single instance of the class. It's initialized to None.

    def __new__(cls):
        # This special method '__new__' is called before '__init__' when an object is created.
        # It's responsible for creating and returning the instance of the class.
        if cls._instance is None:
            # Check if an instance of this class has already been created.
            # If '_instance' is None, it means this is the first time we're trying to create an instance.
            cls._instance = super(Singleton, cls).__new__(cls)
            # If no instance exists, we create a new one using the '__new__' method of the superclass (object).
            # This newly created instance is then stored in the '_instance' variable.
        return cls._instance
        # Regardless of whether a new instance was just created or an existing one was found,
        # this method returns the single, stored instance of the class.


obj1 = Singleton()
# When we try to create the first object 'obj1', '__new__' is called.
# Since '_instance' is None, a new instance is created and stored in '_instance'.
# 'obj1' will refer to this newly created instance.

obj2 = Singleton()
# When we try to create the second object 'obj2', '__new__' is called again.
# This time, '_instance' is not None (it holds the instance created for 'obj1').
# Therefore, a new instance is NOT created. Instead, the existing instance stored in '_instance' is returned.
# 'obj2' will also refer to the same instance in memory as 'obj1'.

print(obj1 is obj2)
# This line checks if 'obj1' and 'obj2' refer to the exact same object in memory.
# Because of the Singleton implementation, this will always print True.
