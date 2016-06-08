def suit(data):
    win = ""
    for a in data:
        if a['player1'] == a['player2']:
            win = "Permainan Seri"

        if a['player1'] == "gunting":
            if a['player2'] == "batu":
                win = a['player2']

            if a['player2'] == "kertas":
                win = a['player1']

        if a['player1'] == "batu":
            if a['player2'] == "gunting":
                win = a['player1']

            if a['player2'] == "kertas":
                win = a['player2']

        if a['player1'] == "kertas":
            if a['player2'] == "gunting":
                win = a['player2']

            if a['player2'] == "batu":
                win = a['player1']

        print "menang: ", win

player1 = raw_input("Masukkan player 1: ")
player2 = raw_input("Masukkan player 2: ")
data=[{"player1": player1, "player2": player2}]
suit(data)
