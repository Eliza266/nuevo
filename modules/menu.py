from tabulate import tabulate
from modules.activos_module import add_activos
from modules.personas_module import add_personas
from modules.zonas_module import add_zonas
from modules.asignacion_module import add_asignacion
from modules.reports_module import report_all_actives, report_list_category, report_list_activ_asig, report_baja_daños ,report_list_historial
from modules.movimientos_module import movimiento
from modules.core_files import read_file, update_file, edit_file_apz, delete_data_apz, search_data_apza, pause_screen, clear_screen


def create_menu():
    clear_screen()
    title = """
++++++++++++++++++++++++++++++++++++
+       SISTEMA DE G & C DE        +
++++++++++++++++++++++++++++++++++++
"""

    # 1. ACTIVOS #¿ Jose
    # 2. PERSONAL #¿ Jose
    # 3. ZONAS #- Eliza
    # 4. ASIGNACIÓN DE ACTIVOS #- Eliza
    # 5. REPORTES #¡ Danna
    # 6. MOVIMIENTOS DE ACTIVOS #¿ Jose
    # 7. SALIR #¿ Jose

    clear_screen()
    print(title)

    opts = (['1', 'ACTIVOS'], ['2', 'PERSONAL'], ['3', 'ZONAS'], ['4', 'ASIGNACIÓN DE ACTIVOS'], [
            '5', 'REPORTES'], ['6', 'MOVIMIENTO DE ACTIVOS'], ['7', 'SALIR'])
    print(tabulate(opts, tablefmt='grid'))

    options = ['1', '2', '3', '4', '5', '6', '7']

    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu()
    else:
        if opt == '1':
            nombre = 'ACTIVOS'
            create_menu_apz(nombre)
            create_menu()
        elif opt == '2':
            nombre = 'PERSONAL'
            create_menu_apz(nombre)
            create_menu()
        elif opt == '3':
            nombre = 'ZONAS'
            create_menu_apz(nombre)
            create_menu()
        elif opt == '4':
            create_menu_asignar()
            create_menu()
        elif opt == '5':
            create_menu_reportes()
            create_menu()
        elif opt == '6':
            create_menu_movimientos()
            create_menu()
        elif opt == '7':
            return


def create_menu_apz(nombre: str):
    clear_screen()
    title = f"""
    ++++++++++++++++++++++++++++
    +       MENÚ {nombre}       +
    ++++++++++++++++++++++++++++
    """
    options = ['1', '2', '3', '4', '5']

    print(title)

    opts = (['1', 'AGREGAR'], ['2', 'EDITAR'], ['3', 'ELIMINAR'],
            ['4', 'BUSCAR'], ['5', 'REGRESAR AL MENÚ PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')

    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu_apz(nombre)
    else:
        clear_screen()
        if opt == '1':
            if nombre == 'ACTIVOS':
                add_activos()
                create_menu_apz(nombre)
            elif nombre == 'PERSONAL':
                add_personas()
                create_menu_apz(nombre)
            elif nombre == 'ZONAS':
                add_zonas()
                create_menu_apz(nombre)

        elif opt == '2':
            if nombre == 'ACTIVOS':
                edit_file_apz(nombre)
                create_menu_apz(nombre)
            elif nombre == 'PERSONAL':
                edit_file_apz(nombre)
                create_menu_apz(nombre)
            elif nombre == 'ZONAS':
                edit_file_apz(nombre)
                create_menu_apz(nombre)

        elif opt == '3':
            if nombre == 'ACTIVOS':
                delete_data_apz(nombre)
                create_menu_apz(nombre)
            elif nombre == 'PERSONAL':
                delete_data_apz(nombre)
                create_menu_apz(nombre)
            elif nombre == 'ZONAS':
                delete_data_apz(nombre)
                create_menu_apz(nombre)

        elif opt == '4':
            if nombre == 'ACTIVOS':
                search_data_apza(nombre)
                create_menu_apz(nombre)
            elif nombre == 'PERSONAL':
                search_data_apza(nombre)
                create_menu_apz(nombre)
            elif nombre == 'ZONAS':
                search_data_apza(nombre)
                create_menu_apz(nombre)

        elif opt == '5':
            pass
    return True


def create_menu_asignar():
    clear_screen()
    title = f"""
    ++++++++++++++++++++++++++++
    +       MENÚ ASIGNACIÓN    +
    ++++++++++++++++++++++++++++
    """
    options = ['1', '2', '3']

    print(title)

    opts = (['1', 'CREAR ASIGNACION'], ['2', 'BUSCAR'],
            ['3', 'REGRESAR AL MENÚ PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu_asignar()
    else:

        if opt == '1':
            add_asignacion()
        elif opt == '2':
            nombre = 'ASIGNACIONES'
            search_data_apza(nombre)
        elif opt == '3':
            create_menu()


def create_menu_reportes():
    clear_screen()
    title = f"""
    ++++++++++++++++++++++++++
    +       MENÚ REPORTES    +
    ++++++++++++++++++++++++++
    """
    options = ['1', '2', '3', '4', '5','6']

    print(title)

    opts = (['1', 'LISTAR TODOS LOS ACTIVOS'], ['2', 'LISTAR ACTIVOS POR CATEGORIA'],
            ['3', 'LISTAR ACTIVOS DADOS DE BAJA POR DAÑO'], ['4', 'LISTAR ACTIVOS Y ASIGNACION'],
            ['5', 'LISTAR HISTORIAL DE MOVIMIENTO DE ACTIVO'],['6', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')

    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
        create_menu_reportes()
    else:

        if opt == '1':
            report_all_actives()
            create_menu_reportes()

        if opt == '2':
            report_list_category()
            create_menu_reportes()

        if opt == '3':
            report_baja_daños()
            create_menu_reportes()

        if opt == '4':
            report_list_activ_asig()
            create_menu_reportes()

        if opt == '5':
            report_list_historial()
            create_menu_reportes()
        
        if opt == '6':
            return


def create_menu_movimientos():
    clear_screen()
    title = f"""
    +++++++++++++++++++++++++++++++
    +       MENÚ MOVIMIENTOS      +
    +++++++++++++++++++++++++++++++
    """
    options = ['1', '2', '3', '4', '5']

    print(title)

    opts = (['1', 'RETORNAR ACTIVO'], ['2', 'DAR DE BAJA ACTIVO'],
            ['3', 'REASIGNAR ACTIVO'], ['4', 'ENVIAR A GARANTÍA'], ['5', 'REGRESAR AL MENU PRINCIPAL'])
    print(tabulate(opts, tablefmt='grid'))

    opt = input('Ingrese la opción:\n-> ')
    if opt not in options:
        clear_screen()
        print(f'La opción ({opt}) ingresada no es valida')
        pause_screen()
        clear_screen()
    else:
        if opt == '1':
            action = 'retorno'
            movimiento(action)
            create_menu_movimientos()
        elif opt == '2':
            action = 'baja'
            movimiento(action)
            create_menu_movimientos()
        elif opt == '3':
            action = 're'
            movimiento(action)
            create_menu_movimientos()
        elif opt == '4':
            action = 'gar'
            movimiento(action)
            create_menu_movimientos()
        elif opt == '5':
            return
