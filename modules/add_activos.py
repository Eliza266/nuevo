from modules.core_files import read_file, update_file, clear_screen, pause_screen
def agregar_activos():
    inventario = read_file('inventario.json')

    data=[]
    from csv import reader
    with open("data/activos2.csv","r") as file:
        lector=reader(file)
        for row in lector:
            data.append(row[0].split(';'))
    activos = {}
    nombres_campos = ["cod_campus", "cod_transaccion", "nro_formulario", "nro_serial", "name_activo",
                    "ubicacion_activo", "marca", "categoria", "estado", "proveedor", "valor", "empresa_resp",
                    "tipo"]
    for sublista in data:
        llave = sublista[0]
        valores = {}
        for nombre_campo, valor in zip(nombres_campos, sublista[0:]):
            valores[nombre_campo] = valor
        valores['historial'] = {}
        activos[llave] = valores
    inventario.get('activos').update(activos)
    update_file('inventario.json', inventario)

def verifyData():
    inventario = read_file('inventario.json')
    if len(inventario["activos"])==0:
        agregar_activos()
    else:
        pass
    
