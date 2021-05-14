# __main__.py
from .reader import Reader

def main():
    r = Reader("role", 0)
    r.get_unused()

if __name__ == "__main__":
    main()