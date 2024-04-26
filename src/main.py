import os
from dotenv import load_dotenv
from file_utils import fileList
from comparator import comparate
from report_generator import generate_report

load_dotenv()

PATH_SOURCE1 = os.getenv('PATH_OLD_FILE')
PATH_SOURCE2 = os.getenv('PATH_NEW_FILE')

check = fileList(PATH_SOURCE1)
new = fileList(PATH_SOURCE2)

result = [
    {
        'nombre': file, 
        'estado': "Existente", 
        'modificacion': comparate(
            os.path.join(PATH_SOURCE1, file), 
            os.path.join(PATH_SOURCE2, file)
            )
    } if file in check else {
        'nombre': file, 
        'estado': "Nueva", 
        'modificacion': "---"
    } for file in new
]

generate_report(result)