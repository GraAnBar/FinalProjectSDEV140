""" GoodBurger.py
You can place an order and receive your digital food
by Grace Bartley 4/25/2023
Update: 5/10/2023 Had to overhaul the program to better suit the application and make it look better"""


from tkintertoy import Window

class Gui(object):
    def makeGui(self):
        """ The start for making the gui """
        self.dialog = Window()
        self.dialog.setTitle('Good Burger Order')
        # start of notebook with variables
        tabs = ('Food', 'Sides')                                            # vairable to title of each tab
        pages = self.dialog.addNotebook('notebook', tabs)                   # variable for notebook pages
        # Pages 'Food'
        self.food = pages[0]
        self.food.addLabel('title', 'Choose your Main Food Item', width=70)
        self.food.plot('title', row=0)
        self.food.addLabel('Combo')
        self.food.plot('Combo', row=1, column=0)
        combo = ('Cheeseburger Meal (Cheeseburger, Large Fry, Large Soda', \
                 'Chicken Nugget Meal (Chicken Nuggets, Large Fry, Large Soda)')      # variable for the food combo
        self.food.addLabel('Single')
        self.food.plot('Single', row=2, column=1)
        single = ('Cheeseburger','Chicken Nuggets')                         # variable for the food single
        self.food.addCheck('combo','Combo',combo, orient='vertical')
        self.food.addCheck('single','Single', single, orient='vertical')
        self.food.set('combo',combo[:0])
        self.food.plot('combo', row=2)
        self.food.set('single',single[:0])
        self.food.plot('single', row=3)
        # Pages 'Side'
        self.sides = pages[1]
        self.sides.addLabel('title', 'Choose your Side(optional)', width=70)
        self.sides.plot('title', row=0)
        self.sides.addLabel('Side Item')
        self.sides.plot('Side Item', row=1, column=0)
        sideItems = ('Fries', 'Salad')                                      # variable for the side item
        self.sides.addLabel('Desert')
        self.sides.plot('Desert', row=1, column=1)
        desert = ('Ice Cream','Chocolate Chip Cookie(C.C.C)')               # variable for the side desert item
        self.sides.addCheck('sideItems','Side Item', sideItems, orient='vertical')
        self.sides.addCheck('desert','Desert',desert, orient='vertical')
        self.sides.set('sideItems', sideItems[:0])
        self.sides.plot('sideItems', row=2)
        self.sides.set('desert',desert[:0])
        self.sides.plot('desert', row=3)
        # Placing the dialog
        self.dialog.addButton('addfood', '', [('Add to Order', self.addOrder)])       # button to confirm you made an order
        self.dialog.addButton('command', space=20)
        self.dialog.changeWidget('command', 1, text='Exit')
        self.dialog.addText('summary', 50, 10,'Status')                     # text box to display results of making order
        self.dialog.plot('summary', row=4, column=0, columnspan=1)
        self.dialog.plot('addfood', row=1, column=0, columnspan=1)
        self.dialog.plot('command', row=2)
        self.dialog.plot('notebook', row=0)
        self.dialog.set('notebook', 0)

    def addOrder(self):
        """ This is where the statement will pop up after you press 'Add to Order' """
        self.dialog.set('summary', 'Thank you, your order has been placed!', allValues=True)
        
def main():
    """ This is how it will display the GUI """
    gui = Gui()
    gui.makeGui()
    gui.dialog.waitforUser()

if __name__ == '__main__':
    main()
