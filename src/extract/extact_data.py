
import datetime
import requests

from src.extract.configs import URLs, Headers



class SearchUrlGenerator:
    """
    Cria a url para um determinado produto
    Exemplo: https://pt.aliexpress.com/w/wholesale-placa-de-video.html?catId=0&initiative_id=SB_20231003082014&SearchText=placa+de+video
    """
    def __init__(self):
        self.url = URLs.PADRAO

    def _format_spaces_search(self, search_term):
        search_term = search_term.replace(' ', '+')
        return search_term
    
    def _format_spaces_url(self, search_term):
        search_term = search_term.replace(' ', '-')
        return search_term
    
    def _generate_yyyymmdd(self):
        now = datetime.datetime.now()
        offset = datetime.timedelta(hours=-5)  # Deslocamento de 5 horas atrás do GMT
        adjusted_time = now + offset
        formatted_date = adjusted_time.strftime('%Y%m%d%H%M%S')
        return formatted_date

    def build_url(self, search_term, page_number=1):
        builded_url = self.url
        html_search_term = self._format_spaces_url(search_term)
        search_term_url = self._format_spaces_search(search_term)
        url_time = self._generate_yyyymmdd()
        url = builded_url.format(html_search_term, url_time, search_term_url, page_number)
        return url




class Extract:
    """
    Uma classe para extrair dados relacionados a um produto do Aliexpress.

    Esta classe é responsável por gerar URLs de pesquisa, fazer solicitações 
    HTTP para buscar dados da página.

    Atributos:
        product_name (str): O nome do produto a ser pesquisado.
    
    Métodos:
        page_data(page_number=1):
            Coleta o conteúdo HTML de uma página específica relacionada à pesquisa do produto.
    """
    def __init__(self, product_name='placa de video') -> None:
        self.search_url_generator = SearchUrlGenerator()
        self.product_name = product_name

    def page_data(self, page_number=1):
        url = self.search_url_generator.build_url(self.product_name, page_number)
        res = requests.get(url, Headers.USER_AGENTE)

        if res.status_code == 200:
            page = res.content
            return page
        
        else:
            page = None
            return page
