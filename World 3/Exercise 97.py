def write(msg):
    length = len(msg)
    print("="*length)
    print(f"{msg}")
    print("="*length) 
    
for x in range (0,3):
    word = str(input("\nType any word or sentence: "))
    write(word)
