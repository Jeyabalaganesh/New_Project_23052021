index_songs = 3
song_index = 1

albums = [
    [
        "Jeans",
        "ARR",
        "1991",
        [
            [1, "Jean1"],
            [2, "Jean2"],
            [3, "Jean3"],
        ]
    ],
    [
        "Muthalvan",
        "ARR",
        "2005",
        [
            [1, "Muthalvan1"],
            [2, "Muthalvan2"],
            [3, "Muthalvan3"],
        ]
    ],
    [
        "Paiya",
        "Yuvan",
        "2010",
        [
            [1, "Paiya1"],
            [2, "Paiya2"],
            [3, "Paiya3"],
        ]
    ],
]


while True:

    print("The available albums are")

    for index , item in enumerate (albums):
        movie , comp, year , song = item
        print("ID: {0} - Movie: {1} -Composer {2} -Year {3} ".format(index+1, movie, comp, year))

    movie = int(input ("Enter the movie no: "))

    if 0 < movie <= len(albums):
        print("The available songs in the movie {0} are :".format(albums[movie-1][0]))

        for index,song in albums[movie-1][index_songs]:
            print ("ID {0} - Song {1}".format(index,song))

        song = int(input("Enter the song number to play"))
        print ("Playing ----^---- {0}".format(albums[movie-1][index_songs][song-1][song_index]))
        print("=============================")
        break

    else:
        print ("Poda Fool")
        break



