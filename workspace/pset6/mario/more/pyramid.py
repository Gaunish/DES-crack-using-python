
def pyramid():

  while True:
    i = int(input("enter height of pyramid:"))
    if i>1 and i<8:
      break

  k=i
  l=0
  x=' '

  while True:
    k = k-1
    for j in range(k):
      print(x,end="")

    l=l+1
    for m in range(l):
      print("#",end="")

    print("  ",end="")

    for c in range(l):
        print("#",end="")

    print("\n")

    if l==i:
     break


pyramid()