class Morse:
    def __init__(self):
        self.str_square = "\u25A0"
        self.str_circle = "\u25CF"
        self.morse_dic = {
            "a" : self.str_circle+self.str_square,
            "b" : self.str_square+self.str_circle+self.str_circle+self.str_circle,
            "c" : self.str_square+self.str_circle+self.str_square+self.str_circle,
            "d" : self.str_square+self.str_circle+self.str_circle,
            "e" : self.str_circle,
            "f" : self.str_circle+self.str_circle+self.str_square+self.str_circle,
            "g" : self.str_square+self.str_square+self.str_circle,
            "h" : self.str_circle+self.str_circle+self.str_circle+self.str_circle,
            "i" : self.str_circle+self.str_circle,
            "j" : self.str_circle+self.str_square+self.str_square+self.str_square,
            "k" : self.str_square+self.str_circle+self.str_square,
            "l" : self.str_circle+self.str_square+self.str_circle+self.str_circle,
            "m" : self.str_square+self.str_square,
            "n" : self.str_square+self.str_circle,
            "o" : self.str_square+self.str_square+self.str_square,
            "p" : self.str_circle+self.str_square+self.str_square+self.str_circle,
            "q" : self.str_square+self.str_square+self.str_circle+self.str_square,
            "r" : self.str_circle+self.str_square+self.str_circle,
            "s" : self.str_circle+self.str_circle+self.str_circle,
            "t" : self.str_square,
            "u" : self.str_circle+self.str_circle+self.str_square,
            "v" : self.str_circle+self.str_circle+self.str_circle+self.str_square,
            "w" : self.str_circle+self.str_square+self.str_square,
            "y" : self.str_square+self.str_circle+self.str_square+self.str_square,
            "z" : self.str_square+self.str_square+self.str_circle+self.str_circle,
            "1" : self.str_circle+self.str_square+self.str_square+self.str_square+self.str_square,
            "2" : self.str_circle+self.str_circle+self.str_square+self.str_square+self.str_square,
            "3" : self.str_circle+self.str_circle+self.str_circle+self.str_square+self.str_square,
            "4" : self.str_circle+self.str_circle+self.str_circle+self.str_circle+self.str_square,
            "5" : self.str_circle+self.str_circle+self.str_circle+self.str_circle+self.str_circle,
            "6" : self.str_square+self.str_circle+self.str_circle+self.str_circle+self.str_circle,
            "7" : self.str_square+self.str_square+self.str_circle+self.str_circle+self.str_circle,
            "8" : self.str_square+self.str_square+self.str_square+self.str_circle+self.str_circle,
            "9" : self.str_square+self.str_square+self.str_square+self.str_square+self.str_circle,
            "0" : self.str_square+self.str_square+self.str_square+self.str_square+self.str_square,
            "," : self.str_square+self.str_square+self.str_circle+self.str_circle+self.str_square+self.str_square,
            "?" : self.str_circle+self.str_circle+self.str_square+self.str_square+self.str_circle+self.str_circle,
            ":" : self.str_square+self.str_square+self.str_square+self.str_circle+self.str_circle+self.str_circle,
            "-" : self.str_square+self.str_circle+self.str_circle+self.str_circle+self.str_circle+self.str_square,
            '"' : self.str_circle+self.str_square+self.str_circle+self.str_circle+self.str_square+self.str_circle,
            "(" : self.str_square+self.str_circle+self.str_square+self.str_square+self.str_circle,
            "=" : self.str_square+self.str_circle+self.str_circle+self.str_circle+self.str_square,
            "." : self.str_circle+self.str_square+self.str_circle+self.str_square+self.str_circle+self.str_square,
            ";" : self.str_square+self.str_circle+self.str_square+self.str_circle+self.str_square+self.str_circle,
            "/" : self.str_square+self.str_circle+self.str_circle+self.str_square+self.str_circle,
            "'" : self.str_circle+self.str_square+self.str_square+self.str_square+self.str_square+self.str_circle,
            "_" : self.str_circle+self.str_circle+self.str_square+self.str_square+self.str_circle+self.str_square,
            ")" : self.str_square+self.str_circle+self.str_square+self.str_square+self.str_circle+self.str_square,
            "+" : self.str_circle+self.str_square+self.str_circle+self.str_square+self.str_circle,
            "@" : self.str_circle+self.str_square+self.str_square+self.str_circle+self.str_square+self.str_circle,
            "é" : self.str_circle+self.str_circle+self.str_square+self.str_circle+self.str_circle,
            "á" : self.str_circle+self.str_square+self.str_square+self.str_circle+self.str_square,
            " " : "       "
    
        }
    def convert_to_morse(self,text):
        converted_text = []
        for letter in text.lower():
            
            try:
                converted_text.append(self.morse_dic[letter]+"   ")
            except:
                pass
        return ''.join(map(str, converted_text))           