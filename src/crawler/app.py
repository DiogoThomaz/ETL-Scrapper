import threading
import time

from src.extract.extact_data import Extract
from src.transform.transform_data import Transform
from src.load.load_data import Load



class AliCrawler:
    def __init__(self, product_name='placa de video', timewait=1):
        self.product_name = product_name
        self.timewait = timewait
        self.extract = Extract(product_name)
        self.transform = Transform()
        self.load = Load()
        self.collected_data = []

    def extract_page_data(self, page_number=1):
        product_html = self.extract.page_data(page_number)
        products_data = self.transform.aliexpress_products(product_html)
        self.collected_data.extend(products_data)

    def colect_firt_50_pages(self):
        threads_list: list[threading.Thread] = []
        inicio = time.time()
        for page_number in range(1, 51):
            print('Coletando página: ', page_number)
            time.sleep(self.timewait)

            crawler_thread = threading.Thread(
                target=self.extract_page_data, 
                args=(page_number,)
                )
            threads_list.append(crawler_thread)
            crawler_thread.start()

        for crawler_thread in threads_list:
            crawler_thread.join()

        lista = self.collected_data
        self.load.save_data(
            self.collected_data,
            self.product_name,
        )
        print('Produtos encontrados: ' + str(len(lista)))
        fim = time.time()
        tempo = round((fim-inicio), 2)
        print(f"Utilizado usando timewait de {self.timewait}s")
        print(f"Tempo de execução {tempo}s")