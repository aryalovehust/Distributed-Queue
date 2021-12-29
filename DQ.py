from random import seed
import random
seed()
L = []
def tree_split(arr,n):
  mini = -1
  tmp = -1
  print("Minislots Occupation: ",arr)
  for i in range(len(arr)):
    if len(arr[i]) > 1 and len(arr[i]) > mini:
      mini = len(arr[i])
      tmp = i
    # if len(arr[i]) == 1:
    #   print("Appending: ",arr[i])
    #   L.append(arr[i])
    #   print("L: ",L)
                 
  queue = []
  for i in range(len(arr)):
    if len(arr[i]) > 1:
      queue.append(arr[i])
  if len(queue) != 0:
    for i in range(len(arr)):
      if len(arr[i]) == 1:
        print("Send to DTQ: ",arr[i])
        L.append([arr[i], [], []])
        print("L: ",L)  

  for i in range(len(queue)):
    for j in range(i, len(queue)):
      if len(queue[j]) > len(queue[i]) :
        queue[i], queue[j] = queue[j], queue[i]
  print("**Send to CRQ:")
  print(queue)
  for j in range(len(queue)):
    new_arr = []
    for i in range(n):
      new_arr.append([])
    print("**************************************************")
    print("Processing group: ",queue[j])
    # pos = 0
    for i in queue[j]:
      pos = random.randint(0,n-1)
      new_arr[pos].append(i)
      # pos = (pos+1)%n
    # print("New arr:")
    # print(new_arr)
    tree_split(new_arr,n)
  
  if len(queue) == 0:
    print("Send to DTQ: ",*arr)
    L.append(arr)
    print("L: ",L)

a = [[6,7,8,9,10],[2,3],[0,1,4,5]]

tree_split(a,3)
print("***************************************")
print("Resolved Tree:")
for i in L:
  print(i)
