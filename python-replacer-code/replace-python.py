try:
    import os
except ImportError:
    print("Le module os n'est pas disponible.")
    exit()

try:
    import shutil
except ImportError:
    print("Le module shutil n'est pas disponible.")
    exit()






def check_path(dest_dir_path):
    if not os.path.isdir(dest_dir_path):
        print("Le répertoire de destination n'existe pas.")
        return False
    return True
    
def check_file(source_file_path):
    if not os.path.isfile(source_file_path):
        print("Le fichier source n'existe pas.")
        return False
    return True

def copy_file_to_dir(source_file_path, dest_dir_path, recursive, ignore_files):
    source_file_name, source_file_ext = os.path.splitext(os.path.basename(source_file_path))

    if recursive:
        for root, dirs, files in os.walk(dest_dir_path):
            for filename in files:
                if any(ignore in filename for ignore in ignore_files):
                    continue
                old_file_path = os.path.join(root, filename)
                new_file_name, _ = os.path.splitext(filename)
                new_file_path = os.path.join(root, new_file_name + source_file_ext)
                try:
                    shutil.copy(source_file_path, new_file_path)
                except PermissionError:
                    print(f"Permission refusée pour le fichier {new_file_path}. Le fichier n'a pas été copié.")
    else:
        for filename in os.listdir(dest_dir_path):
            if any(ignore in filename for ignore in ignore_files):
                continue
            old_file_path = os.path.join(dest_dir_path, filename)
            if os.path.isfile(old_file_path):
                new_file_name, _ = os.path.splitext(filename)
                new_file_path = os.path.join(dest_dir_path, new_file_name + source_file_ext)
                try:
                    shutil.copy(source_file_path, new_file_path)
                except PermissionError:
                    print(f"Permission refusée pour le fichier {new_file_path}. Le fichier n'a pas été copié.")
    input("Appuyez sur une touche pour quitter...")

def main():
    source_file_path = input("Veuillez entrer le chemin vers le fichier source: ")
    dest_dir_path = input("Veuillez entrer le chemin vers le répertoire de destination: ")

    while (not check_file(source_file_path)):
        source_file_path = input("Veuillez entrer le chemin vers le fichier source: ")
    
    while (not check_path(dest_dir_path)):
        dest_dir_path = input("Veuillez entrer le chemin vers le répertoire de destination: ")

    recursive = input("Voulez-vous activer la récursivité ? (oui/non): ")
    recursive = recursive.lower() == "oui"

    ignore_files = []
    print("Indiquez des caractères qui sont contenus dans le noms des fichiers à ignorer (-1 pour terminer) : ")
    while True:
        ignore_file = input()
        if ignore_file == '-1':
            break
        print("Les fichiers qui contiennent : " + ignore_file + " seront ignorés.")
        ignore_files.append(ignore_file)

    copy_file_to_dir(source_file_path, dest_dir_path, recursive, ignore_files)

if __name__ == "__main__":
    main()
