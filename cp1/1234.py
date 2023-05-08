# stringrt="This"
# num = 10

# stringrt = stringrt.upper()
# for i in range(len(stringrt)):
    
#     if i%2!=0:
#         stringrt[3] =stringrt.lower()
        
# print(stringrt)
# # print(stringrt)


while True:
    try:
        sentence = input()
        dancing_sentence = ""
        is_upper = True                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        for letter in sentence:
            if letter != " ":
                if is_upper:
                    dancing_sentence += letter.upper()
                else:
                    dancing_sentence += letter.lower()                                                              
                is_upper = not is_upper                                 
            else:
                dancing_sentence += " "                                                                 
        print(dancing_sentence)
    except EOFError:
        break
