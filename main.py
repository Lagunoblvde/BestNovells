import os
import time
import json
import csv

def sohranenie():
    name = input()
    age = input()
    data = {
        "name":name,
        "age":age
    }
    with open('sohran.json', 'w', encoding="utf-8-sig") as file:
        json.dump(data, file, indent=4)
    with open("sohran.csv", "a", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age])

def load():
    global name
    global age
    with open("sohran.json", "r", encoding="utf-8-sig") as file:
        data = json.load(file)
        name = data["name"]
        age = data["age"]

def out_blue(text):
    print("\033[34m{}".format(text))


def out_green(text):
    print("\033[32m{}".format(text))


def out_red(text):
    print("\033[31m{}".format(text))


def out_white(text):
    print("\033[37m{}".format(text))


def out_yellow(text):
    print("\033[33m{}".format(text))

def tx(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()
global name
global age
global Exp
global Nazvanie
Nazvanie = "\"Судьбоносная встреча\""
names = ["1. Блогер", "2. Мэр Нижнеподкопайска", "3. Одинокий мальчик - гений", "4. Учёный из будущего",
         "5. Путешественник из Африки"]  # Список

names_2 = {
    1: "1. Блогер",
    2: "2. Мэр Нижнеподкопайска",
    3: "3. Одинокий мальчик гений",
    4: "4. Учёный из будущего",
    5: "5. Путешественник из Африки"
}  #Словарь
names_3 = {"1. Блогер", "2. Мэр Нижнеподкопайска", "3. Одинокий мальчик - гений",
           "4. Учёный из будущего", "5. Путешественник из Африки"}  # Множества

def command_menu():
    print("Введите команду")
    vibor = input()
    if vibor == 'lvlup':
        main_menu2()
    elif vibor == 'autors':
        out_blue("----------------------------------------")
        out_white(f"Над Новеллой {Nazvanie} работали:")
        print("")
        out_yellow("Создание и оформление:")
        out_white("Иванов Владислав")
        print("")
        out_yellow("Человек, без которого бы ничего не получилось:")
        out_white("Григоренко Надежда")
        print("")
        out_yellow("Создание сюжета:")
        out_white("Артемюк Илья\nВоробьёв Михаил\nИванова Юлия\nМурашов Тимофей\nШеметов Ярослав")
        main_menu()
    elif vibor == 'delete users':
        delete_users()

def delete_users():
    os.remove("sohran.json")
    os.remove("sohran.csv")
    print("Пользователи удалены.")
    main_menu()
def sohran_menu():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Выберите главу, на которой остановились")
            out_blue("----------------------------------------")
            out_red("1. Глава 1 ")
            print("2. Глава 2 ")
            print("3. Глава 3 ")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            sujet()
            break
        elif vibor == 2:
            sujet4()
            break
        elif vibor == 3:
            print("")
            break

def main_menu():
    while True:
        try:
            out_blue("----------------------------------------")
            out_red(f"Новела {Nazvanie}")
            out_blue("----------------------------------------")
            out_white("Выберите действие:")
            print("1. Играть")
            print("2. Вернуться в игру")
            print("3. Посмотреть истории персонажей")
            print("4. Системные команды")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            sujet()
            break
        elif vibor == 2:
            sohran_menu()
            break
        elif vibor == 3:
            vibor_EXP()
            break
        elif vibor == 4:
            command_menu()
            break

def main_menu2():
    while True:
        try:
            out_blue("----------------------------------------")
            out_red(f"Новелла {Nazvanie}")
            out_blue("----------------------------------------")
            out_white("Выберите действие:")
            print("1. Играть")
            print("2. Посмотреть истории персонажей")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            sujet()
            break
        elif vibor == 2:
            vibor_EXP2()
            break

def vibor_EXP():

    Exp = 1

    if Exp == 1:
        menu_vibor()

    elif Exp == 2:
        menu_vibor2()

    elif Exp == 3:
        menu_vibor3()

def vibor_EXP2():

    Exp = 3

    if Exp == 1:
        menu_vibor()

    elif Exp == 2:
        menu_vibor2()

    elif Exp == 3:
        menu_vibor3()

def sujet():
    while True:
        try:
            out_blue("----------------------------------------")
            out_red("Глава 1")
            out_blue("----------------------------------------")
            out_white("")
            tx("17 марта 2020 года нашего героя пригласили на вручение Нобелевской премии, так как его отец дружит с организатором награждения.")
            tx("Проснувшись рано утром, юный блогер подбирает наряд на вручение.")
            print("")
            out_blue("----------------------------------------")
            print("Выберите одежду:")
            out_green("1. Обычный наряд (Красная толстовка, джинсы и белые кроссовки), в котором он обычно снимает свои видео.")
            out_yellow("2. Праздничный прикид (Дорогой костюм, который ему купил отец), для особых случаев.")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы надели свою рабочую форму, в ней вам будет комфортно, а также вас будет легче узнать")
            print("")
            sujet1()
            break
        elif vibor == 2:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы надели дорогущий костюм, теперь отцу не будет стыдно за вас, но снимать в нём будет неудобно")
            print("")
            sujet1()
            break

def sujet1():
    out_blue("----------------------------------------")
    out_white("")
    tx("После того, как вы оделись, вы отправились на вручение. Отец рассказал, что в этом году оно будет особенным, так как премию получат мальчик.")
    tx("Впервые такую серьёзную награду вручают юному парню, который всю жизнь посвятил своему проекту - вечному двигателю")
    tx("Добравшись до места вручения, вы встретился взглядом с невзрачным и отречённым мальчишкой.")
    tx("У вас сложилось впечатление, что мальчику было некомфортно, будто бы он не желал здесь находиться.")
    tx("Вы решили сделать вид, что не заметили его и прошли мимо. Спустя 40 минут долгожданно вручение премии наконец-то началось.")
    tx("После не особо длительного вступения ведущий наконец-то позвал на вручение главного гостя - Одинокого гения.")
    tx("Какого же было Ваше удивление, когда на сцену вышел тот самый невзрачный и отречённый мальчик.")
    tx("Во время того, как он рассказывал про своё открытие, у него сильно тряслись руки и голос.")
    tx("Всем было сразу понятно, что мальчик не привык к общению с людьми. Вдруг крыша зала провалилась, благо никто никто не пострадал.")
    tx("Вместе с обломками крыши свалился какой-то незнакомец.")
    print("")
    while True:
        try:
            out_blue("----------------------------------------")
            out_blue("Выберите действие:")
            out_green("1. Подбежать и помочь незнакомцу.")
            out_yellow("2. Крикнуть, в порядке ли свалившийся с неба человек.")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы подбежали, но не успели спросить, так как пострадавший встал, отряхнулся и поднялся на сцену.")
            print("")
            sujet2()
            break
        elif vibor == 2:
            out_blue("----------------------------------------")
            out_white("")
            tx("Крикнув ему, Вы не услышали ответа. Вместо этого он встал и поднялся на сцену.")
            print("")
            sujet2()
            break

def sujet2():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("")
            tx("Незнакомец забрал микрофон у мальчика и приедставился учёным из будущего, у которого есть немного времени, чтобы рассказать все секреты, которые он знает.")
            print("")
            out_blue("----------------------------------------")
            out_green("Открыт новый персонаж - \"Учёный из будущего\".")
            out_blue("----------------------------------------")
            print("Хотите прочитать его историю?")
            out_white("1. Хочу")
            print("2. Продолжить играть")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            menu_vibor2()
            break
        elif vibor == 2:
            sujet3()
            break


def sujet3():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("")
            tx("Ему не поверили и посчитали безумцем, охрана схватила его и вывела из здания, где проводилось вручение.")
            tx(
                "Когда все гости пришли в себя, мальчика, которому должна была вручаться премия на сцене уже не было, как и Вас")
            tx("Вы отправились на улицу, чтобы найти этого учёного из будущего. по дороге Вы встретили Одинокого гения.")
            tx("Вы спросили его, почему он ушёл со сцены, не дождавшись концца награждения.")
            tx("Он ответил вам, что хочет разузнать у Учёного, пригодилось ли его изобретение. Вы решили объединиться и найти его.")
            tx("Выйдя на улицу, вы увидели человека, который собрал вокруг себя толпу, он пытался убедить их в своей правоте")
            tx("Вы сразу поняли, что это тот, кто вам нужен.")
            tx("Подобравшись поближе, вы схватили его за руку и увели подальше от толпы.")
            tx("Вы попросили Учёного как-нибудь доказать вам, что он из будущего. Он указал на на мальчика, стоящего рядом.")
            tx("Незнакомец рассказал, что его изобретение продвинуло всю науку, и даже спустя огромное время оно всё ещё используется.")
            tx("Также он упомянул влиятельную личность - Мэра Нижнеподкопайска, который выкупил патент на изобретение молодого гения.")
            tx("О самом же мальчике ничего не известно, он пропал после награждения.")
            tx("Смогут ли новые друзья изменить будущее?")
            out_blue("----------------------------------------")
            out_white("1. Продолжить играть")
            print("2. Выйти из игры")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            sujet4()
            break
        elif vibor == 2:
            out_blue("----------------------------------------")
            out_white("Введите своё игровое имя и возраст")
            sohranenie()
            out_blue("----------------------------------------")
            out_red("Возвращайтесь, чтобы пройти все главы! До свидания!")
            break

def sujet4():
    while True:
        try:
            out_blue("----------------------------------------")
            out_red("Глава 2")
            out_blue("----------------------------------------")
            out_white("")
            tx("Рассказав всё, что Учёный знает, друзья решили не допустить кражи патента открытия мальчика.")
            tx("Для этого им нужно было найти самого Мэра Нижнеподкопайска, тогда они смогли бы убедить его не выкупать права на проект,")
            tx("Ведь только Учёный знал, что мир, в котором Мэр заполучил власть, погряз в корупции и лжи.")
            tx("Также, он сказал, что видел злодея на награждении, он сильно заинтересовался проектом, значит, его можно найти, пока он не уехол в Нижнеподкопайск.")
            tx("Собравшись с мыслями, они выдвинулись на место проведения вручения. ")
            tx("На этом месте собрались правоохранительные органы, чтобы найти преступника, который разрушил здание, проломив крышу.")
            out_blue("----------------------------------------")
            out_white("Что вы предпримите?")
            out_green("1. Предложите обойти полицию.")
            out_yellow("2. Попробуйте в неразберихе найти Мэра Нижнеподкопайска.")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            sujet5()
            break
        elif vibor == 2:
            sujet5()
            break

def sujet5():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("")
            tx("Решив, что будет опасно лишний раз показываться на людях, Вы решили обойти полицию и отправится в отель неподалёку, там, возможно, будет Мэр Нижнеподкопайска.")
            tx("Одинокий мальчик предложил договориться с ним, так как подкупить или переубедить у них вряд ли получится.")
            tx("Войдя в отель, Вы спросили, где находится Мэр, вам назвали номер")
            out_blue("----------------------------------------")
            out_white("Что выберите?")
            print("")
            print("")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue


def istoriya_Bloger():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Характеристики:")
            out_blue("Интелект: 10\nСила: 10\nУниверсальность: 100")
            out_white("Особенности:")
            out_red("Главный герой")
            out_blue("----------------------------------------")
            out_white("")
            tx("Добродушный парень, выросший в обеспеченной семье. Он мечтает стать известным и помогать людям.")
            tx("Для этого он создал свой блог, в котором выкладывает интересные и смешные ролики.")
            tx("Ему удаётся завести новых друзей и создать невероятную историю")
            out_blue("----------------------------------------")
            out_white("1. Вернуться в главное меню.")
            print("2. Продолжить играть")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            main_menu()
            break
        elif vibor == 2:
            print("")
            break

def istoriya_Mer():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Характеристики:")
            out_blue("Интелект: 30\nСила: 10\nУниверсальность: 20")
            out_white("Особенности:")
            out_red("Владеет Нижнеподкопайском")
            out_blue("----------------------------------------")
            out_white("")
            tx("Мэр Нижнеподкопайска - скрытная личность, которая имеет большую власть, чем кажется.")
            tx("Заядлый корупционер, который не скрывает, что ведёт незаконную деятельность.")
            tx("Неосознанно начал общаться с юным Блогером и решил, что сможет прославиться на весь мир, благодаря ему.")
            out_blue("----------------------------------------")
            out_white("1. Вернуться в главное меню.")
            print("2. Продолжить играть")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            main_menu()
            break
        elif vibor == 2:
            print("")
            break

def istoriya_Odinokiy():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Характеристики:")
            out_blue("Интелект: 100\nСила: 10\nУниверсальность: 30")
            out_white("Особенности:")
            out_red("Кандидат Нобелевской премии")
            out_blue("----------------------------------------")
            out_white("")
            tx("Одинокий мальчик, который с детства не имел друзей посвятил всего себя учёбе.")
            tx("Спустя время он добился успеха - смог изобрести вечный двигатель в столь юном возрасте.")
            tx(
                "Его заметили и оценили. Он стал кандидатом Нобелевской премии, а на награждении встретил главного героя, где с ним и познакомился.")
            out_blue("----------------------------------------")
            out_white("1. Вернуться в главное меню.")
            print("2. Продолжить играть")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            main_menu()
            break
        elif vibor == 2:
            print("")
            break

def istoriya_Genii():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Характеристики:")
            out_blue("Интелект: 80\nСила: 10\nУниверсальность: 100")
            out_white("Особенности:")
            out_red("Прибыл из будущего")
            out_blue("----------------------------------------")
            out_white("")
            tx("Учёный, прилетевший из будущего, у него есть немного времени, чтобы рассказать всё, что ждёт человечество спустя время.")
            tx("Это время он решил посвятить Главному герою и его друзьям. Ведь в них он видит будущее всего мира.")
            tx("Успеет ли он рассказать всё, что знает, и исправить ошибки, которые допустил раньше?")
            out_blue("----------------------------------------")
            out_white("1. Вернуться в главное меню.")
            print("2. Продолжить играть")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            main_menu2()
            break
        elif vibor == 2:
            print("")
            break



def istoriya_Afrika():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Характеристики:")
            out_blue("Интелект: 10\nСила: 100\nУниверсальность: 30")
            out_white("Особенности:")
            out_red("У него очень большая семья, очень, он даже не помнит их имена.")
            out_blue("----------------------------------------")
            out_white("")
            tx("Путешественник, который родился и вырос в Африке, мечтает побывать в Сибире.")
            tx("На протяжении всей жизни он слышал лишь истории о земле, где есть белый и холодный снег, но никогда её не видел")
            tx("Он сделает всё, чтобы осуществить свою семью, а помогут ему в этом Главный герой и его новые друзья.")
            out_blue("----------------------------------------")
            out_white("1. Вернуться в главное меню.")
            print("2. Продолжить играть")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            main_menu2()
            break
        elif vibor == 2:
            print("")
            break
def oshibka():
    while True:
        try:
            out_red("----------------------------------------")
            print("Эта история ещё закрыта, повысьте свой уровень, чтобы узнать о новых персонажах")
            print("----------------------------------------")
            out_white("1. Вернуться в главное меню.")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            main_menu()
            break

def menu_vibor():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Выберите персонажа, историю которого хотели бы узнать:")
            print("1. Блогер")
            print("2. Мэр Нижнеподкопайска")
            print("3. Одинокий мальчик - гений")
            out_red("4. Учёный из будущего: Закрыто")
            out_red("5. Путешественник из Африки: Закрыто")
            out_blue("----------------------------------------")
            out_white("6. Вернуться в главное меню")
            out_blue("----------------------------------------")

            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого дейтвия не существует")
            continue
        if vibor == 1:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы выбрали Вашего персонажа. Весёлого блогера, который попал в необычною историю, не планировав ничего подобного.")
            istoriya_Bloger()
            break
        elif vibor == 2:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать историю Мэра Подкопайска, о нём почти ничего не известно. Вот что мы смогли узнать о нём:")
            istoriya_Mer()
            break
        elif vibor == 3:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать историю Одинокого гения. Мальчик, который за короткий промежуток времени смог удивить весь мир")
            istoriya_Odinokiy()
        elif vibor == 4:
            oshibka()
            break
        elif vibor == 5:
            oshibka()
            break
        elif vibor == 6:
            main_menu()
            break
def menu_vibor2():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Выберите персонажа, историю которого хотели бы узнать:")
            print("1. Блогер")
            print("2. Мэр Нижнеподкопайска")
            print("3. Одинокий мальчик - гений")
            print("4. Учёный из будущего")
            out_red("5. Путешественник из Африки: Закрыто")
            out_blue("----------------------------------------")
            out_white("6. Вернуться в главное меню")
            out_blue("----------------------------------------")

            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы выбрали Вашего персонажа. Весёлого блогера, который попал в необычною историю, не планировав ничего подобного.")
            istoriya_Bloger()
            break
        elif vibor == 2:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать историю Мэра Подкопайска, о нём почти ничего не известно. "
                      "Вот что мы смогли узнать о нём:")
            istoriya_Mer()
            break
        elif vibor == 3:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать историю Одинокого гения. Мальчик, который за короткий промежуток времени смог удивить весь мир")
            istoriya_Odinokiy()
            break
        elif vibor == 4:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать будущее, или узнать о человеке из будущего? Это история Учёного, которая возможно ответит на ваши вопросы.")
            istoriya_Genii()
            break
        elif vibor == 5:
            oshibka()
            break
        elif vibor == 6:
            main_menu()
            break
def menu_vibor3():
    while True:
        try:
            out_blue("----------------------------------------")
            out_white("Выберите персонажа, историю которого хотели бы узнать:")
            print("1. Блогер")
            print("2. Мэр Нижнеподкопайска")
            print("3. Одинокий мальчик - гений")
            print("4. Учёный из будущего")
            print("5. Путешественник из Африки")
            out_blue("----------------------------------------")
            out_white("6. Вернуться в главное меню")
            out_blue("----------------------------------------")
            vibor = int(input())
        except ValueError:
            out_blue("----------------------------------------")
            out_red("Такого действия не существует")
            continue
        if vibor == 1:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы выбрали Вашего персонажа. Весёлого блогера, который попал в необычною историю, не планировав ничего подобного.")
            istoriya_Bloger()
            break
        elif vibor == 2:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать историю Мэра Подкопайска, о нём почти ничего не известно. Вот что мы смогли узнать о нём:")
            istoriya_Mer()
            break
        elif vibor == 3:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать историю Одинокого гения. Мальчик, который за короткий промежуток времени смог удивить весь мир")
            istoriya_Odinokiy()
            break
        elif vibor == 4:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать будущее, или узнать о человеке из будущего? Это история Учёного, которая возможно ответит на ваши вопросы.")
            istoriya_Genii()
            break
        elif vibor == 5:
            out_blue("----------------------------------------")
            out_white("")
            tx("Вы хотите узнать о Путешественнике из Африки. В мире бывают случаи, когда мечта может перекрыть всю остальную жизнь.")
            istoriya_Afrika()
            break
        elif vibor == 6:
            main_menu()
            break

main_menu()
