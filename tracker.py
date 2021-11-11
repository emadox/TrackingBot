import requests
import time

#Variables Global
api_key= 'bd51f74b-ab30-4539-b5a1-f6982887e83b'
bot_token= '2042325182:AAEsZsvOYpgA9wTG_1UqtGnouaac_ze3fkw'
chat_id = '-1001683762953'
time_interval= 5*60 #en segundos
index = 0
interes = ['ETH' , 'BTC' , 'AVAX' , 'SHIB' , 'JOE', 'TOKE' , 'OHM', 'CVX']




headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    

params={
        'start': '1',
        'limit': '5000',
        'convert': 'USD',
    }

BD = [['ETH', 0 ], ['BTC', 0 ] , ['AVAX', 0 ] , ['SHIB', 0 ] , ['JOE', 0 ] , ['TOKE', 0 ] , ['OHM', 0 ] , ['CVX', 0 ]]
BDAB = [['ETH', 4900 ], ['BTC', 70000 ] , ['AVAX', 100 ] , ['SHIB', 0 ] , ['JOE', 5 ] , ['TOKE', 10 ] , ['OHM', 1000 ] , ['CVX', 0 ]]
BDAS = [['ETH', 4500 ], ['BTC', 60000 ] , ['AVAX', 80 ] , ['SHIB', 0 ] , ['JOE', 2 ] , ['TOKE', 10 ] , ['OHM', 1000 ] , ['CVX', 0 ]]

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    #Request a Coinmarketcap
json = requests.get(url, headers=headers, params=params).json()
coins = json ['data']

urlv = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
jsonlive = requests.get(urlv, headers=headers, params=params).json()
            

                        
    
def send_alert(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def price_chk():
    for m in range(len(interes)):
        if BD[m][1] <= BDAB[m][1] & BDAB[m][1] != 0 :
            send_alert(chat_id, msg = f'{interes[m]} BAJA Alerta: {BD[m][1]}')
        if BD[m][1] >= BDAS[m][1]:
            send_alert(chat_id, msg = f'{interes[m]} BAJA Alerta: {BD[m][1]}')

def DBupdate():
    
    
    

    for x in coins:
       for y in  interes:    
           if x['symbol'] == y:     
               print( x['symbol'], x['id'], x['quote']['USD']['price'], x['platform'])
               match x['symbol']:
                   case "ETH":
                       BD [0][1] = x['quote']['USD']['price']
                   case "BTC":
                       BD [1][1] = x['quote']['USD']['price']
                   case "AVAX":
                       BD [2][1] = x['quote']['USD']['price']
                   case "SHIB":
                       BD [3][1] = x['quote']['USD']['price']
                   case "JOE":
                       BD [4][1] = x['quote']['USD']['price']
                   case "TOKE":
                       BD [5][1] = x['quote']['USD']['price']
                   case "OHM":
                       BD [6][1] = x['quote']['USD']['price']
                   case "CBX":
                       BD [7][1] = x['quote']['USD']['price']
    print(BD)
    


def main():
    DBupdate()
    price_chk()


    
if __name__ == '__main__':
    main()