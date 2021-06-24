
#Creating a password database

r1=8976
r2=5236
r3=2493
r4=4591

#Base for the users who have signed up

n1='Jeff'
n2='Musk'
n3='Quaza'
n4='Liza'

#Making an input platform for the user

i1=input('Enter your username: ')
i2=int(input('Enter your password\n'))

#Making the error message

t1='Error occured! Please see to it that you have signed up'

#Users hub,Totally Extendable

if i1==n1 and i2==r1:
    print('You are good to go!')

elif i1==n2 and i2==r2:
    print('You are good to go!')

elif i1==n3 and i2==r3:
    print('You are good to go!')

elif i1==n4 and i2==r4:
    print('You are good to go!')

elif i1!=n1 or i2!=r1:
    print('Your username or password is incorrect!')
    print(t1)

elif i1!=n2 or i2!=r2:
    print('Your username or password is incorrect!')
    print(t1)

elif i1!=n3 or i2!=r3:
    print('Your username or password is incorrect!')
    print(t1)

elif i1!=n4 or i2!=r4:
    print('Your username or password is incorrect!')
    print(t1)


