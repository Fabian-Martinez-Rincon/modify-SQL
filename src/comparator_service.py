import os
from typing import List, Dict
from src.comparator import FileComparator


class FileUtils:
    """
    Utilidades relacionadas con manejo de archivos.
    """

    @staticmethod
    def list_directory(path: str) -> List[str]:
        """
        Retorna la lista de archivos contenidos en un directorio.

        Parameters
        ----------
        path : str
            Ruta del directorio a listar.

        Returns
        -------
        list[str]
            Lista de nombres de archivo dentro del directorio.
        """
        try:
            archivos = list()
            for nombre in os.listdir(path):
                archivos.append(nombre)
            return archivos

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: No se encontró el directorio: {path}")

        except Exception as e:
            raise Exception(f"Error general al leer '{path}': {e}")


class FileComparatorService:
    """
    Servicio encargado de comparar archivos entre dos directorios.
    Aplica SRP: un objeto que encapsula toda la lógica de comparación.
    """

    def __init__(self, old_path: str, new_path: str):
        if not os.path.exists(old_path):
            raise FileNotFoundError(f"Directorio no encontrado: {old_path}")

        if not os.path.exists(new_path):
            raise FileNotFoundError(f"Directorio no encontrado: {new_path}")

        self.old_path = old_path
        self.new_path = new_path

    def compare(self) -> List[Dict]:
        """
        Genera una lista de resultados comparando los archivos
        de ambos directorios.
        """
        comparator = FileComparator()
        fileList = FileUtils.list_directory
        old_files = fileList(self.old_path)
        new_files = fileList(self.new_path)

        results = list()

        for file in new_files:
            if file in old_files:
                modification = comparator.compare(
                    os.path.join(self.old_path, file),
                    os.path.join(self.new_path, file)
                )
                estado = "Existente"
            else:
                modification = "---"
                estado = "Nueva"

            results.append({
                "nombre": file,
                "estado": estado,
                "modificacion": modification
            })

        return results
