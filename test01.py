for i in range(5):
  for j in range(20):
    if ((i+j)%3 == 0):
      print('#',end=" ")
    else:
      print('.',end=" ")
  print()