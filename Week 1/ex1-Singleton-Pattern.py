# ex1-Singleton-Pattern.py
# Placeholder for Singleton Pattern example

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    print(a is b)
