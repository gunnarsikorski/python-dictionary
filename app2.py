import mysql.connector

connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student", 
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = connection.cursor()

user_input = input('Please enter a word: ')

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % user_input)
results = cursor.fetchall()

if results:
    for result in results:
        print(f'{user_input}: {result[1]}')
else:
    print('No word found')


# Another fun library to explore a bit - the mySQL connector.
# This one uses a mySQL DB instead of a JSON file for the dictionary data, very similar to a connection
# snippet of code for Postgres.
