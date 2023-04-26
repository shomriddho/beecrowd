string="""This is a dancing sentence
  This   is         a  dancing   sentence  
aaaaaaaaaaa
z"""
string = string.upper()
for i in range(len(string)):
    if i%2==0:
        string[i]=string[i].lower()
print(string)

#not done