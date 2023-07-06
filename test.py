import argparse, sys, subprocess, unittest, os

os.environ.setdefault('DJANGO_SETTINGS_MODUL', 'config.settings.test')

interpreter = 'C:/Users/Santi/OneDrive/Escritorio/python/Gastos/entorno/Scripts/python'

apps = [
    "usuarios",
    "movimientos",
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', help="Use the show the help", action='store_true')
    parser.add_argument('--all', help="Run tests of the all apps", action='store_true')
    parser.add_argument('--migrate', help="Apply the migrations", action='store_true')
    for app in apps:
        parser.add_argument(f'--{app}', help=f"Use to only run test of {app}", action='store_true')
    
    args = parser.parse_args()
    
    if args.help:
        print("USAGE: \n test.py [--help] [--app_name COMMAND]")
        print("")
        print("FILES:")
        print("--app_name \t#Replace app_name with the name of the app you want to test")
        print("--all \t\t#Run test of the all apps")
        print("--migrate \t#Apply migrations")
        print("")
        print("TESTS:")
        print("test.py --usuario --migrate\ntest.py --usuario\ntest.py --all")
        sys.exit()
    
    if args.all:
        # quito los argumentos help y all
        argumentos = args._get_kwargs()
        argumentos.pop(0)
        argumentos.pop(0)
    
    else:
        # obtengo los argumentos ingresados
        argumentos = [(k,v) for k, v in args._get_kwargs() if v]
    
    if argumentos:
        print("\tGenerando base de datos")
        print("-"*50)
        
        if args.migrate:
            print("\tCorriendo migraciones")
            print('-'*50)
            subprocess.run([interpreter, 'manage.py', 'migrate', '--settings=config.settings.test'])
            argumentos.remove(('migrate', True))
        
        # borro datos de la base de datos
        subprocess.call([interpreter, 'manage.py', 'flush', '--no-input', '--settings=config.settings.test'])
        
        for key, value in argumentos:
            module_name = f"apps.{key}.tests"
            try:
                print(f"\tEjecutatndo los tests de {key}")
                print('-'*50)
                
                # importo los tests de la app y los ejecuto
                module = __import__(module_name, fromlist=['Tests'])
                suite = unittest.defaultTestLoader.loadTestsFromModule(module)
                unittest.TextTestRunner().run(suite)
            
            except ImportError:
                print(f"No se pudo importar el modulo {module_name}")
                break
    else:
        print("Debe ingresar uno de los siguientes argumentos:")
        for k, v in args._get_kwargs():
            print(f'--{k}')
