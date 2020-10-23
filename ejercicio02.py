
def menu():
    print("##################### Menu ######################################")
    print("1- Ingresar monto")
    print("2- Egresar monto")
    print("3- Reporte de ingresos")
    print("4- Reporte de egresos")
    print("5- Reporte de todas las transacciones")
    print("6- Reporte total de la cuenta")
    print("7- Salir")
    print("###############################################################")


    

class proyectoFinanzas:
    def __init__(self,monto):
        self.monto=monto

    def mostrarMonto(self):
        print("El monto es de: " + str(self.monto))

class ingresos:
    totIngresos = []
    def sumar(self,proyecto):
        cantidad = float(input("Ingrese monto: "))
        proyecto.monto+=cantidad
        self.totIngresos.append(cantidad)
    
    def mostrarReporteI(self,proyecto):
        o=0
        for i in self.totIngresos:
            o+=1
            print("Ingreso numero "+ str(o)+": "+ str(i))

class egresos:
    totEgresos = []
    def restar(self,proyecto):
        cantidad = float(input("Ingrese monto: "))
        proyecto.monto-=cantidad
        self.totEgresos.append(cantidad)
        
    def mostrarReporteE(self,proyecto):
        o=0
        for i in self.totEgresos:
            o+=1
            print("Egreso numero "+ str(o)+": "+ str(i))
   


print("-----------Bienvenido-----------")
print("presione 1 para crear cuenta")
print("presione cualquier tecla para salir")
if(input("opcion: ")!="1"):
    print("Adios")
else:
    #Creamos la cuenta e instancias de las clases ingresos y egresos
    proyecto = proyectoFinanzas(0)
    i= ingresos()
    e=egresos()
    flag = True
    while(flag):
        menu()
        opc= int(input("opcion: "))
        if(opc==1):
            i.sumar(proyecto)
        elif(opc==2):
            e.restar(proyecto)
        elif(opc==3):
            i.mostrarReporteI(proyecto)
        elif(opc==4):
            e.mostrarReporteE(proyecto)
        elif(opc==5):
            print("Ingresos: ")
            i.mostrarReporteI(proyecto)
            print("###############################")
            print("Egresos: ")
            e.mostrarReporteE(proyecto)
        elif(opc==6):
            proyecto.mostrarMonto()
        else:
            print("Adios")
            flag=False
        

    




