def bioskop(film, data):
    for a in data:
        for b in film:
            if a['umur'] >= b['age']:
                watch = {"nama":"", "film":[]}
                watch['nama'].append(a['nama'])
                watch['film'].append(b['nama'])

    print film
    print data
    print watch

film = [{"nama": "Deadpol", "age":17}, {"nama": "AADC2", "age":17},
        {"nama": "My Stupid Boss", "age":0}, {"nama": "Traffic", "age":13},
        {"nama":"Teenage Mutan Ninja Turtles", "age":13}]
data = [{"nama": "Budi", "umur": 25}, {"nama": "Lauri", "umur": 18},
        {"nama": "Anton", "umur": 12}, {"nama": "Hamzah", "umur": 15},
        {"nama": "Budi", "umur": 25}, {"nama": "Budi", "umur": 25}]

bioskop(film, data)
