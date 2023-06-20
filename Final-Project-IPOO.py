from cpf_generator import CPF

class person ():
    gender = None
    age = None
    name = None
    def __init__(self, name, age, gender):
        self.gender = gender
        self.age = age
        self.name = name
    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age
        return self.age

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender
        return self.gender

class patient(person):
    __address = None
    __cpf = None
    __birthday = None
    def __init__(self, name,age,gender,address,cpf,birthday,amount):
        super().__init__(name,age,gender)
        self.__address = address
        self.__cpf = cpf
        self.__birthday = birthday
        self.__amount = amount

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getBirthday(self):
        return self.__birthday

    def setBirthday(self, birthday):
        self.__birthday = birthday

    def getAmount(self):
        return self.__amount

    def makeWithdraw(self, amount, withdrawal, transactionList):
        if amount < withdrawal:
            return print(f'Error, you dont have money enough!\nCurrent amount: ${amount:.2f}')
        else:
            self.__amount -= withdrawal
            historyTuple = f"Withdrew of -${withdrawal:.2f}"
            transactionList.append(historyTuple)
            return self.__amount

    def makeDeposit(self,amount,depositValue, transactionList):
        if depositValue < 0:
            return print('---Error! You can not deposit a value less then $0---')
        else:
            self.__amount += depositValue
            historyTuple = f'Deposit of ${depositValue:.2f}'
            transactionList.append(historyTuple)
            return self.__amount

def validateCPF():
    patientCpf = input('What is your CPF number: ')
    if CPF.validate(patientCpf) == True:
        print(f"O CPF {CPF.format(cpf)} é Válido!")
    else:
        print(f"O CPF {CPF.format(cpf)} Inválido!")

def showDashboard():
    print('\n')
    print('\t\t____________DASHBOARD_____________')
    print('\t\t| 1- See your information        |')
    print('\t\t| 2- Changes in your information |')
    print('\t\t| 3- Make a withdraw             |')
    print('\t\t| 4- Make a deposit              |')
    print('\t\t| 5- See transaction list        |')
    print('\t\t| 0- Exit                        |')
    print('\t\t__________________________________')


print('|-----REGISTER-----|')
print('First, we need to register you =)')
print('Please answer the following questions')
patientName = input('Your name: ')
patientAge = input('Your age: ')
patientAge = patientAge + ' years old'
patientBirthday = input('When is your birthday (mm/dd): ')
patientAddress = input('Which is your address: ')
patientGender = input('Which is your gender: ')
#patientCpf = input('What is your CPF number: ')
validateCPF()
patientAmount = float(input('Initial deposit amount: $'))
newPatient = patient(patientName, patientAge, patientGender, patientAddress, patientCpf, patientBirthday,patientAmount)


transactionList = []

while True:
    showDashboard()
    mainChoice = int(input('\nWhat you would like to do: '))

    if mainChoice == 0:
        print('Leaving...')
        break

    elif mainChoice == 1:
        print('\n_____________________INFORMATION_____________________')
        print(f'|Name:          {newPatient.getName():<36}|')
        print(f'|Age:           {newPatient.getAge():<36}|')
        print(f'|Birthday date: {newPatient.getBirthday():<36}|')
        print(f'|Address:       {newPatient.getAddress():<36}|')
        print(f'|Gender:        {newPatient.getGender():<36}|')
        print(f'|CPF:           {newPatient.getCpf():<36}|')
        print(f'|Amount:        ${newPatient.getAmount():<35.2f}|')
        print('|___________________________________________________|\n')

    elif mainChoice == 2:
        print(f'-----INFORMATION CHANGE-----')
        print('1- Change your birthday date')
        print('2- Change your name')
        print('3- Change your age')
        print('4- Change your address')
        print('5- Change your gender')
        print('6- Change your CPF')
        print('7- Return')
        choice = int(input('What you would like to do: '))
        while True:
            if choice == 1:
                newBirthdayDate = input('Please, type your new birthday date (mm/dd): ')
                newPatient.setBirthday(newBirthdayDate)
                print('-----Your birthday date was successful changed!-----')
                break

            elif choice == 2:
                newName = input('Please, type your new name: ')
                newPatient.setName(newName)
                print('-----Your name was successful changed!-----')
                break

            elif choice == 3:
                newAge = input('Please, type your new age: ')
                newPatient.setAge(newAge)
                print('-----Your age was successful changed!-----')
                break

            elif choice == 4:
                newAddress = input('Please, type your new address: ')
                newPatient.setAddress(newAddress)
                print('-----Your address was successful changed!-----')
                break

            elif choice == 5:
                newGender = input('Please, type your new gender: ')
                newPatient.setGender(newGender)
                print('-----Your gender was successful changed!-----')
                break

            elif choice == 6:
                newCpf = input('Please, type your new CPF: ')
                newPatient.setCpf(newCpf)
                print('-----Your CPF was successful changed!-----')
                break

            elif choice == 7:
                break

    elif mainChoice == 3:
        removeAmount = float(input('How much would you like to withdraw: $'))
        print('-----Withdrawal made successfully-----')
        newPatient.makeWithdraw(newPatient.getAmount(),removeAmount,transactionList)
        print(f'Your new amount is: ${newPatient.getAmount():.2f}')

    elif mainChoice == 4:
        amountDeposit = float(input('How much would you like to deposit: $'))
        newPatient.makeDeposit(newPatient.getAge(), amountDeposit, transactionList)
        print(f'-----Deposit made successfully-----')
        print(f'Your new amount is ${newPatient.getAmount()}')

    elif mainChoice == 5:
        print('\n\t\t__________Statement__________')
        for e in transactionList:
            print('\t\t|', f'{e:<27}|')
        print('\t\t_____________________________')
        print(f'\t\t|  Amount: ${newPatient.getAmount():<17}|')
        print('\t\t_____________________________')
















