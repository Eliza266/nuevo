from modules.core_files import read_file, clear_screen, pause_screen
import os
from tabulate import tabulate

def report_all_actives():
    inventario = read_file('inventario.json')

    listita = []
    
    for i in inventario['activos'].items():
        codigo = i[0]
        nro_serial = inventario['activos'][i[0]]['nro_serial']
        nombre = inventario['activos'][i[0]]['cod_campus']
        sublist = [codigo,nro_serial,nombre]
        listita.append(sublist)

        if listita:
            print(tabulate(listita,headers = ["CODIGO", "NOMBRE", "NRO SERIAL"], tablefmt = 'fancy_grid'))
            
        else:
            print('No hay activos en la categoría')
            pause_screen()

    if listita:
            pag = 30
            total_pag = (len(listita) - 1) // pag + 1
            for idx in range(total_pag):
                clear_screen()
                data = listita[idx * pag: (idx + 1) * pag ]
                print(tabulate(data, headers = ['CODIGO', 'NOMBRE', 'NRO SERIAL'], tablefmt = 'fancy_grid'))
                print(f'Pagina {idx + 1} de {total_pag}')
                pause_screen()
                clear_screen()

    else:
        print(f'No hay activos registrados')
        pause_screen()
        clear_screen()

    
def report_list_category():
    clear_screen()
    inventario = read_file ('inventario.json')

    listita = []

    category = input('Ingrese el nombre de la categoría que desea ver: ').lower()
    for key, value in inventario.get('activos').items():
        if value.get('categoria', '').lower() == category:
            codigo = key
            nro_serial = value.get('nro_serial', '')
            nombre = value.get('name_activo', '')
            listita.append([codigo, nombre, nro_serial])

# Verificar si se encontraron activos en la categoría especificada
    if listita:
        pag = 30
        total_pag = (len(listita) - 1) // pag + 1
        for idx in range(total_pag):
            clear_screen()
            data = listita[idx * pag: (idx + 1) * pag]
            print(tabulate(data, headers=['CODIGO', 'NOMBRE', 'NRO SERIAL'], tablefmt='fancy_grid'))
            print(f'Pagina {idx + 1} de {total_pag}')
            
    else:
        print('No hay activos en la categoría especificada')

    pause_screen()
    clear_screen()

    
def report_baja_daños():
    clear_screen()
    inventario = read_file('inventario.json')

    listita = []

    for key, value in inventario.get('activos').items():
        for key2, value2 in value.items():
            if key2 == 'estado' and value2 == '2':
                codigo = key
                nombre = value.get('name_activo', '')
                nro_serial = value.get('nro_serial', '')
                listita.append([codigo, nombre, nro_serial])

    if listita:
        pag = 30
        total_pag = (len(listita) - 1) // pag + 1
        for idx in range(total_pag):
            clear_screen()
            data = listita[idx * pag: (idx + 1) * pag]
            print(tabulate(data, headers=['CODIGO', 'NOMBRE', 'NRO SERIAL'], tablefmt='fancy_grid'))
            print(f'Pagina {idx + 1} de {total_pag}')

    else:
        print('No hay activos dados de baja')

    pause_screen()
    clear_screen()


def report_list_activ_asig():
    clear_screen()
    inventario = read_file('inventario.json')

    listita = []

    for key, value in inventario.get('asignaciones').items():
        sublist = [key]
        for key2, value2 in value.items():
            if isinstance(value2, dict):
                for key3, value3 in value2.items():
                    sublist.append(f'{value3}')
            else:
                sublist.append(f'{value2}')
        listita.append(sublist)

    if listita:
        pag = 30
        total_pag = (len(listita) - 1) // pag + 1
        for idx in range(total_pag):
            clear_screen()
            data = listita[idx * pag: (idx + 1) * pag]
            print(tabulate(data, headers=['ID','FECHA','TIPO','Asignación','Detalle'], tablefmt='fancy_grid'))
            print(f'Pagina {idx + 1} de {total_pag}')
            
    else:
        print('No hay asignaciones disponibles')

    pause_screen()
    clear_screen()
def report_list_historial():
    inventario = read_file('inventario.json')
    cod_activo=input('Ingrese el codigo del activo que desea ver el historial: ')
    historial= inventario['activos'][cod_activo]['historial']
    for key, value in historial.items():
        print(f'{key}: ')
        for key2, value2 in value.items():
            print(f"   {key2}: {value2}")

        
    pause_screen()
    clear_screen()

