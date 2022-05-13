from tkinter import *
import requests

class Interface():
	def __init__ (self):
		OPTIONS = ['BRL', 'USD', 'EUR']
		screen = Tk()
		
		# Funtion
		def enter():
			e = EconomiaApi(variableOne.get(), variableTwo.get())
			label = Label(screen, text='{}$ {}'.format(variableOne.get(), e.get()))
			label.place(relx = 0.0,
                 rely = 1.0,
                 anchor ='sw')
                 
		# Configure
		screen.title('Currency Conversion')
		screen.geometry('200x130')
		
		# Draw
		variableOne = StringVar(screen)
		variableOne.set(OPTIONS[0])
		
		variableTwo = StringVar(screen)
		variableTwo.set(OPTIONS[1])
		
		dOne = OptionMenu(screen, variableOne, *OPTIONS)
		dTwo = OptionMenu(screen, variableTwo, *OPTIONS)
		button = Button(screen, text='Enter', command=enter)
		
		dOne.pack(); dTwo.pack(); button.pack()
		screen.mainloop()

class EconomiaApi:
	def __init__ (self, coinOne, coinTwo):
		self.coinOne, self.coinTwo = coinOne, coinTwo
		self.URL = f'https://economia.awesomeapi.com.br/last/{self.coinOne}-{self.coinTwo}'
	
	def get(self):
		if self.coinOne == self.coinTwo:
			return 'ERRO'
		else:	  
			result = requests.get(self.URL)
			print('Response OK' if result else 'Response ERRO')
			
			text = result.json()['{}{}'.format(self.coinOne, self.coinTwo)]['high']; print(text)
			return text

if __name__ == "__main__":
	Interface()
