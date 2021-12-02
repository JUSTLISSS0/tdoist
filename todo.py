myTodo = ["clean my room 5 times#","do some homework 8 times","#play a little bit of video games before i go to bed","go shopping for myself again","fold my clothes 11 times in a row#"]
print(myTodo)
print(f'{len(myTodo)} thing(s) left to do')
print(myTodo.index("clean my room 5 times#"))
for task in myTodo:
  print(task)
myTodo.append("hello")
for task in myTodo:
  print(task)
myTodo.remove ("clean my room 5 times#")
for task in myTodo:
  print(task)
myTodo.sort()
for task in myTodo:
   print(task)
myTodo.insert(2, "im the best")
for task in myTodo:
  print(task)
myTodo.reverse()
for task in myTodo:
  print(task)
myTodo.clear()
for task in myTodo:
  print(task)