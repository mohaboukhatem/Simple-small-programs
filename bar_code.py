from barcode import EAN13
from barcode.writer import ImageWriter

def generator(number):

    my_Code = EAN13(number , writer=ImageWriter)
    my_Code.save("b")

if __name__ =="__main__":
    generator(input("donnez 12 chiffres"))
    