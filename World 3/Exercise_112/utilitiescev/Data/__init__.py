def readmoney(value):
    while True:
        number = input(value).replace(",", ".")
        try:
            return float(number)
        except:
            print("Error, type only numeric values")
        else:
            break
