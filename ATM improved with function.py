import datetime

database_user = {
   'Tola':'password',
    'Bisi':'password',
    'Ade':'password'
}

def login():
    #login function here
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name]):
        print("Welcome " + name)
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False


def bankOperations():
    now = datetime.datetime.now()
    print('Current date and time')
    print (now.strftime ("%d/%m/%Y %H:%M:%S"))
    print('These are the available options:')
    print('1. Balance Enquiry')
    print('2. Cash Deposit')
    print('3. Withdrawal')
    print('4. Complaint')
    print('5. Logout')

    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        print('Account balance')
        print('Your account balance is...')
                
    elif(selectedOption == 2):
        print('Deposit operation')
        deposit = input('Please enter amount to depost \n')
        print('Transaction is successful')
                
    elif(selectedOption == 3):
        print('Withdrawal operations')
        withdraw = input('Please enter amount to withdraw \n')
        print('Transaction is successful')

    elif(selectedOption == 4):
        print('Feedbacks and Complaints')
        Feedback = input('Please enter your feedback/complaint here \n')
        print('Your feedback/complaint has been sucessfully received and being reviewed')

    elif(selectedOption == 5):
        print('Thank you for banking with us')
        exit()   
    else:
        print('Invalid Option selected, please try again')



print("Welcome, what would you like to do?")
print("1. Login")
print("2. Register")

actionSelect = int(input("Select an option \n"))

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()

    bankOperations()
else:
    print('Login failed, username or password incorrect')

