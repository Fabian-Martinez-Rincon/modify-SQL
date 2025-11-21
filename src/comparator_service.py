import os
from typing import List, Dict
from src.file_utils import fileList
from src.comparator import FileComparator

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
        old_files = fileList(self.old_path)
        new_files = fileList(self.new_path)

        results = []

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
