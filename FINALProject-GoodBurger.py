""" GoodBurger.py
You can place an order and receive your digital food
by Grace Bartley 4/25/2023 """

from tkintertoy import Window


def makeGui():
    """ This is where the GUI will be made """
    win = Window()
    win.setTitle('Order')
    win.addButton('exit', '', [('Exit', win.cancel)])
    win.addButton('Ok', '', space=5, orient='horizontal')
    win.plot('Ok', row=5, pady=20)
    win.plot('exit', row=6, pady=30)
    return win
   
def main():
    win = makeGui()
    win.waitforUser()
main()
