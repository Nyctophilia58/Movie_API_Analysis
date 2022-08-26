import requests
import csv
import json
from keys import api_key


def request_data():
    with open('oscar_winners.csv', newline='') as oscar_winners_csv:
        oscar_winners = csv.reader(oscar_winners_csv, delimiter=',')
        next(oscar_winners)
        rows = list(oscar_winners)
        header = ['Movie Title', 'Runtime', 'Genre', 'Award wins', 'Award nominations', 'Box Office']
        with open('movies.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for row in rows:
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


request_data()
