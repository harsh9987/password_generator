import string, secrets

chrs = string.ascii_letters
numbers = string.digits

choose = input("What do you want to generate? (password/pin) : ")
length = input("Choose the length of your password/pin : ")

password_in_chrs = ''.join(secrets.choice(chrs) for i in range(int(length)))
password_in_numbers = ''.join(secrets.choice(numbers) for i in range(int(length)))

print("*********************Python Password Generator**************************")

if choose == "password":
    print(password_in_chrs)

if choose == "pin":
    print(password_in_numbers)

