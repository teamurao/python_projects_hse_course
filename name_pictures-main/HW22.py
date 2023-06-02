import os

filename = input('Введите абсолютный путь к папке с фотографиями: ')
print('Ну, а теперь зайдите в эту папку :)')


def renaming(filename):
    i = 1
    for file in sorted(os.listdir(filename)):
        first_name, ext = os.path.splitext(file)
        if ext.lower() not in '.jpg':
            continue
        full_name = os.path.join(filename, file)
        new_full_name = os.path.join(filename, str(i) + ext)
        os.rename(full_name, new_full_name)
        i += 1
    return


def main():
    renaming(filename)

