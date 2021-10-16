from funciones.arch_manipulacion import escribir_fichero, existe_fichero
from funciones.validaciones import validacion_dni, validacion_menores, validacion_nombre
from time import sleep
def main():
    titulo = '''

██████╗░███████╗░██████╗░██╗░██████╗████████╗██████╗░░█████╗░    ██████╗░███████╗
██╔══██╗██╔════╝██╔════╝░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗    ██╔══██╗██╔════╝
██████╔╝█████╗░░██║░░██╗░██║╚█████╗░░░░██║░░░██████╔╝██║░░██║    ██║░░██║█████╗░░
██╔══██╗██╔══╝░░██║░░╚██╗██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║    ██║░░██║██╔══╝░░
██║░░██║███████╗╚██████╔╝██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝    ██████╔╝███████╗
╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░    ╚═════╝░╚══════╝

██████╗░░█████╗░░█████╗░██╗███████╗███╗░░██╗████████╗███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔════╝
██████╔╝███████║██║░░╚═╝██║█████╗░░██╔██╗██║░░░██║░░░█████╗░░╚█████╗░
██╔═══╝░██╔══██║██║░░██╗██║██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██║███████╗██║░╚███║░░░██║░░░███████╗██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░                     
    '''
    print(titulo)
    registrar = 'yes'
    while registrar == 'yes':
        nombre = input('Ingrese el nombre del paciente: ')
        while not validacion_nombre(nombre):
            nombre = input('Re-ingrese el nombre del paciente: ')
        msj = 'Ingrese la edad del paciente: '
        while True:
            try:
                edad = int(input(msj))
                break
            except ValueError:
                print('ERROR. La edad debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
                msj = 'Re-ingrese la edad del paciente: '    
        if not validacion_menores(edad):
            print('La clínica no acepta pacientes menores de edad. Anulando el alta.\n')         
        else:
            msj = 'Ingrese el DNI del paciente: '
            while True:
                try:
                    dni = int(input(msj))
                    if not validacion_dni(dni):
                        msj = 'Re-ingrese el DNI del paciente: '
                        continue
                    break
                except ValueError:
                    print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
                    msj = 'Re-ingrese el DNI del paciente: '
            try:
                if not existe_fichero('datos/pacientes.txt', str(dni)):
                    escribir_fichero('datos/pacientes.txt', f'{dni};{nombre.capitalize()};{edad}', 'a')
                    print()
                    print('El paciente ha sido registrado con éxito.')
                else:
                    print('Ya se encuentra registrado un paciente con dicho DNI. Anulando el alta.') 
            except FileNotFoundError:
                print('ERROR. El registro de pacientes no fue encontrado en el directorio actual.')
                sleep(3)
                break       
        registrar= input('¿Desea registrar a otro paciente? (yes, no): ')