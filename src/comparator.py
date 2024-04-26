import os
import difflib

def compare_files_with_difflib(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_text = file1.readlines()
        file2_text = file2.readlines()

        differ = difflib.Differ()
        diff = differ.compare(file1_text, file2_text)
        
        filtered_diff = [
            line.strip() 
            for line in diff 
            if line.startswith('-') or line.startswith('+')
        ]
        
        return '\n'.join(filtered_diff)

def comparate(file_path1, file_path2):
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        return "No existe"
    if os.path.getsize(file_path1) != os.path.getsize(file_path2):
        return compare_files_with_difflib(file_path1, file_path2)
    return "Iguales"
