class MyNumbers:
  def __init__(self, start):
    self.a = start

  def __iter__(self):
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers(5)

for x in myclass:
  print(x)
