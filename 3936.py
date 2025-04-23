def hanoi(n, fro, to, additional) :

  if (n == 0) : return

  hanoi(n-1,fro,additional,to)

  print(fro,to)

  hanoi(n-1,additional,to,fro)

 

n = int(input())

hanoi(n,1,2,3)