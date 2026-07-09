class ExampleSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
# ======================================
a = ExampleSingleton()
b = ExampleSingleton()
z = ExampleSingleton()

print( id(a) )
print( id(b) )
print( id(z) )