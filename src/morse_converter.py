Map = {'a' : ".-",'b' :"-...",'c' :"-.-.",'d' : "-..",'e' : ".",'f' : "..-.",'g': "--.",'h' :"....",'i' :"..",'j' :".---",'k' :"-.-",'l' :".-..",'m':"--",'n' :"-.",'o': "---",'p':".--.",'q' :"--.-",'r' :".-.",'s' :"...",'t' :"-",'u' :"..-",'v' :"...-",'w' :".--",'x':"-..-",'y' :"-.--",'z' :"--..",'1' : ".----",'2': "..---",'3': "...--",'4': "....-",'5': ".....",'6': "-....",'7': "--...",'8': "---..",'9': "----.",'0': "-----",'.' : ".-.-.-" ,',': "--..--" ,';' :"---..." ,'?' :"..--..",'\'' : ".----.",'-': "-....-",'/' :"-..-.",'(' :"-.--.-",')' :"-.--.-",'\"' :".-..-.",' ' : ".......",',': "--..--" ,';' :"---..." ,'?' :"..--..",'\'' : ".----.",'-': "-....-",'/' :"-..-.",'(' :"-.--.-",')' :"-.--.-",'\"' :".-..-.",' ' : "......." }
def mors_conver(Str1):
  morse = []
  for S in Str1:
    for key,val in Map.items():
      if key == S :
        morse.append(val)
  Morse = " ".join(str(x) for x in morse)
  return Morse
def text_conver(Morse):
  txt = []
  for m in Morse:
    for key,val in Map.items():
      if val == m :
        txt.append(key)
  Text = "".join(str(x) for x in txt)
  return Text



if __name__ == "__main__": 
  print("Converting the text to morse:\t")
  Str = input("Enter the string:")
  Morse= mors_conver(Str)
  print(Morse)
  print("\nText:\n")
  Text = text_conver(Morse.split(" "))
  print(Text)
