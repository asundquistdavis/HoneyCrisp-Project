from apples_db import add_to_db, query_db

add_to_db('phrase', phrase='Hello this is a test as well', playername='Carissa')
for p in query_db('phrase', playername='Carissa'):
    print(f'Phrase: {p.phrase}\nUser: {p.playername}')


