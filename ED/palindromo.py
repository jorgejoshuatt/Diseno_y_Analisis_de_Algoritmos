for h in range(0,24,1):
  for m in range (0,60,1):
    horario="0"+str(h)+":"+"0"+str(m) 
    if h<10:
      horario="0"+str(h)+":"+str(m)
    if m<10:
      horario=str(h)+":"+"0"+str(m)
    palindromo=horario[::-1] 
    if palindromo==horario:
      print(f"{horario} es un palindromo\n")
