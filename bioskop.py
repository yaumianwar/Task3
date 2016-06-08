def bioskop(film, data):
    for a in data:
        for b in film:
            if a['umur'] >= b['age']:
                a['film'].append(b['nama'])

    print film
    print data


film = [{"nama": "Deadpol", "age":17}, {"nama": "AADC2", "age":17},
        {"nama": "My Stupid Boss", "age":0}, {"nama": "Traffic", "age":13},
        {"nama":"Teenage Mutan Ninja Turtles", "age":13}]
data = [{"nama": "Budi", "umur": 25, "film":[]}, {"nama": "Lauri", "umur": 18, "film":[]},
        {"nama": "Anton", "umur": 12, "film":[]}, {"nama": "Hamzah", "umur": 15, "film":[]},
        {"nama": "Indra", "umur": 17, "film":[]}]

bioskop(film, data)
