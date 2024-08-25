"""
#
# Part: python class and objest
#
"""
# Mask a Class
class MyClass:
    x = 5

# call a class
objest1 = MyClass()
print("1:", objest1.x)
objest2 = MyClass()
print("2:", objest2.x)

class Person:
    def __init__(self, name_p, age_p):
        pass
        self.name = name_p
        self.age = age_p

    def __str__(self):
        return f"{self.name} - {self.name}"
    
    def sayHi(self, lastname):
        print("Hey yo what'sup" + "" + lastname)

p1 = Person("John", 20)
print(p1.name, p1.age)
print(p1)

p1.sayHi("Son")

p2 = Person("Joe", 30)
print(p2.name, p2.age)
print(p2)

p2.sayHi("Nathan")


class Car:
    def __init__(self, body_color, engine_size):
        self.wheels = 4
        self.window = 4
        self.window_front = 1
        self.window_back = 1
        self.body_color = body_color
        self.engine_size = engine_size

        def push_window_button(self):
            #do something
            pass

        def pop_window_button(self):
            #do something
            pass

        def calSpeed(self):
            speed = self.engine_size * 1000
            return speed

        def turn_on_front_light(self,status):
            if status == "on":
                # do something
                pass
            else:
                # do something
                pass

        