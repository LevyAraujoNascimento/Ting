def exists_word(word, instance):
    finalResult = []
    for data in instance.data:
        numLine = 0
        isAvailable = False
        result = {
            "palavra": word.lower(),
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }
        for line in data['linhas_do_arquivo']:
            numLine += 1
            if word.lower() in line.lower():
                isAvailable = True
                result["ocorrencias"].append({"linha": numLine})
        if isAvailable:
            finalResult.append(result)
    return finalResult


def search_by_word(word, instance):
    finalResult = []
    for data in instance.data:
        numLine = 0
        isAvailable = False
        result = {
            "palavra": word.lower(),
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }
        for line in data['linhas_do_arquivo']:
            numLine += 1
            if word.lower() in line.lower():
                isAvailable = True
                result["ocorrencias"].append({
                    "linha": numLine,
                    "conteudo": line
                })
        if isAvailable:
            finalResult.append(result)
    return finalResult
