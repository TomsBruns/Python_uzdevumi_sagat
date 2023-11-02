"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""










class AAA:
    def  __init__(self):
        self.roman_sk={
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M'
    }
    def to_roman(self,num):
        result=""
        for value, numeral in sorted(self.roman_sk.items(), key=lambda x: x[0], reverse=True):
            while num >=value:
                result+= numeral
                num-=value
        return result
#piemērs
skaitlis=1234567810
#definē objektu
kk=AAA()
#jaunajam objektam izsauc klases metode
romieshu=kk.to_roman(skaitlis)
#noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romieshu}.")