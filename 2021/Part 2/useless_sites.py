import os
import random
from webbrowser import open, open_new
import pyautogui as pg

def useless_sites():
	links = [
	"https:\\longdogechallenge.com",
	"https:\\checkboxrace.com",
	"https:\\onesquareminesweeper.com",
	"http:\\heeeeeeeey.com",
	"http:\\corndog.io",
	"https:\\mondrianandme.com",
	"https:\\puginarug.com",
	"https:\\checkboxolympics.com",
	"https:\\alwaysjudgeabookbyitscover.com",
	"https:\\thatsthefinger.com",
	"https:\\cant-not-tweet-this.com",
	"http:\\eelslap.com",
	"http:\\www.staggeringbeauty.com",
	"http:\\burymewithmymoney.com",
	"https:\\smashthewalls.com",
	"https:\\jacksonpollock.org",
	"http:\\endless.horse",
	"https:\\www.trypap.com",
	"http:\\www.republiquedesmangues.fr",
	"http:\\www.movenowthinklater.com",
	"http:\\www.partridgegetslucky.com",
	"http:\\www.rrrgggbbb.com",
	"http:\\www.koalastothemax.com",
	"http:\\www.everydayim.com",
	"http:\\randomcolour.com",
	"http:\\cat-bounce.com",
	"http:\\chrismckenzie.com",
	"https:\\thezen.zone",
	"http:\\hasthelargehadroncolliderdestroyedtheworldyet.com",
	"http:\\ninjaflex.com",
	"http:\\ihasabucket.com",
	"http:\\corndogoncorndog.com",
	"http:\\www.hackertyper.com",
	"https:\\pointerpointer.com",
	"http:\\imaninja.com",
	"http:\\drawing.garden",
	"http:\\www.ismycomputeron.com",
	"http:\\www.nullingthevoid.com",
	"http:\\www.muchbetterthanthis.com",
	"http:\\www.yesnoif.com",
	"http:\\lacquerlacquer.com",
	"http:\\potatoortomato.com",
	"http:\\iamawesome.com",
	"https:\\strobe.cool",
	"http:\\thisisnotajumpscare.com",
	"http:\\doughnutkitten.com",
	"http:\\crouton.net",
	"http:\\corgiorgy.com",
	"http:\\www.wutdafuk.com",
	"http:\\unicodesnowmanforyou.com",
	"http:\\chillestmonkey.com",
	"http:\\scroll-o-meter.club",
	"http:\\www.crossdivisions.com",
	"http:\\tencents.info",
	"https:\\boringboringboring.com",
	"http:\\www.patience-is-a-virtue.org",
	"http:\\pixelsfighting.com",
	"http:\\isitwhite.com",
	"https:\\existentialcrisis.com",
	"http:\\onemillionlols.com",
	"http:\\www.omfgdogs.com",
	"http:\\oct82.com",
	"http:\\chihuahuaspin.com",
	"https:\\popcat.click",
	"http:\\www.blankwindows.com",
	"http:\\tunnelsnakes.com",
	"http:\\www.trashloop.com",
	"http:\\www.ascii-middle-finger.com",
	"http:\\spaceis.cool",
	"http:\\www.donothingfor2minutes.com",
	"http:\\buildshruggie.com",
	"http:\\buzzybuzz.biz",
	"http:\\yeahlemons.com",
	"http:\\wowenwilsonquiz.com",
	"https:\\thepigeon.org",
	"http:\\notdayoftheweek.com",
	"http:\\www.amialright.com",
	"http:\\nooooooooooooooo.com",
	"https:\\greatbignothing.com",
	"https:\\zoomquilt.org",
	"https:\\dadlaughbutton.com",
	"https:\\www.bouncingdvdlogo.com",
	"https:\\remoji.com",
	"http:\\papertoilet.com",
	"https:\\loopedforinfinity.com"
	]

	# ouvre un seul lien au hasard dans la liste
	def random_site():
		site = random.choice(links)
		print(f"\n=> {site} <=")
		open(site)

	# ouvre tous les liens de la liste
	def open_all():
		for liens in links :
			open(liens)

	# script pour spammer Chrome
	def chrome_spam():
		rate = int(input("Nombre de fenêtre à ouvrir: "))
		for i in range(rate):
			os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

	separator = '\n--------------------------------------------'
	while True:
		# présentation
		print('\nQue voulez-vous faire ?\n1 : Ouvrir un lien au hasard\n2 : Ouvrir tous liens\n3 : Spammer Chrome')
		choice = input('\nVotre choix: ')
		if choice == '1':
			random_site()
			print(separator)
		elif choice == '2':
			open_all()
			print(separator)
		elif choice == '3':
			chrome_spam()
			print(separator)
		elif choice == "exit" or choice == "quit":
			break
		else:
			print('\nNon pris en charge. Entrez un numéro correct !')
			print('\n--------------------------------------------')
