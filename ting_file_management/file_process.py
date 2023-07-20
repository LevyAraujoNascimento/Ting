from ting_file_management.file_management import txt_importer
import sys


def numLinhas(dataFile):
    numLine = 0
    for i in dataFile:
        if i:
            numLine += 1
    return numLine


def process(path_file, instance):
    isAvailable = True
    for element in instance.data:
        if element['nome_do_arquivo'] == path_file:
            isAvailable = False
    if isAvailable:
        dataFile = txt_importer(path_file)
        result = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': numLinhas(dataFile),
            'linhas_do_arquivo': dataFile,
        }
        instance.enqueue(result)
        sys.stdout.write(str(result))


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write('Não há elementos\n')
    else:
        name = instance.data[0]['nome_do_arquivo']
        instance.dequeue()
        sys.stdout.write(f'Arquivo {name} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
