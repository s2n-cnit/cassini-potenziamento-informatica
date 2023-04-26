from datetime import datetime


class Person:
    def __init__(self, name: str, surname: str,
                 tax_id: str, birth_date: datetime):
        self.__name = name
        self.__surname = surname
        self.__tax_id = tax_id
        self.__birth_date = birth_date

    def age(self):
        d = datetime.now() - self.__birth_date
        return int(d.days / 365)

    def __str__(self):
        return f"{self.__name} {self.__surname} " \
               f"({self.__birth_date.day}/{self.__birth_date.month}/{self.__birth_date.year})"

    def name(self, value=None):
        if value is None:
            return self.__name
        self.__name = value
        return self  # To obtain the chain-method-call

    def surname(self, value=None):
        if value is None:
            return self.__surname
        self.__surname = value
        return self

    def tax_id(self, value=None):
        if value is None:
            return self.__tax_id
        self.__tax_id = value
        return self

    def birth_date(self, value=None):
        if value is None:
            return self.__birth_date
        self.__birth_date = value
        return self

    def is_older(self, p):
        return self.birth_date() < p.birth_date()

    def is_younger(self, p):
        return self.birth_date() > p.birth_date()

    def has_same_age(self, p):
        return self.birth_date() == p.birth_date()


teacher = Person("Alessandro", "Carrega",
                 "CRRLSN82B27F965V", datetime(2000, 4, 5))

print(teacher)  # == print(str(teacher))

# It is not possible to do
# p.__name = "Mark" because __name is private
teacher.name("Mark") \
    .surname("Right") \
    .birth_date(datetime(2001, 4, 5))

print(teacher)

# Exercise
# Try to declare 2 objects of type Person e check who is the oldest one.
# Objects: p1 & p2

p1 = Person("P1 Name", "P1 Surname", "P1-TaxCode", datetime(2003, 6, 7))
p2 = Person("P2 Name", "P2 Surname", "P2-TaxCode", datetime(2005, 6, 5))

if p1.is_younger(p2):
    print(f"{p2} is older than {p1}")
elif p1.is_older(p2):
    print(f"{p1} is older than {p2}")
else:
    print(f"{p1} has the same age of {p2}")
