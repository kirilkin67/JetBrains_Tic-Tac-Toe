class House:
    construction = "building"
    elevator = True

# object of the class House
new_house = House()
print("Type", type(new_house))
print(dir(new_house))

stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff, 0))

class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))
print()

class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year


# name, last_name, birth_year = input(), input(), input()
student = Student(input(), input(), input())
print(student.id)

class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f"Hello, I am {self.name}!")


new_person = Person(input())
new_person.greet()
Person(input()).greet()

class Lightbulb:
    def __init__(self):
        self.state = "off"

    # create method change_state here
    def change_state(self):
        # 1 version
        if self.state == "off":
            self.state = "on"
        else:
            self.state = "off"
        # 2 version
        self.state = "on" if self.state == "off" else "off"
        # 3 version
        self.state = ("off", "on")[self.state == "off"]

        print("Turning the light {}".format(self.state))

class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100
		# 2 version
        self.dollars += deposit_dollars + (self.cents + deposit_cents) // 100
        self.cents = (self.cents + deposit_cents) % 100


bank = PiggyBank(1, 1)
bank.add_money(500, 500)
print(bank.dollars, bank.cents)

class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0

    # fix this method
    def add_friends(self, n):
        self.friends += n
        print("{} now has {} friends.".format(self.username, self.friends))

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


s = Stack()
s.is_empty()
s.push(0)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.pop()
s.peek()
s.pop()
print(s.is_empty())