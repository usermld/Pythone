'''
1. создания файла: +++
    - открываем файл на режи дозапись (а) +++
2. добавление контакта: +++
    - запросить у пользователя данные контакта +++
    - открыть открываем файл на режи дозапись (а) +++
    - добавить контакт +++
3. вывод данных на экран: +++
    - открыть файл на чтение (r) +++
    - считать файл +++
    - вывести на экран +++
4. поиск контакта: +++
    - выбор варианта поиска +++
    - запросить данные для поиска +++
    - открыть файл на чтение +++
    - считываем даные файла, сохраняем их в переменную +++
    - осуществляем поск контакт +++
    - вывести на экран найденый контакт +++
5. Создание UI (пользовательского интерфейса): +++
    - вывести меню на экран +++
    - запросить у пользователя вариант действия +++
    - запустить соотвествующию функцию +++
    - осуществить возможность выхода из программы +++
'''


def input_surname():
    return input("Введите фамилию контакта: ").title()

def input_name():
    return input("Введите имя контакта: ").title()

def input_patronymic():
    return input("Введите отчество контакта: ").title()

def input_phone():
    return input("Введите номер контакта контакта: ")

def input_addres():
    return input("Введите адресс (город) контакта: ").title()


def creat_contactk():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    addres = input_addres()
    return f"{surname} {name} {patronymic}: {phone}\n{addres}\n\n"

def add_contactk():
    contactk_str = creat_contactk()
    with open("phone_book.txt", "a", encoding="utf-8") as file:
        file.write(contactk_str)


def print_contacts():
    with open("phone_book.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()
    #print([contacs_str])
    contacts_list = contacts_str.rstrip().split("\n\n")
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

def copy_contact():
    print(
            "Возможнве варианты копирования:\n"
            "1. По фамилии\n"
            "2. По имени\n"
            "3. По отчеству\n"
            "4. По телефону\n"
            "5. По адресу(город)\n"
            )
    var = input("Выберите вариант действия: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("некоректный вод")
        var = input("Выберите вариант поиска:")

        
    i_var = int(var) - 1
    
    search = input("Введите данные для поиска: ").title()

    with open("phone_book.txt", "r", encoding="utf-8") as file:
            contacs_str = file.read()
    #print([contacts_str])
    contacs_list = contacs_str.rstrip().split("\n\n")
    #print(list_contacs)
    
    for str_contact in contacs_list:
        lst_contact = str_contact.replace(":", "").split()
        if search in lst_contact[i_var]:
            print(f"{str_contact} успешно скопирован!\n")
    with open(f"copy.txt", "a", encoding="utf-8") as copy_file:
        copy_file.write(f"{str_contact}\n\n")

def search_contackt():
    print(
            "Возможнве варианты поиска:\n"
            "1. По фамилии\n"
            "2. По имени\n"
            "3. По отчеству\n"
            "4. По телефону\n"
            "5. По адресу(город)\n"
            )
    var = input("Выберите вариант действия: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("некоректный вод")
        var = input("Выберите вариант поиска:")

        
    i_var = int(var) - 1
        
    search = input("Введите данные для поиска: ").title()
    print()
    with open("phone_book.txt", "r", encoding="utf-8") as file:
        contacs_str = file.read()
    #print([contacts_str])
    contacs_list = contacs_str.rstrip().split("\n\n")
    #print(list_contacs)
    
    for str_contact in contacs_list:
        lst_contact = str_contact.replace(":", "").split()
        if search in lst_contact[i_var]:
            print(f"{str_contact}\n")
            

           
    


def interfeice():
    with open("phone_book.txt", "a", encoding="utf-8"):
        pass
    
    var = 0
    while var != "5":
        print(
            "Возможнве варианты действий:\n"
            "1. Добавить контакт\n"
            "2. Вывести на экран\n"
            "3. Поиск контакта\n"
            "4. Копировать контакт\n"
            "5. Выход\n"
            )
        
        var = input("Выберите вариант действия: ")
        while var not in ("1", "2", "3", "4", "5"):
            print("некоректный вод\n")
            var = input("Выберите вариант действия: ")
            print()
            
        match var:
            case "1":
                add_contactk()
            case "2":
                print_contacts()
            case "3":
                search_contackt()
            case "4":
                copy_contact()
            case "5":
                print("Good bye!")
                



if __name__ == "__main__":
    interfeice()
    
    