import sys
output = open("output.txt", mode="w", encoding="utf-8")
with open(sys.argv[1], mode="r", encoding="utf-8") as smn:
    a = smn.read().replace("\n", ":")
    a = a.split(":")
    d = {}
    for i in range(len(a)):
        if i % 2 == 0:
            d[a[i]] = list(a[i+1].split(" "))

    ### COMMAND TO NESTED LIST
    commands = []
    with open(sys.argv[2]) as inputs:
        for a in inputs.read().splitlines():
            commands.append(a.split())
    k = 0

    ### ANU
    def add_new_user():
        global k
        if commands[k][1] not in d.keys():
            d[commands[k][1]] = []
            output.write("User {} has been added to the social network successfully\n".format(commands[k][1]))
            k += 1
        elif commands[k][1] in d.keys():
            output.write("ERROR: Wrong input type! for 'ANU’! -- This user already exists!!\n")
            k += 1

    ### DEU
    def delete_existing_user():
        global k
        if commands[k][1] not in d.keys():
            output.write("ERROR: Wrong input type! for 'DEU'!--There is no user named {}!!\n".format(commands[k][1]))
            k += 1
        elif commands[k][1] in d.keys():
            for i in d.values():
                if commands[k][1] in i:
                    i.remove(commands[k][1])
            d.pop(commands[k][1])
            output.write("User {} and his/her all relations have been deleted successfully\n".format(commands[k][1]))
            k += 1

       ### ANF
    def add_new_friend():
        global k
        if commands[k][1] in d.keys():
            for i in d.values():
                if d[commands[k][1]] == i:
                    if commands[k][2] not in i:
                        i.append(commands[k][2])
                        output.write("Relation between {} and {} has been added successfully\n".format(commands[k][1],commands[k][2]))
                        for o in d.values():
                            if d[commands[k][2]] == o:
                                o.append(commands[k][1])

                    if commands[k][2] in i:
                        output.write("“ERROR: A relation between {} and {} already exists!!\n".format(commands[k][1],commands[k][2]))
            k+=1

        elif commands[k][1] not in d.keys() and commands[k][2] in d.keys():
            output.write("ERROR: Wrong input type! for 'ANF'! -- No user named {} found!!\n".format(commands[k][1]))
            k += 1
        elif commands[k][2] not in d.keys() and commands[k][1] in d.keys():
            output.write("ERROR: Wrong input type! for 'ANF'! -- No user named {} found!!\n".format(commands[k][2]))
            k += 1
        elif commands[k][1] not in d.keys() and commands[k][2] not in d.keys():
            output.write(
                "ERROR: Wrong input type! for 'ANF'! -- No user named {} and {} found!!\n".format(commands[k][1],
                                                                                                  commands[k][2]))
            k += 1

    ### DEF
    def delete_existing_friend():
        global k
        if commands[k][1] in d.keys() and commands[k][2] in d.keys():
            for i in d.values():
                if d[commands[k][1]] == i:
                    if commands[k][2] in i:
                        i.remove(commands[k][2])
                        output.write("Relation between {} and {} has been deleted successfully\n".format(commands[k][1],
                                                                                                         commands[k][
                                                                                                             2]))
                    if commands[k][2] not in i:
                        output.write(
                            "ERROR: No relation between {} and {} found!!\n".format(commands[k][1], commands[k][2]))
                if d[commands[k][2]] == i:
                    if commands[k][1] in i:
                        i.remove(commands[k][1])
            k += 1
        elif commands[k][1] not in d.keys() and commands[k][2] in d.keys():
            output.write("“ERROR: Wrong input type! for 'DEF'! -- No user named {} found!\n".format(commands[k][1]))
            k += 1
        elif commands[k][2] not in d.keys() and commands[k][1] in d.keys():
            output.write("ERROR: Wrong input type! for 'DEF'! -- No user named {} found!\n".format(commands[k][2]))
            k += 1
        elif commands[k][1] not in d.keys() and commands[k][2] not in d.keys():
            output.write(
                "“ERROR: Wrong input type! for 'DEF'! -- No user named {} and {} found!\n".format(commands[k][1],
                                                                                                  commands[k][2]))
            k += 1

    ### CF
    def count_friend():
        global k
        if commands[k][1] in d.keys():
            output.write("User {} has {} friends\n".format(commands[k][1], len(d[commands[k][1]])))

        if commands[k][1] not in d.keys():
            output.write("“ERROR: Wrong input type! for 'CF'! -- No user named {} found!\n".format(commands[k][1]))
        k += 1


    ### FPF
    def find_possible_friends():
        global k
        list_1, list_2, list_3 = list(), list(), list()
        distance = commands[k][2]

        if commands[k][1] in d.keys():

            if distance == "1":
                for i in d[commands[k][1]]:
                    list_1.append(i)
                a = set(list_1)
                x = str(sorted(a))
                x = x.replace("[","{")
                x = x.replace("]","}")
                output.write(
                    "User {} has {} possible friends when maximum distance is 1\n".format(commands[k][1], len(a)))
                output.write("These possible friends: {}\n".format(x))

            elif distance == "2":
                for i in d[commands[k][1]]:  # ilk ismin valueleri(arkadaşları)
                    list_2.append(i)
                    for j in d[i]:  # valuedeki isimlerin her birinin valuesi
                        if j != commands[k][1]:
                            list_2.append(j)
                b = set(list_2)
                y = str(sorted(b))
                y = y.replace("[","{")
                y = y.replace("]","}")
                output.write(
                    "User {} has {} possible friends when maximum distance is 2\n".format(commands[k][1], (len(b))))
                output.write("These possible friends: {}\n".format(y.replace("[","{")))

            elif distance == "3":
                for i in d[commands[k][1]]:  # ilk ismin valueleri
                    list_3.append(i)
                    for j in d[i]:  # valuedeki isimlerin her birinin valuesi
                        if j != commands[k][1]:
                            list_3.append(j)
                            for o in d[j]:
                                list_3.append(o)
                list_3 = sorted(list_3)
                del list_3[0]
                c = set(list_3)
                z = str(sorted(c))
                z = z.replace("[","{")
                z = z.replace("]","}")
                output.write("User {} has {} possible friends when maximum distance is 3\n".format(commands[k][1], (len(c)-1)))
                output.write("These possible friends: {}\n".format(z))
            k += 1

        if distance != "1" and distance != "2" and distance != "3":
            output.write("ERROR: Maximum distance is out of range!!\n")
            k +=1

        if commands[k][1] not in d.keys():
            output.write("“ERROR: Wrong input type! for 'FPF'! -- No user named {} found!\n".format(commands[k][1]))
            k += 1

    ### SF
    def suggest_friend():
        global k
        MD = commands[k][2]
        sf_2,sf_3 = list(),list()
        mutual_list = []
        if commands[k][1] in d.keys():
            for first in d[commands[k][1]]:
                for second in d[first]:
                    mutual_list.append(second)
                    if (mutual_list.count(second)) == 2 and second != commands[k][1] :
                        sf_2.append(second)
                        set_sf_2 = set(sorted(sf_2))

                    if (mutual_list.count(second)) == 3 and second != commands[k][1] :
                        sf_3.append(second)
                        sf_2.append(second)
                        set_sf_3 = set(sorted(sf_3))
            if MD == "2":
                output.write("The suggested friends for {} (when MD is 2):\n".format(commands[k][1]))
                for set_2 in sf_2:
                    if set_2 in sf_2 and set_2 not in sf_3:
                        output.write(" '{}' has 2 mutual  friends with '{}' \n".format(commands[k][1],set_2))
                    else :
                        output.write(" '{}' has 3 mutual  friends with '{}' \n".format(commands[k][1], set_2))

                output.write("Suggestion List for {}: {} \n".format(commands[k][1],set_sf_2))
                k += 1

            if MD == "3":
                output.write("The suggested friends for {} (when MD is 3) :\n".format(commands[k][1]))
                for set_3 in sf_3:
                    if set_3 in sf_2 and set_3 not in sf_3:
                        pass
                    else:
                        output.write(" '{}' has 3 mutual  friends with '{}' \n".format(commands[k][1], set_3))
                output.write("Suggestion List for {} : {}\n".format(commands[k][1],set_sf_3))
                k+=1


            if  MD != "2" and MD != "3" :
                output.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
                k += 1

        if commands[k][1] not in d.keys():
            output.write("Error: Wrong input type! for 'SF'! -- No user named {} found!!\n".format(commands[k][1]))
            k += 1

    ### GETTING INPUT FROM COMMANDS
    for c in commands:
        if commands[k][0] == "ANU":
            add_new_user()
        if commands[k][0] == "DEU":
            delete_existing_user()
        if commands[k][0] == "ANF":
            add_new_friend()
        if commands[k][0] == "DEF":
            delete_existing_friend()
        if commands[k][0] == "CF":
            count_friend()
        if commands[k][0] == "FPF":
            find_possible_friends()
        if commands[k][0] == "SF":
            suggest_friend()
