import json, sys, os

BASE = 'data/'
global count
count = 0

# PANTALLA


def clear_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")


def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")

# GENERALES


def check_file(archivo: str, data):
    if (not (os.path.isfile(BASE + archivo))):
        with open(BASE + archivo, "w") as bw:
            json.dump(data, bw, indent=4)


def read_file(archivo: str):
    with open(BASE+archivo, 'r') as rf:
        inventario = json.load(rf)
    return inventario


def update_file(archivo, data):
    with open(BASE + archivo, 'w') as fw:
        json.dump(data, fw, indent=4)


def edit_file_apz(nombre):

    if nombre == 'ACTIVOS':
        msg = 'Ingrese el "Código Campus" del activo que va a editar\n-> '
    elif nombre == 'PERSONAL':
        msg = 'Ingrese el "id" de la persona que va a editar\n-> '
    elif nombre == 'ZONAS':
        msg = 'Ingrese el "Número de zona" de la zona que va a editar\n-> '

    inventario = read_file('inventario.json')

    if len(inventario.get(nombre.lower())) == 0:
        print('Aun no hay datos que editar')
        pause_screen()
        return

    palabra = input(msg)

    if nombre.lower() in inventario:
        if palabra in inventario[nombre.lower()]:
            data = inventario[nombre.lower()][palabra]

            for key, value in data.items():
                if key not in ['cod_campus', 'nro_formulario', 'categoria', 'estado', 'id', 'nro_zona', 'ex_cpu', 'ex_mon', 'ex_mou', 'ex_tec', 'ubicacion_activo']:
                    if type(data[key]) == dict:
                        if key == 'historial':
                            return
                        if (type(data[key]) == dict):
                            for key2 in data[key].keys():
                                if input(f'Desea modificar el {key2}? s(si) / Enter(no)\n-> ').lower() == 's':
                                    clear_screen()
                                    data[key][key2] = input(
                                        f'Ingrese el nuevo valor para {key2} :')
                                    clear_screen()
                    else:
                        if input(f'Desea modificar el {key}? s(si) / Enter(no)\n-> ').lower() == 's':
                            clear_screen()
                            data[key] = input(f'Ingrese el nuevo valor para {key}:\n-> ')
                            clear_screen()

            inventario[nombre.lower()][palabra] = data
            update_file('inventario.json', inventario)
            pause_screen()
        else:
            print(f'No existe en {nombre.lower()}: {palabra}')

def delete_data_apz(nombre):
    clear_screen()

    if nombre == 'ACTIVOS':
        msg = 'Ingrese el "Código campus" del activo que va a eliminar\n-> '
    elif nombre == 'PERSONAL':
        msg = 'Ingrese el "id" de la persona que va a eliminar\n-> '
    elif nombre == 'ZONAS':
        msg = 'Ingrese el "Número de zona" de la zona que va a eliminar\n-> '

    inventario = read_file('inventario.json')

    if len(inventario.get(nombre.lower())) == 0:
        print('Aun no hay datos que eliminar')
        pause_screen()
        return

    delete_value = input(msg)

    if delete_value not in inventario[nombre.lower()]:
            global count
            count += 1
            print(f'El dato que ingresó no esta registrado | Intento {count}/3')
            pause_screen()
            if count > 2:
                count = 0
                return
            delete_data_apz(nombre)
    else:
        
        if (nombre == 'ACTIVOS'):
            for key, value in inventario['asignaciones'].items():
                for key2, value2 in value.items():
                    if key2 == 'activos_asignados':
                        for i, item in enumerate(value[key2]):
                            if item == delete_value:
                                print('El activo no se puede eliminar, porque se encuentra asignado')
                                pause_screen()
                                return
                        inventario[nombre.lower()].pop(delete_value)
                        update_file('inventario.json', inventario)
                        return
                            
        if delete_value in inventario.get('asignaciones'):
            lng = len(inventario.get('asignaciones').get(delete_value).get('activos_asignados'))
        else:
            lng = 0

        if (nombre == 'PERSONAL' or nombre == 'ZONAS') and (lng == 0):
            inventario[nombre.lower()].pop(delete_value)
            update_file('inventario.json', inventario)
        else:
            print('No se pudo eliminar pues tiene elementos asignados')
            pause_screen()
            return


def search_data_apza(nombre):

    inventario = read_file('inventario.json')

    if nombre == 'ACTIVOS':
        msg = 'Ingrese el "Código campus" del activo que va a buscar\n-> '
    elif nombre == 'PERSONAL':
        msg = 'Ingrese el "id" de la persona que va a buscar\n-> '
    elif nombre == 'ZONAS':
        msg = 'Ingrese el "Número de zona" de la zona que va a buscar\n-> '
    elif nombre == 'ASIGNACIONES':
        msg = 'Ingrese el "id" / "número de zona" de la persona / zona que desea buscar'

    if len(inventario.get(nombre.lower())) == 0:
        print('Aun no hay datos que buscar')
        pause_screen()
        return

    search_value = input(msg)

    if search_value not in inventario[nombre.lower()]:
        global count
        count += 1
        print(f'El dato que ingresó no esta registrado | Intento {count}/3')
        pause_screen()
        if count > 2:
            count = 0
            return
        search_data_apza(nombre)
    else:
        print('VALORES\n')
        for item, value in (inventario[nombre.lower()][search_value]).items():
            if type(value) == dict:
                print(f'{item}:\n')
                for item2, value2 in value.items():
                    if type(value2) == dict:
                        print(f'    {item2}:\n')
                        for item3, value3 in value2.items():
                            print(f'\t{item3}: {value3}')
                        print('\n')
                    # print(f'{item2}: {value2}\n')
            elif type(value) == list:
                print(f'{item}:\n')
                for item2, value2 in enumerate(value):
                    if item2 == 0:
                        item2 = 'ID: '
                    elif item2 == 1:
                        item2 = 'Nombre: '
                    print(f'\t{item2}{value2}\n')
            else:
                print(f'{item}: {value}\n')
        print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n')
        pause_screen()
