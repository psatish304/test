'''class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print('config is',self.cpu,self.ram)


com1=computer()
com2=computer()


com1.config('i5','8gb')
com2.config('Rayzen 3',8)'''

hungry = input('are you hungry/thirsty.?').lower()
if hungry == 'hungry':
	print('Please Eat something which you can')
elif hungry=='thirsty':
	print('please drink something..')
else:
	print('Enjoy and continue your work')
