import time
import requests
import datetime
import threading
from typing import List
from logger import Logger


class StockPriceStream(threading.Thread):
    _TIME_INTERVAL = 1
    _ENDPOINT = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'
    
    def __init__(self, name: str):
        threading.Thread.__init__(self)
        self._name = name
        self._running = False
        self._endpoint = self.__class__._ENDPOINT.format(name)
        self._logger = Logger.get_instance('Stock')
        
    def run(self):
        self._running = True
        while self._running:
            response = requests.get(self._endpoint)
            if response.status_code != 200:
                self._logger.info(f'Response with status code => {response.status_code}')
                time.sleep(self.__class__._TIME_INTERVAL)
                continue
            
            data = response.json()
            date = datetime.datetime.utcnow().isoformat()
            
            quote = {
                'date': date,
                'price': float(data.get('price'))
            }
            
            self._logger.info(quote["price"])
            time.sleep(self.__class__._TIME_INTERVAL)
    
    def stop(self):
        self._running = False
        self.join()
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def running(self) -> bool:
        return self._running
