import random
art = '''
  ________._________________________     
 /  _____/|   \_   _____/\__    ___/     
/   \  ___|   ||    __)    |    |        
\    \_\  \   ||     \     |    |        
 \______  /___|\___  /     |____|        
        \/         \/                    
___________________                      
\__    ___/\_____  \                     
  |    |    /   |   \                    
  |    |   /    |    \                   
  |____|   \_______  /                   
                   \/                    
________  .____     ___________ ________ 
\_____  \ |    |    \_   _____//  _____/ 
 /   |   \|    |     |    __)_/   \  ___ 
/    |    \    |___  |        \    \_\  \'
\_______  /_______ \/_______  /\______  /
        \/        \/        \/        \/ '''

print(art)
gift = ['Любой предмет мужского гардероба из магазина Vistula', 'Мини-аквариум']
print("Привет!\nЭту мини-программу написала Лиза.\nОна не придумала, что подарить тебе на 23 фераля, поэтому свой подарок ты выберешь сам.\nНадеюсь ты не против :)")
while True:
    answer = input("Отправь 'хочу свой подарок' если хочешь продолжить игру\nПы сы другого варианта ввода нет:)").lower()
    if answer == 'хочу свой подарок':
        print("Я рада, что ты согласился!\nПрограмма рандомно выберет тебе подарок из моего списка\nИтак, вот твой подарок...\n")
        present = random.choice(gift)
        print(str(present))
        if present == gift[0]:
            print("Я оплачу любой предмет гардероба на твой выбор, который ты будешь с удовольствием носить :)")
        elif present == gift[1]:
            print("Я думаю, по согласованию с хозяевами, мы можем купить домой мини-аквариум. Поставим его на деревянную полочку в гостинной. Расходы я беру на себя :)\nПы сы разумеется если ты согласишься")
        break
    else:
        print("Я же говорила, что вариант ввода только один) Подумай еще раз :)")
        continue