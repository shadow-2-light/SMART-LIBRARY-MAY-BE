"""1. ADD BOOK
   2.LEND BOOK
   3.DISPLAY BOOK
   4.RETURN BOOK
   """

class Library:

    def __init__(self,list,name):
        self.name = name
        self.list = list
        self.lendDict = {}

    def displayBooks(self):
        print(f"WE HAVE FOLLOWING BOOKS IN OUR LIBRARY {self.name}")
        for books in self.list:
            print(books)

    def lendBook(self,book,user):
        if book in self.list:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("NOW YOU CAN TAKE THIS BOOK")
            else:
                print(f"SORRY THIS BOOK IS ALREADY USING BY {self.lendDict[book]}")
        else:
            print("THIS BOOK IS NOT PRESENT IN OUR LIBRARY")

    def addBook(self,book):
        self.list.append(book)
        print("THANKS FOR SUPPORT. YOU GIVEN BOOK IS ADDED")

    def returnBook(self,book):
        self.lendDict.pop(book)




if __name__ == '__main__':


     lib = Library(['RICH DAD POOR DAD', 'BILLIONAIRES MINDSET' ,
                    'NEVER GIVE UP' ,'H.C.VERMA'] ,'UP_SKILL_WITH_AVNISH')

     while 1:
        print(f"WELCOME TO {lib.name} LIBRARY , HOW MAY WE CAN HELLP YOU")
        print("1. DISPLAY BOOKS")
        print("2. LEND A BOOK")
        print("3. ADD A BOOK")
        print("4. RETURN A BOOK")

        user_input = int(input(""))

        if user_input==1:
            lib.displayBooks()

        elif user_input==2:
           b = input("ENTER THE NAME OF BOOK YOU WANT TO LEND :")
           c = input("ENTER YOUR NAME HERE :")
           lib.lendBook(b,c)

        elif user_input == 3:
           book = input("ENTER THE NAME OF BOOK :")
           lib.addBook(book)

        elif user_input == 4:
           book = input("ENTER THE NAME OF BOOK :")
           lib.returnBook(book)

        else:
           print("please enter a valid input")
           continue


        print("Press q to quit and c to continue")
        b = input("")
        if b =="q"or b == "Q":
            exit()

        elif b == "c" or b == "C":
            continue

        else:
           print("invalid")
           continue
