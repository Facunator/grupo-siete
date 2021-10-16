from turnos.validacionesTurnos import valDNI, valMes, valDia, valHora, valTurno
from funciones.arch_manipulacion import escribir_fichero

def regTurno(matriz):
    print("Registro de turnos inicializado. A considerar: \nDias no disponibles: 1, 8, 15, 22 \nHorario permitido: De 10:00 a 14:00 \nDuracion del turno: 15 minutos")
    print("*"*40, "\n")
    while True:
        try:
            dniTurno = input("Ingresar DNI del paciente: ")
            while valDNI(dniTurno)==False:
                dniTurno = input("Ingresar un DNI válido [8 dígitos]: ")
                
            mesTurno = input("Ingresar Mes de turno: ")
            while valMes(mesTurno) == False:
                mesTurno = input("Ingresar un Mes válido para el turno: ")
                
            diaTurno = input("Ingresar Día del turno: ")
            while valDia(diaTurno, mesTurno.title())==False:
                diaTurno= input("Ingresar un número de día válido para el mes ingresado: ")
            assert diaTurno not in [1,8,15,22], "Se ingresó un día en el que el médico no trabaja"
            
            horaTurno= input("Ingresar Hora del turno (horas:minutos): ")
            while valHora(horaTurno)==False:
                horaTurno= input("Ingresar una hora válida para el turno: ")
            horaComparar = int(horaTurno.replace(":",""))
            assert (1000<=horaComparar<=1400), "Se ingresó un horario en el que el médico no trabaja"
            
            datos = [dniTurno,mesTurno.title(),str(diaTurno),horaTurno]
            if valTurno(matriz,datos)==True:
                matriz.append(datos)
                try:
                    escribir_fichero('datos/turnos.txt', f'{dniTurno};{mesTurno.title()};{diaTurno};{horaTurno}', 'a')
                    print()
                    print('El turno ha sido registrado con éxito') 
                except FileNotFoundError:
                    print('No se encontró el archivo de turnos en el directorio específicado')
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