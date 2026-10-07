import pytest

from loja.carrinho import Carrinho
from loja.produto import Calca, Camiseta, Produto


def test_camiseta_herda_a_validacao_do_produto():
    with pytest.raises(ValueError):
        Camiseta("Camiseta básica", -10, "M", "curta")


def test_manga_invalida():
    with pytest.raises(ValueError):
        Camiseta("Camiseta básica", 39.90, "M", "regata")


def test_carrinho_aceita_camiseta_e_calca():
    c = Carrinho()
    camiseta = Camiseta("Camiseta básica", 39.90, "M", "curta")
    calca = Calca("Calça jeans", 129.90, "G", "slim")
    assert isinstance(camiseta, Produto)
    assert isinstance(calca, Produto)
    c.adicionar(camiseta)
    c.adicionar(calca)
    assert c.quantidade_de_pecas == 2


def test_descricao_reaproveita_a_da_mae():
    camiseta = Camiseta("Camiseta básica", 39.90, "M", "curta")
    calca = Calca("Calça jeans", 129.90, "G", "slim")
    assert camiseta.descricao() == "Camiseta básica M: R$ 39.90 · manga curta"
    assert calca.descricao() == "Calça jeans G: R$ 129.90 · slim"