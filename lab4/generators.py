#ex1
N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x*x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#ex2
N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    if(x % 2 == 0):
        if(x!=N and x!=N-1 ):
         print(x, end=', ')
        else:
         print(x)

#ex3
N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    if(x % 3 == 0) and (x % 4 == 0):
      print(x)

#ex4
a = int(input())
b = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = a
    return self

  def __next__(self):
    if self.a <= b:
      x = self.a
      self.a += 1
      return x*x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    
      print(x)

#ex5
N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = N
    return self

  def __next__(self):
    if self.a >= 0:
      x = self.a
      self.a -= 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
  
