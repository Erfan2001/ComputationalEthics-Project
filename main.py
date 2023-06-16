from scenarios import mendacity, libel, false_negative_rumor, false_positive_rumor


def main():

    while True:
        print('press e to exit')
        print('1: mendacity \n 2: libel \n 3: false_negative_rumor \n 4: false_positive_rumor')
        a = input('which scenario do you want?(1,2,3,4,5,6,7)')

        if a == 'e':
            break
        
        a = int(a)

        if a == 1:

            print('the best action for the mendacity scenario is : ' + mendacity())
            print('\n\n')

        elif a == 2:

            print('the best action for the libel scenario is : ' + libel())
            print('\n\n')

        elif a == 3:

            print('the best action for the false_negative_rumor scenario is : ' + false_negative_rumor())
            print('\n\n')

        elif a == 4:

            print('the best action for the false_positive_rumor scenario is : ' + false_positive_rumor())
            print('\n\n')

if __name__ == '__main__':
    main()