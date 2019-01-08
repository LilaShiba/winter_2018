password = 'meow'
user_ans = ''
count = 0
while user_ans != password and count < 3:
    user_ans = input('what is you password')
    count += 1

if count < 3:
    print('your in')
else:
    print('too many tires, you are locked out')
