from rules import rules

def mendacity():
    
    print("#####################     lie    #################################")

    a1 = 'to lie'
    a2 = 'not to lie'

    c1 = 'the court is right'
    c2 = 'the court is wrong'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 6:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        return a1
    else:
        return a2

def libel():
    
    
    print("#####################     libel    #################################")

    a1 = 'right testimony'
    a2 = 'wrong testimony'

    c1 = 'the court is right'
    c2 = 'the court is wrong'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]


                elif i == 8:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 4:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 8:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        return a1
    else:
        return a2

def false_positive_rumor():

 
    print("#####################     false positive rumor    #################################")

    a1 = 'wrong testimony'
    a2 = 'right testimony'

    c1 = 'the court is wrong'
    c2 = 'the court is right'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]

                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]

                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                
                elif i == 11:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]
                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        return a1
    else:
        return a2

def false_negative_rumor():
 
    print("#####################     false negative rumor    #################################")

    a1 = 'wrong testimony'
    a2 = 'right testimony'

    c1 = 'the court is wrong'
    c2 = 'the court is right'


    actions = (a1, a2)
    consequence = (c1, c2)

    equation = {a1: c1, a2: c2}

    def utility(action):
        u = 0
        for i in range(1,len(rules)+1):
            if action == a1:

                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]


                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u -= rules[i-1][1]

                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')



            elif action == a2:
                if i == 3:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]

                elif i == 7:
                    print(rules[i-1][0])
                    print(f'according to this rule the utility of this action will be +{rules[i-1][1]}')
                    u += rules[i-1][1]

                    
                else:
                    print(f'{rules[i-1][0]} does not apply for this scenario')

        return u
    
    print("################### action 1 ###################\n")
    u1 = utility(a1)
    print(f'the utility for action 1 will be {u1}')

    print("################### action 2 ###################\n")
    u2  = utility(a2)
    print(f'the utility for action 2 will be {u2}')


    if u1 >= u2:
        return a1
    else:
        return a2


