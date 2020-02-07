import os


# Vraca putanje svih html fajlova u direktorijumu i poddirektorijumima
def get_html_files(dir_path):
    list_all = os.listdir(dir_path)
    file_list = list()
    for f in list_all:
        file_path = os.path.join(dir_path, f)
        if os.path.isfile(file_path):
            if f.endswith('.html'):
                file_list.append(file_path)
        elif os.path.isdir(file_path):
            file_list = file_list + get_html_files(file_path)
    return file_list
