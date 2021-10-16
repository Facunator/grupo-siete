# app principal
import pantallas.reg_paciente as registro_p
import pantallas.menu as menu
import turnos.RegistroTurno as rt
import os
clear = lambda: os.system('cls')
clear()
opcion = menu.consulta_opcion()

matrizTurnos= [["DNI","Mes","Dia","Hora"]]
while opcion != 0:
    clear()
    if opcion == 1:
        rt.regTurno(matrizTurnos)
    if opcion == 4:
        registro_p.main()
    else:
        pass
        # le sigue el resto de opciones
    clear()
    opcion = menu.consulta_opcion()