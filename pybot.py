bot_dict = {
   'おはよう' : 'おはようございます',
   'ありがとう': 'どういたしまして',
   'さようなら': 'またのご利用お待ちしております'
   }

while True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break
    
    if not response:
        response = '何を言っているか、分かりません'
    print(response)

    if 'さようなら' in command:
        break