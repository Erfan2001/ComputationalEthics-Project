from scenarios import mendacity, libel, false_negative_rumor, false_positive_rumor


def main():

    while True:
        print('press e to exit')
        print('1: mendacity \n2: libel \n3: false_negative_rumor \n4: false_positive_rumor')
        a = input('which scenario do you want?(1,2,3,4)')

        if a == 'e':
            break
        
        a = int(a)

        if a == 1:
            mendacity()

        elif a == 2:
            libel()

        elif a == 3:
            false_negative_rumor()

        elif a == 4:
            false_positive_rumor()


if __name__ == '__main__':
    main()