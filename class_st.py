class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == "__main__":
    bob = Person('Bob Smith', 42, 30000, 'software')
