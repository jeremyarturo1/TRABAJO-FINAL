#Crear un Sistema que solicite el monto, cantidad de cuotas o (plazo) en meses, porcentaje de interes anual de un préstamo. Calcule la cuota mensual y muestre la tabla amortizada de los meses.


#1.    Usar ciclos, clases, metodos o funciones, condiciones, vectores o tablas, etc.

#2.    El Proyecto debe subirlo a un repositorio. Su suben archivos comprimido al repositorio del Proyecto automaticamente perderan 10 puntos.

#3.    Deben crear atributos con tipos de datos correspondiente a la información que van a tener.

#4.    Las variables deben tener nombres alusivos a su información.

#5.    Tratar de usar codigo legible y divider en subprogramas o funciones, cuando entiendan sea necesario.


'''Tabla de amortizacion'''

capital=float(input("Ingrese la capital a prestar:\n"))
plazos=(int(input("Ingrese los plazos para pagar el monto de: "+str(capital)+"\n")))
interes=(float(input("Ingrese ahora los intereses para pagar el capital\n")))

interes=interes*0.01

plazos_almacenada=capital*(((1+interes)**plazos)*interes)

plazos_almacenada=plazos_almacenada/(((1+interes)**plazos)-1)

saldo=capital

plazos_almacenada="{0:.2f}".format(plazos_almacenada)

for i in range (1,plazos + 1):
    
    #Operacion
    
    interes_operable="{0:.2f}".format(float(saldo)*float(interes))

    abono="{0:.2f}".format(float(plazos_almacenada)-float(interes_operable))

    saldo="{0:.2f}".format(float(saldo)-float(abono))
    if(float(saldo)<0):
        saldo="Completado"
    print("Periodo:{0}| Cuota:{1}| Intereses:{2}| Abono:{3}| Saldo:{4}\n\n".format(i,plazos_almacenada,interes_operable,abono,saldo))