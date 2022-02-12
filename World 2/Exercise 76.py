products = ('Bottle',20,'Book',15.90,'Pen',2.50,'Pencil',1.50,'Scissors',7.60,'A4 paper',10)
print("-"*22)
print("List of products")
print("-"*22)
for c in range (0,len(products)):
    if c % 2 == 0:
        print(f"{products[c]:.<20}",end='')
    else:
        print(f"${products[c]:>6.2f}")
print("-"*22)
