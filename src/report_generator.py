import xlsxwriter
from typing import List, Dict

class ReportStyles:
    """
    Contiene los estilos usados dentro del reporte Excel.
    No tiene lógica, solo valores constantes.
    """
    BORDER_COLOR = "black"

    BASE = {
        "text_wrap": True,
        "border": 1,
        "border_color": BORDER_COLOR
    }

    EQUAL = {
        "bg_color": "#98FB98",
        "text_wrap": True,
        "border": 1,
        "border_color": BORDER_COLOR
    }

    DIFF = {
        "bg_color": "#F0F8FF",
        "text_wrap": True,
        "border": 1,
        "border_color": BORDER_COLOR
    }

    NEW = {
        "bg_color": "#FFFACD",
        "text_wrap": True,
        "border": 1,
        "border_color": BORDER_COLOR
    }


class ReportConfig:
    """
    Constantes generales de configuración para el reporte.
    """
    HEADERS = ["Nombre", "Estado", "Modificación"]

    COLUMN_WIDTHS = {
        "A": 30,
        "B": 20,
        "C": 100
    }


class ReportGenerator:
    """
    Genera un archivo Excel basado en configuraciones externas y estilos.
    """

    def __init__(self, filename: str = "comparacion.xlsx"):
        self.filename = filename
        self.workbook = xlsxwriter.Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()

        # Crear formatos desde estilos externos
        self.cell_base = self.workbook.add_format(ReportStyles.BASE)
        self.format_equal = self.workbook.add_format(ReportStyles.EQUAL)
        self.format_diff = self.workbook.add_format(ReportStyles.DIFF)
        self.format_new = self.workbook.add_format(ReportStyles.NEW)

    def set_headers(self, headers: List[str]) -> None:
        for col, header in enumerate(headers):
            self.worksheet.write(0, col, header, self.cell_base)

        for col_letter, width in ReportConfig.COLUMN_WIDTHS.items():
            self.worksheet.set_column(f"{col_letter}:{col_letter}", width)

    def add_rows(self, data: List[Dict]) -> None:
        for row, item in enumerate(data, 1):
            modification = item.get("modificacion", "")

            if modification == "Iguales":
                fmt = self.format_equal
            elif modification in ("---", "Diferentes tamaños"):
                fmt = self.format_diff
            else:
                fmt = self.format_new

            self.worksheet.write(row, 0, item["nombre"], fmt)
            self.worksheet.write(row, 1, item["estado"], fmt)
            self.worksheet.write(row, 2, modification, fmt)

    def close(self) -> None:
        self.workbook.close()

    def generate(self, data: List[Dict]) -> None:
        self.set_headers(ReportConfig.HEADERS)
        self.add_rows(data)
        self.close()