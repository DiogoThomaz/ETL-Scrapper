class URLs:
    PADRAO = 'https://pt.aliexpress.com/w/wholesale-{}.html?catId=0&initiative_id=AS_{}&SearchText={}&spm=a2g0o.home.1000002.0&trafficChannel=ppc&g=y&page={}'
    GPU = 'https://pt.aliexpress.com/w/wholesale-placa-de-video.html?catId=0&initiative_id=AS_20230829154517&SearchText=placa+de+video&spm=a2g0o.home.1000002.0&trafficChannel=ppc&g=y&page={}'
    BASE = 'https://pt.aliexpress.com/w/wholesale-raspberry-pi.html?SearchText=raspberry+pi&catId=0&initiative_id=AS_20230829144122&spm=a2g0o.home.1000002.0&trafficChannel=ppc&g=y&page={}'
    CATEGORIA = 'https://pt.aliexpress.com/category/201000020/consumer-electronics.html?category_redirect=1&spm=a2g0o.home.105.1.25901c91C086cn&CatId=201000020&trafficChannel=ppc&isCategoryBrowse=true&g=n&page={}'

class Headers:
    USER_AGENTE = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
