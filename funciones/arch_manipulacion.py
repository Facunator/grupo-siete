def existe_fichero(arch, dato):
    # busca por cada línea un dato, si existe retorna True, sino False
    encontrado = False
    with open(arch, 'r') as fichero:
        linea = fichero.readline()
        while linea != '' and encontrado != True:
            if dato in linea:
                encontrado = True
            linea = fichero.readline()
    return encontrado

def escribir_fichero(arch, dato, tipo):
    # sobre-escribe un fichero o agrega contenido, depende el tipo especificado
    with open(arch, tipo) as fichero:
        fichero.write(dato + '\n')