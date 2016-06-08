

def blabla(data, angkaLess, angkaMore):
    dataMore = []
    dataLess = []
    dataBetween = []
    maks=0
    minim=100
    orangTua = ""
    orangMuda = ""
    for a in data:
        if a['umur'] > angkaMore:
            dataMore.append(a['umur'])

        if a['umur'] < angkaLess:
            dataLess.append(a['umur'])

        if a['umur'] > angkaLess and a['umur'] < angkaMore:
            dataBetween.append(a['umur'])

        if a['umur'] > maks:
            maks = a['umur']
            orangTua = a['name']

        if a['umur'] < minim:
            minim = a['umur']
            orangMuda = a['name']


    print data
    print "Jumlah orang yang berumur lebih dari " + str(angkaMore) + " adalah " + str(len(dataMore))
    print "Jumlah orang yang berumur kurang dari " + str(angkaLess) + " adalah " + str(len(dataLess))
    print "Jumlah orang yang berumur antara " + str(angkaLess) +  " dan " + str(angkaMore) + " adalah " + str(len(dataBetween))
    print "Paling Tua", orangTua
    print "Paling Muda", orangMuda

data = [{"name": "Yaumi", "umur": 19}, {"name": "Ady", "umur": 100}, {"name": "Rudy", "umur": 70},
            {"name": "Indah", "umur": 10}, {"name": "Ichal", "umur": 40}]


blabla(data, 20, 50)
