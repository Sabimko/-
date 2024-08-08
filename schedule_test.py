import schedule
import time
import requests

def test():
    print("hello itpark")
    print(time.ctime())
    
def get_btc_price():
    print("=====BTCUSDT=====")
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url=url).json()
    # print(response)
    """"Стоимость биткоина на текущее время: {}, цена: {} """
    
    price = response.get('price')
    print(f'Стоимость биткоина на текущее время: {time.ctime}, цена: {price}')
    # print(price)
    
    
schedule.every(1).seconds.do(get_btc_price)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at("10:33").do(test)

while True:
    schedule.run_pending()
    time.sleep(1)
    