import os
import difflib
from typing import Optional


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

        Parameters
        ----------
        file1 : str
            Ruta absoluta del archivo original.
        file2 : str
            Ruta absoluta del archivo nuevo.

        Returns
        -------
        str
            "Iguales", "No existe", "Diferentes tamaños" o el diff generado.
        """
        validation_msg = self._validate_paths(file1, file2)
        if validation_msg:
            return validation_msg

        # Si difieren en tamaño, se comparan con difflib
        if os.path.getsize(file1) != os.path.getsize(file2):
            return self._compare_with_difflib(file1, file2)

        # Si son idénticos en tamaño, hacemos lectura completa
        with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
            if f1.read() == f2.read():
                return "Iguales"

        # Si el contenido difiere, retornamos diff más claro
        return self._compare_with_difflib(file1, file2)

    def _validate_paths(self, file1: str, file2: str) -> Optional[str]:
        """
        Verifica que ambos archivos existan.

        Returns
        -------
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

        Devuelve un bloque de texto con:
        - líneas agregadas (+)
        - líneas eliminadas (-)

        Parameters
        ----------
        file1 : str
            Ruta del archivo viejo.

        file2 : str
            Ruta del archivo nuevo.

        Returns
        -------
        str
            Texto con las diferencias.
        """
        with open(file1, 'r', encoding="utf-8") as f1, open(file2, 'r', encoding="utf-8") as f2:
            old_text = f1.readlines()
            new_text = f2.readlines()

        differ = difflib.Differ()
        diff = differ.compare(old_text, new_text)

        filtered = [
            line.strip()
            for line in diff
            if line.startswith('- ') or line.startswith('+ ')
        ]

        return "\n".join(filtered) if filtered else "Diferencias menores (sin cambios visibles)"
