def f(x):
  return eval(function_f)
function_f=input()
a=int(input())
b=int(input())
n=int(input())
Es=0.5*(10**(2-n))
mid_old=None
print(f"Es={Es}")
print("\nIter\ta\t\tf(a)\t\tb\t\tf(b)\t\tmid\t\tf(mid)\t\tEa\t\tEr")
i=0
while True:
  i+=1
  mid=(a+b)/2
  if mid_old==None:
    Ea=0
    Er=0
  else:
    Ea=abs(mid-mid_old)
    Er=abs((mid-mid_old)/mid)*100
  print(f"{i}\t{a:.3f}\t\t{f(a):.3f}\t\t{b:.3f}\t\t{f(b):.3f}\t\t{mid:.3f}\t\t{f(mid):.3f}\t\t{Ea:.3f}\t\t{Er:.3f}")
  if f(a)*f(mid)<0:
    b=mid
  else:
    a=mid
  if mid_old is not None and Er<Es:
    break
  mid_old=mid
print("Root =", mid)