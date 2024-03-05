from modules.core_files import read_file, pause_screen, update_file
from modules.asignacion_module import add_asignacion, history    

def movimiento(action):

    if action == 'retorno':
        msg = 'Ingrese el "Código Campus" del activo que quiere retornar\n-> '
        state = '0'
    elif action == 'baja':
        msg = 'Ingrese el "Código Campus" del activo que quiere dar de baja\n-> '
        state = '2'
    elif action == 're':
        msg = 'Ingrese el "Código Campus" del activo que quiere reasignar\n-> '
        state = '1'
    elif action == 'gar':
        msg = 'Ingrese el "Código Campus" del activo que quiere enviar a garantía\n-> '
        state = '3'
    else:
        print('Ninguna opcion es valida')
        pause_screen()
        return

    inventario = read_file('inventario.json')

    if action != 're':
        text = 'No aplica'
        fecha_movimiento = input('Ingrese la fecha del movimiento\n-> ')

    act_return = input(msg)

    if act_return not in inventario.get('activos'):
        print('El activo ingresado no existe')
        pause_screen()
        movimiento(action)
    else:
        estado = inventario.get('activos').get(act_return).get('estado')

        if action == 'baja':
            if estado == '2':
                print('El activo no se puede dar de baja, porque ya esta "Dado de baja"')
                pause_screen()
                return
            elif estado == '3':
                print('El activo no se puede dar de baja, porque esta "En reparación / garantía"')
                pause_screen()
                return
        elif action == 'gar':
            if estado == '3':
                print('El activo no se puede enviar a garantía porque ya esta "En reparación"')
                pause_screen()
                return
            elif estado == '2':
                print('El activo no se puede enviar a garantía porque esta dado de baja"')
                pause_screen()
                return
        elif action == 're':
            if estado != '1':
                print('El activo no se puede reasignar, el estado debe ser "Asignado (1)"')
                pause_screen()
                return


        if estado is None:
            print('Aun no hay un estado asignado')
            pause_screen()
            movimiento(action)
        else:
            if estado != '0':

                if action != 're':
                    inventario = history(fecha_movimiento, action, act_return, text)
                    print('Movimiento realizado con éxito')
                    pause_screen()

                inventario['activos'][act_return]['estado'] = state
                update_file('inventario.json', inventario)
                if estado == '1':

                    ubicacion = input('Ingrese el "ID" / "Número Zona" de la persona / zona en la cual se encuentra asignado el activo\n-> ')
                    if ubicacion not in inventario.get('asignaciones'):
                        print('La ubicacion ingresada no existe')
                        pause_screen()
                        movimiento(action)
                    else:
                        inv = inventario['asignaciones'][ubicacion]['activos_asignados']
                        if len(inv) == 0:
                            print('Aun no hay datos asignados')
                            pause_screen()
                            movimiento(action)

                        for idx, item in enumerate(inv):
                            if item == act_return:
                                inventario['asignaciones'][ubicacion]['activos_asignados'].pop(idx)
                                if action == 're':
                                    inventario['activos'][act_return]['estado'] = '0'
                                    inventario['activos'][act_return]['ubicacion_activo'] = 'no_asignada'
                                    update_file('inventario.json', inventario)
                                    add_asignacion(act_return, True)
