### Week 2a Quiz ###
import simpleguitk as simplegui
print
# 5.
# Which of the following functions needs global x declaration?
x = 5

def d(y):
    y = x + y
    return y

print d(1)

def b(x,y):
    x = x + y
    return x

print b(x,2)

def c(y):
    return x + y

print c(1)

def a(y):
    global x
    x = x + y
    return y

print a(1)
print


# 6.
# What is the value of count at the end of this code?
count = 0

def square(x):
    global count
    count += 1
    return x**2

print square(square(square(square(3))))
print count
print


# 7.
# Which names occur in the global scope?
# 8.
# Which names occur in a local scope?
a = 3
b = 6

def f(a):
    c = a + b
    return c

print f(a)
print f(b)
print
