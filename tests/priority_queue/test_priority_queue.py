from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    # enfileirando os elementos
    for i in range(10):
        mock = {
            "qtd_linhas": i
        }
        queue.enqueue(mock)
    assert queue.__len__() == 10
    # testando prioridade
    assert queue.is_priority({"qtd_linhas": 1000}) is False
    # removendo um elemento
    queue.dequeue()
    assert queue.__len__() == 9
    # buscando um elemento
    assert queue.search(0) == {"qtd_linhas": 1}
    # index de busca inválido
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(1000)


# test_basic_priority_queueing()
