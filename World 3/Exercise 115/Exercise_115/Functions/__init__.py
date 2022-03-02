def validation_file(data):
    try:
        a = open(data,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def create(data):
    try:
        a = open(data,'wt+')
        a.close()
    except:
        print('An Error has occured while creating the file')
    else:
        return a

def registering(data,name='Unknown',age=0):
    a = open(data,'at')
    a.write(f'{name};{age}\n')
    a.close()
    

def mensagem():
    print('The DataBase Has Been Created!')

def search(data):
    try:
        a = open(data,'rt')
    except:
        error_database()
    else:
        for x in a:
            organized_data = x.split(';')
            organized_data[1] = organized_data[1].replace('\n','')
            print(f'Name: {organized_data[0]:<15}{organized_data[1]:>5} years old')


def error_database():
    print('DataBase wasn\'t found')
    print('To visualize all the people')
    print('you have to register someone first!')
    print('In the home screen select the register option')
    print('to create a database')
