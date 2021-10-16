def valDNI(dni):
    if dni.isnumeric()==True and len(dni)==8:
        return True
    else:
        return False
    
def valMes(mescadena):
    listames = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    mescadena = mescadena.title()
    if mescadena.title() in listames:
        return True
    else:
        return False
    
def valDia(dia,mes):
    try:
        dia = int(dia)
        lista31= ["Enero","Marzo","Mayo","Junio","Julio","Agosto","Octubre","Diciembre"]
        if mes=="Febrero":
            diamax = 28
        elif mes in lista31:
            diamax = 31
        else:
            diamax = 30
            print(dia,diamax)
        if 1<=dia<=diamax:
            return True
        else:
            return False
    except:
        return False

def valHora(hora):
    listahora = hora.split(':')
    horasola = hora.replace(":","")
    if len(listahora)==2 and horasola.isnumeric()==True:
        num1, num2 = listahora
        num1 = int(num1)
        num2 = int(num2)
        if 0<=num1<24 and 0<=num2<=59:
            return True
        else:
            return False
    else:
        return False
    
def valTurno(matriz,data):
    if data in matriz:
        return False
    else:
        return True