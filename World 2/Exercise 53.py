sentence = str(input("Tipe a sentence: ")).upper().strip()
word = sentence.split()
newsentence = ''.join(word)
reverse = ''

for a in range (len(newsentence)-1,-1,-1):
    reverse += newsentence[a]
print("The inverse of ", newsentence,"is:", reverse)
if reverse == newsentence:
    print("The sentence is a palindrome")
else:
    print("The sentence isn't a palindrome")
