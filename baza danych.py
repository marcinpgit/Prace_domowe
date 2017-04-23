# baza kontaktów
# jeszcze nad nią pracuję - nie pokazuje że imię itp. jest już dodane oraz pracuję
# nad usunięciem elementu - ew. będę wdzięczny za wskazówki

choice = None
baza = []

while choice != "0":
    print("""
    \tBAZA DANYCH\n
    ------------------------------
    1 - dodaj nowy kontakt do bazy
    2 - wyświetl bazę danych
    3 - usuń kontakt z bazy danych
    0 - wyjście z programu
    ------------------------------
    """)

    choice = input("Wybierz opcję: ")

    if choice == "0":
        print("Wyjście z programu")

    elif choice =="1":
        print("\nWybrałeś opcję dodania kontaktu do bazy.")

        imie = input(("Podaj imię do dodania do bazy: "))
        if imie in baza:
            print("Podane imię już istnieje!!!")

        nazwisko = input(("Podaj nazwisko do dodania do bazy: "))
        if nazwisko in baza:
            print("Podane nazwisko już istnieje!!!")

        telefon = input(("Podaj numer telefonu do dodania do bazy: "))
        if telefon in baza:
            print("Podany numer telefonu już istnieje!!!")
        miasto = input(("Podaj miasto do dodania do bazy: "))

        if miasto in baza:
            print("Podane miasto już istnieje!!!")

        imie = imie.capitalize()
        nazwisko = nazwisko.capitalize()
        miasto = miasto.capitalize()
        # wpis = [imie, nazwisko, telefon, miasto]
        baza.append(imie)
        baza.append(nazwisko)
        baza.append(telefon)
        baza.append(miasto)
        # wpis = (imie, nazwisko, telefon, miasto)
        # baza.append(wpis)


    elif choice == "2":
        print("\nPoniżej Twoja baza danych:\n")
        for i in baza:
            print(i)

# pracuje jeszcze nad opcją 3
    elif choice == "3":
        imie1 = input("Podaj imię do usunięcia: ")
        if imie1 == imie:
            del baza[]


    else:
        print("Niestety ", choice, " nie jest prawidłowym wyborem.")

