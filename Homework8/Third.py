from easygui import *

def calculate(month):
    match month:
        case 1:
            msgbox("\nJanuary - 31 days")
        case 2:                     
            msgbox("\nFebruar - 29 days if year is leap")
            msgbox("\nFebruar - 28 days if year is not leap")
        case 3:
            msgbox("\nMarch - 31 days")
        case 4:
            msgbox("\nApril - 30 days")
        case 5:
            msgbox("\nMay - 31 days")
        case 6:
            msgbox("\nJune - 30 days")
        case 7:
            msgbox("\nJuly - 31 days")
        case 8:
            msgbox("\nAugust - 31 days")
        case 9:
            msgbox("\nSeptember - 30 days")
        case 10:
            msgbox("\nOctober - 31 days")
        case 11:
            msgbox("\nNovember - 30 days")
        case 12:
            msgbox("\nDecember - 31 days")     

name = enterbox("Hello stranger, what's your name?")
m = integerbox("Write please number of your month: ", lowerbound = 1, upperbound = 12)
calculate(m)

                        