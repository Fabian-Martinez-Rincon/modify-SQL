import os
import difflib
from typing import List, Dict, Optional


class FileComparator:
    """
    Clase encargada de comparar archivos de texto utilizando diferentes estrategias.
    
    Métodos:
    --------
    compare(file1: str, file2: str) -> str
        Punto de entrada principal. Compara ambos archivos y devuelve el resultado.
    
    _compare_with_difflib(file1: str, file2: str) -> str
        Realiza una comparación detallada usando difflib y muestra solo las diferencias.
    
    _validate_paths(file1: str, file2: str) -> Optional[str]
        Valida que ambos archivos existan y retorna un mensaje si alguno no existe.
    """

    def compare(self, file1: str, file2: str) -> str:
        """
        Compara dos archivos usando validaciones y difflib si es necesario.

        file1 : str
            Ruta absoluta del archivo original.
        file2 : str
            Ruta absoluta del archivo nuevo.
        "Iguales", "No existe", "Diferentes tamaños" o el diff generado.
        """
        validation_msg = self._validate_paths(file1, file2)
        if validation_msg:
            return validation_msg

        if os.path.getsize(file1) != os.path.getsize(file2):
            return self._compare_with_difflib(file1, file2)

        with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
            if f1.read() == f2.read():
                return "Iguales"

        return self._compare_with_difflib(file1, file2)

    def _validate_paths(self, file1: str, file2: str) -> Optional[str]:
        """
        Verifica que ambos archivos existan.
        Optional[str]
            Devuelve un mensaje de error si algún archivo no existe.
            Devuelve None si ambos son válidos.
        """
        if not os.path.exists(file1) or not os.path.exists(file2):
            return "No existe"
        return None

    def _compare_with_difflib(self, file1: str, file2: str) -> str:
        """
        Compara dos archivos mostrando solo las diferencias.

        Devuelve:
        - Líneas eliminadas (prefijo "- ")
        - Líneas agregadas (prefijo "+ ")
        """

        with open(file1, 'r', encoding="utf-8") as f1, open(file2, 'r', encoding="utf-8") as f2:
            old_text = f1.readlines()
            new_text = f2.readlines()

        differ = difflib.Differ()
        diff = differ.compare(old_text, new_text)

        filtered = list()
        for line in diff:
            line = line.strip()
            if line.startswith("- ") or line.startswith("+ "):
                filtered.append(line)

        if filtered:
            return "\n".join(filtered)
        return "Diferencias menores (sin cambios visibles)"


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
