import requests, json
import time
from datetime import datetime


def linebot(request):
    try:
        access_token = 'access_token from line'
        secret = 'secret from line'
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        msg = json_data['events'][0]['message']['text']
        tk = json_data['events'][0]['replyToken']
        line_bot_api.reply_message(tk,TextSendMessage(msg))
        print(msg, tk)
        print(json_data)
    except:
        print(request.args)
    return 'OK'


def getAllPickUp():
   # MU783ZP/A 白色Pro Max 256G
   getPickupModel("白色Pro Max 256G","https://www.apple.com/tw/shop/fulfillment-messages?pl=true&mts.0=regular&mts.1=compact&parts.0=MU783ZP/A&searchNearby=true&store=R694")
   # MU793ZP/A 原色Pro Max 256G
   getPickupModel("原色Pro Max 256G","https://www.apple.com/tw/shop/fulfillment-messages?pl=true&mts.0=regular&mts.1=compact&parts.0=MU793ZP/A&searchNearby=true&store=R694")
   # MU2N3ZA/A 黑色Pro Max 256G
   #getPickupModel("黑色Pro Max 256G","https://www.apple.com/hk-zh/shop/fulfillment-messages?pl=true&mts.0=regular&parts.0=MU2N3ZA/A&location=%E9%A6%99%E6%B8%AF")

def getPickupModel(model, target):
   response = requests.get(target)
   if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Access the desired values
        stores = data["body"]["content"]["pickupMessage"]["stores"]

        for store in stores:
            modules = store["partsAvailability"]
            for part_number, module in modules.items():
                pickupSearchQuote = module["pickupSearchQuote"]
                storePickupProductTitle = module["messageTypes"]["regular"]["storePickupProductTitle"]
                if(pickupSearchQuote != "目前無法提供" and pickupSearchQuote != "暫無供應"):
                    print(store["storeName"])
                    print("可現場取貨時間:", pickupSearchQuote)
                    print("商品名稱:", storePickupProductTitle)
                    text = "【" + store["storeName"] + "】"+ storePickupProductTitle
                    text += "\n"+ pickupSearchQuote
                    sendLineMsg(text, "Ub99d5a8e35a56099a95d443c4e401368") #send to me
                    #sendLineMsg(text, "U3e2490547710bdbc016f2879749ddfb8") #send to tiffy
                else:
                    print("【"+store["storeName"]+"】" + "目前無"+model+" 現貨");

        print(datetime.now())

   else:
        print("Failed to retrieve data. Status code:", response.status_code)

def sendLineMsg(myText, receiver):
  headers = {'Authorization':'line authrorizatoin ','Content-Type':'application/json'}
  body = {
      'to': receiver,
      'messages':[{
              'type': 'text',
              'text': myText
          }]
      }
  # 向指定網址發送 request
  req = requests.request('POST', 'https://api.line.me/v2/bot/message/push',headers=headers,data=json.dumps(body).encode('utf-8'))
  # 印出得到的結果
  print(req)
  print(req.text)

# getAllPickUp()


while True:
  getAllPickUp()
  time.sleep(30)
