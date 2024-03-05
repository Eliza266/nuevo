from modules.core_files import read_file, update_file, clear_screen, pause_screen

def add_personas():

    clear_screen()

    inventario = read_file('inventario.json')


    id = input('Ingrese id/cc de la persona\n-> ') 

    if id in inventario.get('activos'):
        print('El id/cc que tratas de ingresar ya existe')
        pause_screen()
    else:

        clear_screen()
        opt = input('Elija si es persona natural: "1", o persona jurídica: "2"\n-> ')
        if opt == "1":
            tipo = 'Natural'
        elif opt == "2":
            tipo = "Juridica"
        else:
            print(f'La opción "{opt}" no es valida solo se acepta 1 ó 2')
            pause_screen()
            add_personas()
        clear_screen()
        name = input('Ingrese nombre del empleado\n-> ')
        clear_screen()
        email = input(f'Ingrese el email de {name}\n-> ')
        clear_screen()

        if input('Tiene teléfono móvil? Si(s) / No(Enter) \n-> ').lower() == 's':
            tel_movil = input(f'Ingrese teléfono móvil de {name}\n-> ')
            if tel_movil.isdigit():
                print("Teléfono móvil válido.")
            
            else:
                print("Por favor, ingrese solo números para el teléfono móvil.")
                tel_movil = 'No aplica'
                pause_screen()
                clear_screen()
        else:
            tel_movil = 'No aplica'


       
        if input('Tiene teléfono en casa? Si(s) / No(Enter) \n-> ').lower() == 's':
            tel_casa = input(f'Ingrese número del teléfono de casa para {name}\n-> ')
            if tel_movil.isdigit():
                print("Teléfono móvil válido.")
            else:
                print("Por favor, ingrese solo números para el teléfono casa.")
                tel_movil = 'No aplica'
                pause_screen()
                clear_screen()
        else: 
            tel_casa = 'No aplica'

        if input('Tiene teléfono personal? Si(s) / No(Enter) \n-> ').lower() == 's':
            tel_personal = input(f'Ingrese teléfono personal de {name}\n-> ')
            if tel_movil.isdigit():
                print("Teléfono móvil válido.")
            else:
                print("Por favor, ingrese solo números para el teléfono personal.")
                tel_movil = 'No aplica'
                pause_screen()
                clear_screen()
        else: 
            tel_personal = 'No aplica'

        if input('Tiene teléfono de oficina? Si(s) / No(Enter) \n-> ').lower() == 's':
            tel_oficina = input(f'Ingrese teléfono de oficina de {name}\n-> ')
            if tel_movil.isdigit():
                print("Teléfono móvil válido.")
            else:
                print("Por favor, ingrese solo números para el teléfono oficina.")
                tel_movil = 'No aplica'
                pause_screen()
                clear_screen()
        else: 
            tel_oficina = 'No aplica'

        persona = {
            'id': id,
            'tipo': tipo,
            'name': name,
            'email': email,
            'telefonos': {
                'tel_movil': tel_movil,
                'tel_casa': tel_casa,
                'tel_personal': tel_personal,
                'tel_oficina': tel_oficina
                }
            }

        inventario.get('personal').update({id:persona})
        update_file('inventario.json', inventario)
        return