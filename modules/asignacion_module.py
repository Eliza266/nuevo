from modules.core_files import read_file, update_file, clear_screen, pause_screen

def history(fecha:str, tipo:str, code_act:str, text:str, re=False):

    inventario = read_file('inventario.json')


    if tipo == 'baja':
        tipo = '2'
    elif tipo == 'gar':
        tipo = '3'

    historial = {
        'id': len(inventario.get('activos').get(code_act).get('historial'))+1,
        'fecha': fecha,
        'tipo': tipo,
        'id_resp': text
    }

    inventario.get('activos').get(code_act).get('historial').update({historial['id']:historial})
    return inventario

# valida el tipo de asignaciones
def val_tipo_asignacion():
    print('Ingrese el tipo de asignación que desea registrar: ')
    print('1. Personal \n2. Zona')
    opt = input('-')
    if opt == '1':
        tipo_asignacion = 'Personal'
    elif opt == '2':
        tipo_asignacion = 'zona'
    else:
        print('Opción Incorrecta')
        pause_screen()
        clear_screen()
        tipo_asignacion = val_tipo_asignacion()
    return tipo_asignacion

def validar_id(code='', check=False):
    inventario = read_file('inventario.json')
    asignados = []
    id_persona = input('Ingrese el Id de la persona: ')
    if id_persona in inventario['personal']:
        nombre = inventario.get('personal').get(id_persona).get('name')
        print(nombre)
        activo = validar_activo(asignados, code, check)

        if check == False:
            op = True
        elif check == True:
            op = False
            asignados.append(activo)
        while op:
            list_opciones = ['s','n']                
            opcion = input('Desea agregar otro activo? s(Si) n(No)').lower()
            if opcion in list_opciones:
                if opcion == 's':
                        asignados.append(activo)
                        activo = validar_activo(asignados, code, check)
                elif opcion == 'n':
                        asignados.append(activo)
                        op = False
            else: 
                print('Opcion Incorrecta')
                pause_screen()
                clear_screen()
        return id_persona, asignados
    else:
        print('El Id no se encuentra registrado')
        pause_screen()
        clear_screen()
        validar_id()

def validar_zona_asignada(code='', check=False):
    inventario = read_file('inventario.json')
    opcion_zona = input('Ingrese el número de la zona: ')
    opcion_zona = str(opcion_zona).zfill(3)
    opcion_zona = 'z' + opcion_zona
    asignados = []
    
    
    if opcion_zona in inventario['zonas']:
        capacidad = inventario['zonas'][opcion_zona]['capacidad_zona']
        def validar_capacidad(code='', check=False): 
            global activo
            activo = validar_activo(asignados, code, check)
            if (activo[:3] == 'cpu') and (inventario['zonas'][opcion_zona]['ex_cpu']) == capacidad:
                print(f'Lo sentimos, la Capacidad de la zona {opcion_zona} para CPU se encuentra llena')
                validar_capacidad(code, check)
            else:
                if activo[:3] == 'mou' and (inventario['zonas'][opcion_zona]['ex_mou']) == capacidad:
                    print(f'Lo sentimos, la Capacidad de la zona{opcion_zona} para Mouse se encuentra llena')
                    validar_capacidad(code, check)
                else:
                    if activo[:3] == 'mon' and (inventario['zonas'][opcion_zona]['ex_mon']) == capacidad:
                        print(f'Lo sentimos, la Capacidad de la zona{opcion_zona} para Monitores se encuentra llena')
                        validar_capacidad(code, check)
                    else:
                        if activo[:3] == 'tec' and (inventario['zonas'][opcion_zona]['ex_tec']) == capacidad:
                            print(f'Lo sentimos, la Capacidad de la zona{opcion_zona} para teclados se encuentra llena')
                            validar_capacidad(code, check)
        validar_capacidad(code, check)
        global activo 
        if check == False:
            op = True
        elif check == True:
            op = False
            asignados.append(activo)
        while op:
            list_opciones = ['s','n']                
            opcion = input('Desea ingresar otro activo? s(Si) n(No)').lower()
            if opcion in list_opciones:
                if opcion == 's':
                        asignados.append(activo)
                        validar_capacidad()
                else: 
                    if opcion == 'n':
                        asignados.append(activo)
                        op = False
            else: 
                print('Opcion Incorrecta')
                pause_screen()
                clear_screen()
        return opcion_zona, asignados
    else:
        print('Opción Incorrecta, Rectifique el número de zona')
        pause_screen()
        clear_screen()
        return validar_zona_asignada()

def validar_activo(asignados:list, code='', check=False):
    inventario = read_file('inventario.json')
    if check == True:
        cod_campus = code
    elif check == False:
        cod_campus = input('Ingrese el "Código Campus" del activo: ')

    if cod_campus not in asignados:
        if cod_campus not in inventario['activos']:
            print('El código ingresado no corresponde a ningún activo')
            pause_screen()
            clear_screen()
            return validar_activo(asignados, code, check)
        else:
            estado = inventario['activos'][cod_campus]['estado']
            if estado == '0':
                    return cod_campus
            else:
                if estado == '1':
                    print('El activo ya se encuentra "Asignado"')
                    pause_screen()
                    clear_screen()
                    return validar_activo(asignados, code, check)
                elif estado == '2':
                    print('El activo se encuentra "Dado de Baja"')
                    pause_screen()
                    clear_screen()
                    return validar_activo(asignados, code, check)
                elif estado == '3':
                    print('El activo se encuentra "En Reparacion y/o Garantía"')
                    pause_screen()
                    clear_screen()
                    return validar_activo(asignados, code, check)
    else:
        print('El activo ya se encuentra asignado')
        return validar_activo(asignados, code, check)

def add_asignacion(code='', check=False):
    inventario = read_file('inventario.json')
    if check == True:
        fecha_asignacion = str(input('Ingrese la Fecha de la reasignación: '))
        tipo = '4'
    elif check == False:
        fecha_asignacion = str(input('Ingrese la Fecha de la asignación: '))
        tipo = '1'
    tipo_asignacion = val_tipo_asignacion()
    if tipo_asignacion == 'Personal':
        id_personas, asignados = validar_id(code, check)
        id = id_personas
        nombre = inventario['personal'][id]['name']
    else:
        opcion_zona, asignados = validar_zona_asignada(code, check)
        id = opcion_zona
        nombre = inventario['zonas'][id]['nombre_zona']
        for i in range(len(asignados)):
            if asignados[i][:3] == 'cpu':
                inventario['zonas'][id]['ex_cpu'] += 1
            else:
                if asignados[i][:3] == 'mon':
                    inventario['zonas'][id]['ex_mon'] += 1
                else:
                    if asignados[i][:3] == 'mou':
                        inventario['zonas'][id]['ex_mou'] += 1
                    else: 
                        if asignados[i][:3] == 'tec':
                            inventario['zonas'][id]['ex_tec'] += 1
    for i in asignados:
        inventario['activos'][i]['estado'] = '1'
        inventario['activos'][i]['ubicacion_activo'] = id

    if id in inventario['asignaciones']:
        inventario['asignaciones'][id]['activos_asignados'].extend(asignados)
    else:
        asignacion = {
            'fecha_asignacion': fecha_asignacion,
            'tipo_asignacion ': tipo_asignacion,
            'asignado_a': id,
            'activos_asignados': asignados
        }
        inventario.get('asignaciones').update({id:asignacion})
    update_file('inventario.json', inventario)

    for idx in range(len(asignados)):
        inventario = history(fecha_asignacion, tipo, asignados[idx], id)
        update_file('inventario.json', inventario)
    del_asig_vacias()

def del_asig_vacias() :
    inventario = read_file('inventario.json')
    claves_a_eliminar = []
    for clave, asignacion in inventario['asignaciones'].items():
        if not asignacion['activos_asignados']:
            claves_a_eliminar.append(clave)
    for clave in claves_a_eliminar:
        del inventario['asignaciones'][clave]
    update_file('inventario.json', inventario)


