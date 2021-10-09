''' Registro del turno (dni, mes, dia, hora)
limites:
    dias no permitidos - 1, 8, 15, 22
    horas permitidas - de 10:00 a 14:00
    no se permiten tener dos turnos a la vez (ej: 9:30 y 9:40)
    
Funciones:
registroTurno = Iniciliza el registro de turnos para cargarlos en una matriz
verificarMes  = Verifica que el mes ingresado corresponda a nuestro calendario
verificarDia  = Verifica que el dia ingresado corresponda a uno de los días disponibles en su respectivo mes
'''

def registroTurno(matriz):
    print("Registro de turnos inicializado. A considerar:")
    print("Dias no disponibles: 1, 8, 15, 22")
    print("Horario permitido: De 10:00 a 14:00")
    print("Duracion del turno: 15 minutos")
    print("*"*40)
    print()
    while True:
        try:
            dniTurno = input("Ingresar DNI del paciente: ")
            
            mesTurno = input("Ingresar Mes de turno: ")
            mesTurno = verificarMes(mesTurno)
            
            diaTurno = input("Ingresar Día del turno: ")
            while diaTurno.isnumeric()==False:
                diaTurno= input("Ingresar un número válido para el día: ")
            diaTurno = int(diaTurno)
            while verificarDia(diaTurno, mesTurno)==False:
                diaTurno= input("Ingresar un número de día válido para el mes ingresado: ")
            assert diaTurno not in [1,8,15,22], "Se ingresó un día en el que el médico no trabaja"
            
            horaTurno= input("Ingresar Hora del turno (horas:minutos): ")
            while verificarHoraValida(horaTurno)==False:
                horaTurno= input("Ingresar una hora válida para el turno: ")
            horaComparar = int(horaTurno.replace(":",""))
            assert (1000<=horaComparar<=1400), "Se ingresó un horario en el que el médico no trabaja"
            
            datos = [dniTurno,mesTurno,diaTurno,horaTurno]
            if validarTurno(matriz,datos)==True:
                matriz.append(datos)
            else:
                print("Error al registrar el turno: Ya hay un turno registrado para esa fecha y horario")
        except AssertionError as error:
            print("Error al registrar el turno:",error)
        finally:
            decision = input("Registrar otro turno? (s/n): ")
            while decision not in ["s","n"]:
                decision = input("Ingresar una opción válida. Opciones -> s - Si; n - No :")
            if decision == "n":
                print("Finalizando el registro..")
                break
            
def verificarMes(mescadena):
    listames = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    mescadena = mescadena.title()
    while not mescadena in listames:
        mescadena = input("Reingresar un Mes válido: ")
        mescadena = mescadena.title()
    return mescadena

def verificarDia(dia,mes):
    lista31= ["Enero","Marzo","Mayo","Junio","Julio","Agosto","Octubre","Diciembre"]
    if mes=="Febrero":
        diamax = 28
    elif mes in lista31:
        diamax = 31
    else:
        diamax = 30
    if dia<1 or dia>diamax:
        return False
    else:
        return dia

def verificarHoraValida(hora):
    listahora = hora.split(':')
    horasola = hora.replace(":","")
    if len(listahora)==2 and horasola.isnumeric()==True:
        num1, num2 = listahora
        num1 = int(num1)
        num2 = int(num2)
        if 0<=num1<24 and 0<=num2<59:
            return True
        else:
            return False
    else:
        return False

def validarTurno(matriz,data):
    valido = True
    for f in range (len(matriz)):
        if matriz[f][1] == data[1] and matriz[f][2] == data[2] and matriz[f][3] == data[3]:
            valido = False
    return valido
            
matrizTurnos = [["DNI", "Mes", "Dia", "Hora"],["1503","Febrero",13,"10:30"]]
registroTurno(matrizTurnos)
print(matrizTurnos)
