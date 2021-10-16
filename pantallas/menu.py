from time import sleep
import os; clear = lambda: os.system('cls')

def menu_grafico():
    menu = '''
                                            1. Registrar turno
                                            2. Modificar turno
                                            3. Eliminar turno
                                            4. Registrar paciente
                                            5. Modificar paciente
                                            6. Eliminar paciente
                                            7. Listar pacientes
                                            8. Listar turnos
                                            9. Buscar turno
                                            0. Salir
    '''
    titulo = f'''

                              ░█████╗░██╗░░░░░██╗███╗░░██╗██╗░█████╗░░█████╗░
                              ██╔══██╗██║░░░░░██║████╗░██║██║██╔══██╗██╔══██╗
                              ██║░░╚═╝██║░░░░░██║██╔██╗██║██║██║░░╚═╝███████║
                              ██║░░██╗██║░░░░░██║██║╚████║██║██║░░██╗██╔══██║
                              ╚█████╔╝███████╗██║██║░╚███║██║╚█████╔╝██║░░██║
                              ░╚════╝░╚══════╝╚═╝╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░░╚═╝
    '''
    print(titulo + '\n' + menu)

def consulta_opcion():
    # consulta la opción del usuario, en caso de errores vuelve a consultar
    while True:
        menu_grafico()
        try:
            opcion = int(input('¿Qué desea hacer?: '.rjust(60)))
            assert opcion < 9 and opcion > -1
            break
        except:
            print('Por favor elija una opción válida.'.rjust(70))
            sleep(2)
            clear()
    return opcion
        





