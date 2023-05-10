# Scrivi una classe Python per implementare la funzione elevazione_potenza(x,n) (in modo più formale pow(x,n)).

from datetime import date, datetime


class Test:
    @staticmethod
    def elevazione_potenza(x, n):
        output = 1
        for i in range(n):
            output = output * x
        return output


# t = Test()
# t.elevazione_potenza(2, 3)

Test.elevazione_potenza(2, 3)


class Person:
    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def age(self):
        return datetime.now() - self.birth_date


x = Person("Mario", "Rossi", date(2021, 10, 2))

x.age()
