"""
Author: Rafael Cardoso Pereira
Version: python 3.7.9
Reference: solutionderived from: http://nsayer.blogspot.com/2007/07/algorithm-for-evaluating-poker-hands.html

PS:  I know that every variable must be encapsulated, but encapsulation requires a lot of code to write and, since this is a small local code,
the encapsulation is not really necessary. 
"""
from pokerhand import PokerHand

if __name__== "__main__":
    # testing
    print(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC")))
    print(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")))
    print(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")))
    print(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")))
    print(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")))
    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")))
    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")))
    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")))
    print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")))
    print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")))
    print(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")))
    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")))
    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")))
    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))
    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))
    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))
    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")))
    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")))
    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")))
    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")))
    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))
    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))
    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))
    print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))
    print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))
    print(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")))



