# from apples_db import add_to_db, query_db

# add_to_db('phrase', phrase='Hello this is a test as well', playername='Carissa')
# for p in query_db('phrase', playername='Carissa'):
#     print(f'Phrase: {p.phrase}\nUser: {p.playername}')

with open('./requirements.txt', 'r') as r:
    with open('./requirements_2.txt', 'w') as w:
        s = r.readline().split()
        while len(s) > 0:
            l = s[0]+'=='+s[1]+'\n'
            w.write(l)
            s = r.readline().split()


        