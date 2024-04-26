import os

def fileList(directorio):
    try:
        return [nombre_archivo for nombre_archivo in os.listdir(directorio)]
    except FileNotFoundError as fnf_error:
        print(f"Error: No se pudo encontrar el directorio: {directorio}")
        print(fnf_error)
        return []
    except Exception as e:
        print(f"Error general: {e}")
        return []
