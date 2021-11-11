import requests
import time

#Variables Global
api_key= 'bd51f74b-ab30-4539-b5a1-f6982887e83b'
bot_token= '2042325182:AAEsZsvOYpgA9wTG_1UqtGnouaac_ze3fkw'
chat_id = '-1001683762953'
threshold = 66000
time_interval= 5*60 #en segundos
index = 0


headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    

params={
        'start': '1',
        'limit': '5000',
        'convert': 'USD',
    }

    
    
interes = ['ETH' , 'BTC' , 'AVAX' , 'SHIB' , 'JOE', 'TOKE' , 'OHM', 'CVX']

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    #Request a Coinmarketcap
json = requests.get(url, headers=headers, params=params).json()
coins = json ['data']




for x in coins:
    for y in  interes:    
        if x['symbol'] == y:
            print( x['symbol'], x['id'], x['quote']['USD']['price'], x['platform'])
            

                        
    
def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

    requests.get(url)
    if price < threshold:
        send_message(chat_id=chat_id, msg=f'Datos Generales:  {price}')
    
def main():
    price_list =[]



create newfile "laconchadetumadre"

if __name__ == '__main__':
    main()