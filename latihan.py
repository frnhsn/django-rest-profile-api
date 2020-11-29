# def decor(func):
#     def wrapper(x):
#         print("Before called")
#         func(x)
#         print("After called")
#     return wrapper

# def f(x):
#     print("Value of x:" + x)



# class decorator_class:
#     def __init__(self, f):
#         self.f = f

#     def __call__(self):
#         print("Decorating," + self.f__name__)
#         self.f()

# def foo():
#     print("Inside foo()")


# class Memoize:

#     def __init__(self, fn):
#         self.fn = fn
#         self.memo = {}

#     def __call__(self, *args):
#         if args not in self.memo:
#             self.memo[args] = self.fn(*args)
#         return self.memo[args]

# @Memoize
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(40))

# print(fib.memo)


# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# lst = [34, 978, 42]
# lst_backwards = Reverse(lst)
# for el in lst_backwards:
#     print(el)

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def fibi(n):
#     old, new = 0, 1

#     if n < 1:
#         print(0)
#     for x in range(1,n):
#         old, new = new, new + old
   
#     return new

# print(fibi(5))


# class A:
#     class_attr = "I am a class attribute!"

#     def __init__ (self):
#         self.instance_attr = "I am an instance attribute"

#     def instance_method(self):
#         print("Calling instance_attr ...")
#         return self.instance_attr

#     @staticmethod
#     def static_method():
#         print("Calling class_attr ... ")
#         return A.class_attr

#     @classmethod
#     def class_method(cls):
#         print("Calling class_attr ... ")
#         return cls.class_attr

# a = A()
# a.class_attr = "This is actually an instance attribute instead of class attribute"
# print(A.static_method())
# print(a.static_method())
# print(A.class_method())
# print(a.class_attr)
# print(a.__class__.class_attr)
# print(a.class_method())
# print(a.instance_method())
# prnt(A.instance_method())


# class A:
    
#     ca_A = "class attribute of A"
    
#     def __init__(self):
#         self.ia_A = "instance attribute of A instance"
        
# class B(A):
 
#     ca_B = "class attribute of B"
    
#     def __init__(self):
#         super().__init__()
#         self.ia_B = "instance attribute of A instance"


# a = A()
# print(a.ia_B)

# class SimpleDescriptor(object):
#     """
#     A simple data descriptor that can set and return values
#     """

#     def __init__(self, initval=None):
#         print("__init__ of SimpleDecorator called with initval: ", initval)
#         self.__set__(self, initval)

#     def __get__(self, instance, owner):
#         print(instance, owner)
#         print('Getting (Retrieving) self.val: ', self.val)
#         return self.val

#     def __set__(self, instance, value):
#         print('Setting self.val to ', value)
#         self.val = value

# class MyClass(object):
    
#     x = SimpleDescriptor("green")
    
# m = MyClass()
# print(m.x)
# m.x = "yellow"
# print(m.x)

# class SimpleClass:
#     x = "this is class attribute"

# a = SimpleClass()
# a.x = "I am overriding this class attribute"
# print(a.x)


# class A:
#     def m(self):
#         print("m of A called")

# class B(A):
#     def m(self):
#         print("m of B called")
#         super().m()
    
# class C(A):
#     def m(self):
#         print("m of C called")
#         super().m()

# class D(B,C):
#     def m(self):
#         print("m of D called")
#         super().m()

# x = D()
# x.m()

# print(D.mro())


# class Length:

#     __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
#                 "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
#                 "mi" : 1609.344 }
    
#     def __init__(self, value, unit = "m" ):
#         self.value = value
#         self.unit = unit
    
#     def Converse2Metres(self):
#         return self.value * Length.__metric[self.unit]
    
#     def __add__(self, other):
#         l = self.Converse2Metres() + other.Converse2Metres()
#         return Length(l / Length.__metric[self.unit], self.unit )
    
#     def __str__(self):
#         return str(self.Converse2Metres())
    
#     def __repr__(self):
#         return "Length(" + str(self.value) + ", '" + self.unit + "')"

# if __name__ == "__main__":
#     x = Length(4)
#     print(x)
#     y = eval(repr(x))

#     z = Length(4.5, "yd") + Length(1)
#     print(repr(z))
#     print(z)


# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             print(super(Singleton, cls).__call__(*args, **kwargs))
#             print(Singleton._instances)
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]

    
# class SingletonClass(metaclass=Singleton):
#     pass


# class RegularClass():
#     pass


# x = SingletonClass()
# y = SingletonClass()
# print(x == y)

# x = RegularClass()
# y = RegularClass()
# print(x == y)

class NoneElement(object):
    def __init__(self):
        self.value = None
        self.next = None

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        while counter != position:
            if current.next:
                current = current.next
                counter += 1
            else:
                return None
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        while counter + 1 < position:
            if current.next:
                current = current.next
                counter += 1
            else:
                return "Nothing was inserted"
        new_element.next, current.next = current.next, new_element
        return f'Inserted {new_element} on {position}'

    def delete(self, value):
        """Delete the first node with a given value."""
        counter = 1
        current = self.head
        while counter + 1 < value:
            if current.next:
                current = current.next
                counter += 1
            else:
                return "Nothing was deleted"
        current.next, current.next.next = current.next.next, None
        return None
    

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)