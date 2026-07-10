# This is the code that will encrypt the word, sentence or paragraph as well as decrypt the word, sentence or paragraph.

# Rules of encryption:
# 1) If the word contains at least 3 characters, remove the first letter and append it to the end. 
# Then, add 3 random characters at the beginning and 3 random characters at the end.
# 2) If the word contains fewer than 3 characters, simply reverse the string.

# Rules of decryption:
# 1) If the word contains fewer than 3 characters, reverse it back.
# 2) Otherwise, remove the 3 random characters from the start and 3 from the end. Then, take the last letter and move it back to the beginning.

import random
import string

inp_text=input("You can start typing: ") 
inp_text_list=inp_text.split()

# encryption Side
encoded_words = []

for index, word in enumerate(inp_text_list): 
    if len(word)<=2: # If word is less than 3 words then it will be reversed.
            rev_word= word[::-1]

            encoded_words.append(rev_word)   

    elif len(word)>2: 
        temp1=word[1:]+word[0]  #removing the first letter and appending it to the end.

        random_front = ''.join(random.choices(string.ascii_lowercase, k=3)) # adding 3 random characters at the beginning
        random_back = ''.join(random.choices(string.ascii_lowercase, k=3))  # adding 3 random characters at the end.
        encrypted_word = random_front + temp1 + random_back 

        encoded_words.append(encrypted_word)

encrypted_sentence = " ".join(encoded_words)
print("Secret Message :", encrypted_sentence)

# Decryption Side
decoded_words =[]

for index, word in enumerate(encoded_words):
    if len(word)<=2: 
         rev_word= word[::-1]   # If word is less than 3 words then it will be reversed.

         decoded_words.append(rev_word)

    elif len(word)>2:
         word_cut=word[3:-3]    # removing 3 random characters from the beginning and end.
         temp2=word_cut[-1]+word_cut[0:-1]  

         decoded_words.append(temp2)

decrypted_sentence = " ".join(decoded_words)
print("Secret Message decoded :", decrypted_sentence)