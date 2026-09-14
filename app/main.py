import sys

def hello(name="World"):
    return "Hello %s!" % name

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(hello(name))