def read_gold():
    gold_file = open('gold.csv', "r")

    user = []
    user_gold = []

    for line in gold_file:
        user.append(line.split(';')[0])
        user_gold.append(int(line.split(';')[1]))

    gold_file.close()

    gold_table = [user, user_gold]
    return gold_table


def user_exist(username):
    for user_tb in read_gold()[0]:
        if user_tb == username:
            return True
    return False


def write_gold(username):
    index = -1
    gold_table = read_gold()

    if user_exist(username):
        gold_file = open('gold.csv', "w")

        while gold_table[0][index] != username:
            index += 1
        gold_table[1][index] += 1

        for line in range(len(gold_table[0])):
            gold_file.write(f'{gold_table[0][line]};{gold_table[1][line]}\n')

    else:
        gold_file = open('gold.csv', "a")
        gold_file.write(f'{username};1\n')
        gold_file.close()
    return


def total_gold():
    gold = 0
    gold_table = read_gold()
    for i in gold_table[1]:
        gold += i

    return gold


def get_user_gold(user):
    userlist = read_gold()[0]
    for i in range(len(userlist)):
        if user == userlist[i]:
            user_gold = read_gold()[1][i]

    return user_gold


def sortSecond(val):
    return val[1]


def get_score():
    scoreboard = []
    userlist = read_gold()[0]
    user_gold = read_gold()[1]
    for user in range(len(userlist)):
        scoreboard.append((userlist[user], user_gold[user]))
    scoreboard.sort(key=sortSecond, reverse=True)

    return scoreboard


