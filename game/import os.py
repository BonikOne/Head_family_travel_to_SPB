import os

# Путь к папке с изображениями
folder_path = r"C:\Travel to SPB\game\images\make_up"

# Проходим по всем файлам в папке
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png") and len(filename) > 6:
        old_path = os.path.join(folder_path, filename)
        new_filename = filename[6:]
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f"Переименовано: {filename} to {new_filename}")