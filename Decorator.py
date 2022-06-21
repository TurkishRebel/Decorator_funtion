def mukemmel(fonk):
 def wrapper():
  mükemmel = []
  for i in range(3, 1001):
     toplam = 0
     c = 2
     while i-1 > c:
      if i % c == 0:
       toplam = c + toplam
       c = c+1
      else:
         c= c + 1
     if toplam == i-1:
        mükemmel.append(i)
  print("Mükemmel sayılar = "+ str(mükemmel))
  fonk()
 return(wrapper)
@mukemmel
def asal_mi():
  asal = []
  for i in range(3,1001):
   c = 2
   while i-1 > c:
    if i % c == 0:
      break
    else :
       c = c+1
   if i-1 == c:
       asal.append(i)
  print("Asal sayılar = "+ str(asal))
asal_mi()