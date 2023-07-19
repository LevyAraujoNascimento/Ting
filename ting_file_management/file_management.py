import sys


def txt_importer(path_file):
    if path_file.find('.txt') == -1:
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
