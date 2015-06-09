nombre = input("Ingresar El Nombre Del Vendedor")
venta1 = int(input("Ingresar La venta Del Primer Mes"))
venta2 = int(input("Ingresar La venta Del segundo Mes"))
venta3 = int(input("Ingresar La venta Del Tercer Mes"))
comision =(venta1+venta2+venta3) *0.125
print ("Informe De Comisiones\n"+"vendedor\tVentas\tComision\n"+nombre+"\t"+str(venta1+venta2+venta3)+"\t"+str(comision)+"n")