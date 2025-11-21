import os
import subprocess
import venv


class VirtualEnvManager:
    """
    Clase encargada de gestionar un entorno virtual, instalar dependencias
    y ejecutar comandos dentro del venv.

    Parámetros
    ----------
    venv_dir : str
        Carpeta donde se creará el entorno virtual.
    requirements_file : str
        Ruta del archivo requirements.txt.
    """

    def __init__(self, venv_dir: str = "venv", requirements_file: str = "requirements.txt"):
        self.venv_dir = venv_dir
        self.requirements_file = requirements_file

    @property
    def python_executable(self) -> str:
        """Devuelve la ruta del Python dentro del entorno virtual."""
        if os.name == "nt":
            return os.path.join(self.venv_dir, "Scripts", "python.exe")
        return os.path.join(self.venv_dir, "bin", "python")


    def create(self) -> None:
        """Crea el entorno virtual si no existe."""
        if os.path.isdir(self.venv_dir):
            print(f"Entorno virtual '{self.venv_dir}' ya existe")
            return

        print(f"Creando entorno virtual en '{self.venv_dir}'...")
        builder = venv.EnvBuilder(with_pip=True)
        builder.create(self.venv_dir)
        print("Entorno virtual creado")


    def install_dependencies(self) -> None:
        """Instala dependencias dentro del entorno virtual."""
        print("Instalando dependencias...")
        subprocess.check_call([self.python_executable, "-m", "pip", "install", "-r", self.requirements_file])
        print("Dependencias instaladas")

    # --------------------------
    #  Ejecutar comandos dentro del venv
    # --------------------------
    def run_module(self, module_name: str) -> None:
        """Ejecuta un módulo Python dentro del entorno virtual."""
        print(f"Ejecutando módulo: {module_name}")
        subprocess.check_call([self.python_executable, "-m", module_name])


