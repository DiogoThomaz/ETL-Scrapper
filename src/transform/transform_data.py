import time
from bs4 import BeautifulSoup

from src.transform.configs import SoupSeletores



class Transform:
    """
    Uma classe para transformar os dados de uma página da web em uma lista de produtos do AliExpress.

    Esta classe utiliza a biblioteca BeautifulSoup para analisar o conteúdo HTML da página
    e extrair informações sobre os produtos, como preço, quantidade vendida, descrição e links.

    Métodos:
        aliexpress_products(page):
            Transforma o conteúdo HTML da página em uma lista de dicionários, onde cada dicionário
            representa um produto com informações de preço, quantidade vendida, descrição e link.

    """
    def _html_to_page(self, html):
        """
        Transforma o html em objeto beautifoulsoup

        Args:
            html (str): Código html
        """
        page = BeautifulSoup(html, 'html.parser')
        return page

    def aliexpress_products(self, html):
        """
        Extrai uma lista de produtos de um html

        Args:
            html (str): Código Html

        Returns:
            collected_data: Lista de produtos
        """
        soup = self._html_to_page(html)

        preco_elementos = soup.select(SoupSeletores.PRECO)
        vendidos_elementos = soup.select(SoupSeletores.VENDIDOS)
        descricao_elementos = soup.select(SoupSeletores.DESCRICAO)
        link_elementos = soup.select(SoupSeletores.LINKS)

        print('[i] - Coletando dados da página...')

        collected_data = []
        for preco_element, vendidos_element, descricao_element, link_element in zip(
            preco_elementos, vendidos_elementos, descricao_elementos, link_elementos
        ):
            preco = preco_element.text
            vendidos = vendidos_element.text.split(' ')[0]
            descricao = descricao_element.text
            link = 'https:' + link_element['href']

            collected_data.append({
                'descricao': descricao,
                'preco': preco,
                'vendidos': vendidos,
                'link': link
            })

        print('[i] - Dados coletados com sucesso!')
        return collected_data
