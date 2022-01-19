import random
class Dusman:
	kalan_can=100
	def alay_etme(self):
		self.kalan_can-=5
		print("\n{}, alay geçmeni duydu ve morali bozuldu !\n-{}: Argh\nDüşmanının {} canı kaldı.".format(dusman,dusman,self.kalan_can))
	def yumruk(self):
		sonuc=random.choices(['hasar_verme','savunması'], [4,1],k=1)[0]
		if (sonuc=="hasar_verme"):
			global kalan_can
			self.kalan_can-=15
			print("\n{}, yumruğundan kaçamadı !\n-{}: Argh\nDüşmanının {} canı kaldı.".format(dusman,dusman,self.kalan_can))
		else:
			print("\n{}, yumruk saldırından kaçtı !\n{} hala {}  cana sahip !".format(dusman,dusman,self.kalan_can))
	def kilic_saldirisi(self):
		sonuc=random.choice(['hasar_verme','savunması'])
		if(sonuc=="hasar_verme"):
			global kalan_can
			self.kalan_can-=25
			print("\n{}, kılıclı saldırınla hasar aldı !\n-{}: argh\nDüşmanının {} canı kaldı. ".format(dusman,dusman,self.kalan_can))
		else:
			print("\n{}, saldırından kalkanıyla korundu !\n{} hala {} cana sahip !".format(dusman,dusman,self.kalan_can))
class Savasci:
	kalan_canim=100
	def alay_etme(self):
		self.kalan_canim-=5
		print("\n{}, senle alay geçti ! !\n{}, moralin bozuldu !\n{} Canın kaldı.".format(dusman,savasci,self.kalan_canim))
	def yumruk(self):
		sonuc=random.choices(['hasar_verme','savunması'], [4,1],k=1)[0]
		if(sonuc=="hasar_verme"):
			global kalan_canim
			self.kalan_canim-=15
			print("\n{}, yumruğuyla sana hasar verdi !\n{}, canın acıdı !\n{} Canın kaldı.".format(dusman,savasci,self.kalan_canim))
		else:
			print("\n{}, Düşmanın yumruk saldırısından kaçtın !\nHala {} canın var !".format(savasci,self.kalan_canim))
	def kilic_saldirisi(self):
		sonuc=random.choice(['hasar_verme','savunması'])
		if(sonuc=="hasar_verme"):
			global kalan_canim
			self.kalan_canim-=25
			print("\n{}, kılıçla canını azalttı !\n{}, vücudun kanıyor !\n{} Canın kaldı.".format(dusman,savasci,self.kalan_canim))
		else:
			print("\n{} saldırıdan kalkanınla korundun !\n{} hala {} cana sahip !".format(savasci,dusman,self.kalan_canim))
print("Bilgilerinizi girin :")
savasci=input("~Savaşçı adı:\n")
dusman=input("~Düşman adı:\n")
print("\n\n-----Karşılaşma başlıyor !-----\n")
rakip=Dusman()
player=Savasci()
i=0
while True :
	if(i>0):
		print("-----\n\nSaldırı sırası sende !")
	else:
		print("İlk saldırıyı sen yap !")
	i+=1
	print("\nSaldırıların Bilgisi:\n~~Alay etme: Kesin hasar verir, 5 hasar\n~~Yumruk: %80 Hasar verme ihtimali, 15 hasar\n~~Kılıç saldırısı: %50 Hasar verme ihtimali, 25 hasar ")
	hamle=input("Saldırını yaz : ")
	if(hamle=="Alay etme"):
		rakip.alay_etme()
	if(hamle=="Yumruk"):
		rakip.yumruk()
	if(hamle=="Kılıç saldırısı"):
		rakip.kilic_saldirisi()
	if(rakip.kalan_can<=0):
		print("-----\n\nRakibin canı bitti !\n-----Tebrikler {}, karşılaşmayı Kazandın !!!-----".format(savasci))
		break
	print("-----\n\nSaldırı sırası Düşmanda !")
	saldirisi=random.choices(['Alay_etme','Yumruk','Kilic_saldirisi'],[2,1,1],k=1)[0]
	if(saldirisi=="Alay_etme"):
		player.alay_etme()
	if(saldirisi=="Yumruk"):
		player.yumruk()
	if(saldirisi=="Kilic_saldirisi"):
		player.kilic_saldirisi()
	if(player.kalan_canim<=0):
		print("\n{} canın bitti !\n-----Rakibin {} karşılaşmayı Kazandı !!!-----".format(dusman))
		break
