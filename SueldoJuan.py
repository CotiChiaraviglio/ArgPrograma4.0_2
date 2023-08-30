ene_jun = 300
jul_oct = 500
nov_dic = 700

promedio = int((ene_jun + jul_oct + nov_dic) / 12) 

if promedio < 300:
  print("El sueldo de Juan es de", promedio, " dólares, y es un sueldo bajo")

elif promedio >= 300 and promedio <900:
  print("El sueldo de Juan es de", promedio, "dólares, y es un sueldo normal")

else :
  print("El sueldo de Juan de", promedio, "dólares, y es un sueldo mejor de lo normal.")


