password = ''
count = 0

while password != 'abcd1234' and count < 4: #test statment #l
    password = input('Enter Password ')
    count += 1
print('Password correct in %d attempts' %(count)) if password == 'abcd1234' else print('All attempts failed ')



