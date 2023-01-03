while True:

    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == 'bharath':
        if password == 'surya':
            flag = 1
            print()
            break
        else:
            print('Sorry wrong password')
    else:
        print('Sorry invalid credentials')

while flag == 1:
        
    import requests
    print('Welcome to basic API Tester')
    print()
    while True:
        print('Chose from the options below')
        print('''1) GET
2) POST
3) EXIT ''' )
        ch = int(input('Enter option: '))
        if ch == 1:    
            url = input('Enter a URL: ')
            dict3 = {}
            dict1 = {}
            i=input('Do you want to include any parameters ?[y/n] : ')
            if i=='y':
                num_keys = int(input('Enter the number of keys to add: '))
                
                for x in range(num_keys):
                    key = input('Enter name of the key: ')
                    value = input('Enter name of the value: ')
                    dict1[key] = value
            h=input('Do you want to include any headers ?[y/n] : ')
            if h=='y':
                num_keys = int(input('Enter the number of keys to add: '))
                
                for x in range(num_keys):
                    key = input('Enter name of the key: ')
                    value = input('Enter name of the value: ')
                    dict3[key] = value
            response = requests.get(url, params=dict1, headers=dict3)
            if response.status_code in range(200, 300):
                print('Succesfull')
                print()
                try:
                    print(response.json())
                except:
                    print('No Body present hence dumping entire content')
                    print(response.content)
            elif response.status_code in range(400, 550):
                print('Error')
        elif ch == 2:
            url = input('Enter the URL into which you want to post data : ')
            num_keys = int(input('Enter the number of keys to add: '))
            
            h1=input('Do you want to include any headers ?[y/n] : ')
            if h1=='y':
                num_keys = int(input('Enter the number of keys to add: '))
                dict4 = {}
                for x in range(num_keys):
                    key = input('Enter name of the key: ')
                    value = input('Enter name of the value: ')
                    dict4[key] = value
                response = requests.post(url, header=dict4)
            else:    
                response = requests.post(url)
            num_keys = int(input('Enter the number of keys to add: '))
            dict2 = {}
            for x in range(num_keys):
                key = input('Enter name of the key: ')
                value = input('Enter name of the value: ')
                dict2[key] = value
            
                
            response = requests.post(url, data = dict2)
            if response.status_code in range(400, 550):
                print()
                print('Error')
            else:
                print(response.content)
        elif ch == 3:
            flag = 0
            print("Exiting...")
            break
