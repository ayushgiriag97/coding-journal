# class Student():

#     def __init__ (self , name ,grade):
#         self.name = name
#         self.grade = grade

#     def study(self):
#         print(f"{self.name} is studying for grade {self.grade}")

# s1 = Student("Ayush" , "A")
# s2 = Student("Rahul" , "B")
# s1.study()
# s2.study()

# class Phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery

#     def show_status(self):
#         print(f"{self.brand} phone has {self.battery}%")

# p1 = Phone("iphone", "85")
# p2 = Phone("Samsung", "100")

# p1.show_status()
# p2.show_status()

# class Dog():
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def bark(self):
#         print(f"{self.name} says {self.sound}")

# s1= Dog("Bruno", "Bho Bho")
# s2 = Dog("Tommy" , "Woof")

# s1.bark()
# s2.bark()

# class BankAccount:
     
#      def __init__(self, owner, balance):
#         self.owner = owner 
#         self.balance = balance

#         def deposit(self, amount):
#             self.balance += amount
#             print(f"{amount} deposited . New balance: {self.balance}")

# u1 = BankAccount("Ayush" , 100000)
# u1.deposit

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit (self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance: {self.balance}")

# u1 = BankAccount("Ayush" , 100000)
# u1.deposit(10000)


# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def accleration(self, boost):
#         self.speed += boost
#         print(f"{self.brand} accelerated by{boost} km/h. Current spped: {self.speed} km/h")

# c1 = Car("Ferrari", 60)
# c1.accleration(40)

# class SmartPhone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery

#     def use_app(self, minutes):
#         self.battery -= minutes
#         print(f"{self.brand} used for {minutes} mins. Batter is now{self.battery}%")

#     def charge(self, amount):
#         self.battery += amount
#         print(f"{self.brand} charged by {amount}%. Battery is now {self.battery}%")

# p1 = SmartPhone("Iphone", 100)
# p1.use_app(30)
# p1.charge(15)

