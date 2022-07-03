from ast import Import

import json
import time
from binance.client import Client
from binance.enums import *
import Setting

api_key = 'i1WSVGPkm6w1giMQLhQsS1oF49Osv4iJCQgMGDILN73eIm0ns8YCM46V3vnJPbH0'
api_secret = '8sTcKVWPncxYyrx0Lutp0fW3KRQuNTGNnitK3YVaYaabfyH1j6U9byHIIZhjDY5g'

TENGO_BUSD = False
TENGO_USDT = False
MINIMO_BUSD = 20
MINIMO_BUSD = 20
MINIMO_USDT = 20
OPERACION=''


client = Client ( api_key, api_secret)
print ("login")
# info = client.get_symbol_ticker (symbol = "BTCBUSD") #BUSD
# info2 = client.get_symbol_ticker (symbol = "BTCUSDT") #USDT
# print (info)
# print (info2)
info5 = client.get_symbol_ticker (symbol = "BUSDUSDT") #BUSD
# si price es mayor a uno entonces busd es mayor que usdt: comprar usdt

print (info5)

# info4 = client.get_exchange_info()
# simbolos = info4['symbols']
# for a in simbolos : 
#     # datos = a['symbol'] ,a['pricePrecision'] ,a['quantityPresicion']
#     if a['symbol']=='USDTBUSD':
#         print ("ver")
#         # print (a['pricePrecision'])
#         print (a['quantityPrecision'])
#         print (a['symbol'])

        
# print ("exit")
# print(type(info2))
i=0
try:

    while i<24:#cantidades de repeticiones
        # precioBUSD = info.get("price")
        # print("0")
        # print(precioBUSD)
        
        # precioUSDT = info2.get("price")
        # print("1")
        # print(precioUSDT)
        #liquidez
        info3 = client.get_account()
        balan = info3['balances']
        for c in balan:
            if float (c['free']) > 0:
                if(c['asset']) =="BUSD":
                    TENGO_BUSD=True
                    DISPONIBLE_BUSD = float (c['free'])
                if(c['asset']) =="USDT":
                    TENGO_USDT=True
                    DISPONIBLE_USDT = float (c['free'])
                    

                print (c)

        print (DISPONIBLE_BUSD)
        print (DISPONIBLE_USDT)

        print("terminado")
    # si price es mayor a uno entonces busd es mayor que usdt: comprar usdt
        
        precio = info5.get("price")
        print(precio)

        if (float(precio) < 1) and TENGO_USDT == True and DISPONIBLE_USDT >= MINIMO_BUSD:
            print("comprarBUSD")
            OPERACION='BUY'
    
        # print(precioBUSD<precioUSDT)
        # print(DISPONIBLE_USDT >= MINIMO_BUSD)

        # precio usdt=1,00 
        # precio busd = 0,99
        if (float (precio) > 1) and TENGO_BUSD == True and DISPONIBLE_BUSD >= MINIMO_USDT:
            print("comprarUSDT")
            OPERACION='SELL'
            print(OPERACION)

    #AVERIGUAR SI SE 
        
            print('hola')
            OPERACION = 'SELL1'
            if OPERACION!='':
                print("entra")
                print(OPERACION)
                orderBuy2 = client.create_test_order (#borrar el test para ejecutar la order real 
                    symbol = 'BUSDUSDT',
                    side = OPERACION,
                    type = 'MARKET',
                    quantity = 20.00000000
                )
        
        time.sleep(10)#el nro hace que se ejecute en 1 hora 3600 sec
        i+=1
        print(i)
except:
    print('error en proceso nro '+ str(i))
    archivo = open("file1.txt","w")#w permito de escritura write...//R de read...
    archivo.write ('error en proceso nro '+ str(i))
    archivo.close()
    i=10000





print("terminado3")

