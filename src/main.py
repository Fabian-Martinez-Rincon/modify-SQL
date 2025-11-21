import os
from dotenv import load_dotenv

from src.comparator_service import FileComparatorService
from src.report_generator import ReportGenerator

def main():
    """Punto de entrada del proyecto."""

    load_dotenv()

    old_path = os.getenv('PATH_OLD_FILE')
    new_path = os.getenv('PATH_NEW_FILE')

    if old_path is None or new_path is None:
        raise ValueError("PATH_OLD_FILE o PATH_NEW_FILE no están definidos en .env")

    comparator = FileComparatorService(old_path, new_path)
    results = comparator.compare()

    report = ReportGenerator("comparacion.xlsx")
    report.generate(results)

if __name__ == "__main__":
    main()
