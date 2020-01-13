def add_name(name):
    def wrapper(cls):
        cls.NAME = name
        return cls
    return wrapper


@add_name('tom')  # Person = add_name('tom')(Person)
class Person:
    pass


def main():
    print(Person.__dict__)


if __name__ == '__main__':
    main()
