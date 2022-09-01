import requests
import csv
from keys import api_key
import datetime


def request_data():
    with open('oscar_winners.csv', newline='') as oscar_winners_csv:
        oscar_winners = csv.reader(oscar_winners_csv, delimiter=',')
        next(oscar_winners)
        rows = list(oscar_winners)
        header = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office']
        with open('movies.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for row in rows[:10]:
                movie_id = row[1]
                url = f'http://www.omdbapi.com/?i={movie_id}&apikey={api_key}'
                response = requests.get(url)
                data = response.json()
                movie_title = data['Title']
                runtime = int(data['Runtime'].rstrip(' min'))
                genre = data['Genre']
                award_wins = int(data['Awards'].split(' ')[1]) + int(data['Awards'].split(' ')[3])
                award_nominations = int(data['Awards'].split(' ')[6])
                box_office = data['BoxOffice'].lstrip('$')
                box_office = int(box_office.replace(',', ''))
                info = [movie_title, runtime, genre, award_wins, award_nominations, box_office]
                writer.writerow(info)


def add_five_movies():
    with open('oscar_winners.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['Titanic', 'tt0120338'])
        writer.writerow(['The Lord of the Rings: The Return of the King', 'tt0167260'])
        writer.writerow(['La La Land', 'tt3783958'])
        writer.writerow(['Forrest Gump', 'tt0109830'])
        writer.writerow(['My Fair Lady', 'tt0058385'])


# def add_data_of_new_movies():
#     with open('oscar_winners.csv', newline='') as oscar_winners_csv:
#         oscar_winners = csv.reader(oscar_winners_csv, delimiter=',')
#         next(oscar_winners)
#         rows = list(oscar_winners)
#         with open('movies.csv', 'a') as f:
#             writer = csv.writer(f)
#             for row in rows[10:]:
#                 movie_id = row[1]
#                 url = f'http://www.omdbapi.com/?i={movie_id}&apikey={api_key}'
#                 response = requests.get(url)
#                 data = response.json()
#                 movie_title = data['Title']
#                 runtime = int(data['Runtime'].rstrip(' min'))
#                 genre = data['Genre']
#                 award_wins = int(data['Awards'].split(' ')[1]) + int(data['Awards'].split(' ')[3])
#                 award_nominations = int(data['Awards'].split(' ')[6])
#                 box_office = data['BoxOffice'].lstrip('$')
#                 box_office = int(box_office.replace(',', ''))
#                 info = [movie_title, runtime, genre, award_wins, award_nominations, box_office]
#                 writer.writerow(info)


def add_additional_columns():
    with open('oscar_winners.csv', newline='') as oscar_winners_csv:
        oscar_winners = csv.reader(oscar_winners_csv, delimiter=',')
        next(oscar_winners)
        rows = list(oscar_winners)
        header = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations',
                  'Box Office', 'Rated', 'Director', 'Released']
        with open('movies.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for row in rows[:]:
                movie_id = row[1]
                url = f'http://www.omdbapi.com/?i={movie_id}&apikey={api_key}'
                response = requests.get(url)
                data = response.json()
                movie_title = data['Title']
                runtime = int(data['Runtime'].rstrip(' min'))
                genre = data['Genre']
                award_wins = int(data['Awards'].split(' ')[1]) + int(data['Awards'].split(' ')[3])
                award_nominations = int(data['Awards'].split(' ')[6])
                box_office = data['BoxOffice'].lstrip('$')
                box_office = int(box_office.replace(',', ''))
                rated = data['Rated']
                director = data['Director']
                released = data['Released']
                info = [movie_title, runtime, genre, award_wins, award_nominations, box_office,
                        rated, director, released]
                writer.writerow(info)


request_data()
# add_five_movies()
# add_data_of_new_movies()
add_additional_columns()
