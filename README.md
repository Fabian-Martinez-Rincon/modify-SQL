# File Comparator

- [Introducción](#introducción)
- [Características principales](#características-principales)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Flujo general](#flujo-general)
- [Resultado](#resultado-con-los-ejemplos-dados)
- [Documentación por archivo](#-documentación-por-archivo)
---

## Introducción

Este programa compara dos carpetas que contienen archivos SQL y genera un reporte de las diferencias encontradas entre los archivos con el mismo nombre en ambas carpetas.

## Características principales

- Compara archivos SQL en dos directorios especificados.
- Genera un reporte detallado de las diferencias encontradas.
- Fácil de usar y configurar mediante un archivo .env.

---

## Estructura del repositorio

```bash
modify-SQL/
│── run.py
│── env_manager.py
│── requirements.txt
│── .env_example
│── src/
│   ├── comparator_service.py
│   ├── comparator.py
│   ├── report_generator.py
│   ├── report_constants.py
│   ├── file_utils.py
│   └── main.py
```

### Flujo generalExplicar

- `run.py` prepara todo
- `VirtualEnvManager` crea venv y ejecuta
- `src.main` coordina el proceso
- `FileComparatorService` compara archivos
- `ReportGenerator` genera Excel

---

https://github.com/Fabian-Martinez-Rincon/modify-SQL/assets/55964635/169358a1-b7e9-4904-9ba3-2afcdbd83dd3



Tenemos un archivo .env_example que es el que contendra los path de los directorios a comparar. Este lo renombramos a .env y le agregamos los path de los directorios a comparar.

- Si estamos en windows, podemos dar doble click en el path arriba del directorio y luego copiar eso.

```bash
PATH_OLD_FILE=C:\Users_example\User_Example\Desktop\directory1
PATH_NEW_FILE=C:\Users_example\User_Example\Desktop\directory2
```

### Resultado (Con los ejemplos dados)

![image](https://github.com/Fabian-Martinez-Rincon/modify-SQL/assets/55964635/1dfc8b21-bf12-4851-a74a-03c25a625828)

Este software se podria escalar a una carpeta con muchos archivos y compararlos, pero para este caso solo se comparan dos archivos.

---

### 📂 Documentación por archivo