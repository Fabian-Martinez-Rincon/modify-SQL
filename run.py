from env_manager import VirtualEnvManager

def main():
    manager = VirtualEnvManager(venv_dir="venv", requirements_file="requirements.txt")
    manager.create() # 1) Crear venv si no existe
    manager.install_dependencies() # 2) Instalar dependencias si es necesario
    manager.run_module("src.main") # 3) Ejecutar tu aplicación principal


if __name__ == "__main__":
    main()
