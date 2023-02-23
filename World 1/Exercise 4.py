def returns(value):
    print("---------------------")
    print("Class type: ", type(value))
    print("Is upper ?", value.isupper())
    print("Is lower ?", value.islower())
    print("Is alpha numeric ?", value.isalnum())
    print("Is alphabetic ?", value.isalpha())
    print("---------------------")


value = input("Type a value: ")
returns(value)
