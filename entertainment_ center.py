import fresh_tomatoes
import Media

"""initializing the list of my movies"""
valerian_and_the_city_of_thousand_planets = Media.movies("Valerian",
                                                         "and the city",
                                                         "https://i.ytimg.com"
                                                         "/vi/BszXhUjJz00/",
                                                         "maxresdefault.jpg"
                                                         "https://youtube.com"
                                                         "https://youtube.com"
                                                         "/watch?v=NNrK7xVG3PM"
                                                         "2017"),

Jumanji_Welcome_to_the_jungle = Media.movies("Jumanji",
                                             "Welcome to the jungle",
                                             "in a new jumanji"
                                             "4 high school kids discover",
                                             "video game console",
                                             "the game jungle setting",
                                             "https://img.youtube.com"
                                             "/vi/2QKg5SZ_35I/hqdefault.jpg",
                                             "https://www.youtube.com"
                                             "/watch?v=2QKg5SZ_35I",
                                             "2017")

Roman_J_Israel = Media.movies("Roman_j_israel",
                              "Roman J Israel is a  socially isolated lawyer",
                              "perhaps a little on the autism spectrum side"
                              "is extremely bright can give you obscure"
                              "code of justice yet idealistically principled"
                              " cases of the poor and disadvantaged."
                              "http://filmrap.net/wp-content/uploads/"
                              "2017/11/Screen-Shot-2017-11-07-at-12.31"
                              ".00-PM-3.png"
                              "https://www.youtube.com"
                              "/watch?v=tGVIKqbEtdU")


the_foreigner = Media.movies("The_foreigner",
                             "foreigner",
                             "A man seeks revenge"
                             "his daughter is killed"
                             "and the police does nothing",
                             "https://i.ytimg.com/vi/"
                             "r_rSAbYyIq0/maxresdefault.jpg"
                             "https://www.youtube.com/embed/LmImJ6ZUiqE"
                             "2017"),

Black_Panther = Media.movies("Black_panther",
                             "After the death of his father",
                             "the king of wakanda, young t'challla"
                             "returns home to the isolated high tech"
                             "African nation to succeed to the throne"
                             "and take his rightful place as king."
                             "But when a powerful enemy reappears, t'challa"
                             "mettle as king - and black panther is tested"
                             "when he is drawn into a formidable conflict that"
                             "puts the fate of wakanda & entire world at risk",
                             "https://upload.wikimedia.org/wikipedia/en/0/0c/"
                             "Black_Panther_film_poster.jpg"
                             "https://youtu.be/X_MUyHpojYE")

The_Hangover_Part_III = Media.movies("The_Hangover_Part_III"
                                     "This time, there's no"
                                     "wedding. No bachelor party"
                                     "What could go wrong right?"
                                     "hits the road, all bets"
                                     "are off in The Hangover 3"
                                     "https://upload.wikimedia.org"
                                     "/wikipedia/en/c/ce/"
                                     "The_Hangover_Part_II_Soundtrack.jpg"
                                     "https://www.youtube.com"
                                     "/watch?v=KLAkxSjs8ZY")


"""List of my movies"""

movies = []
movies.append(valerian_and_the_city_of_thousand_planets)
movies.append(Jumanji_Welcome_to_the_jungle)
movies.append(Roman_j_israel)
movies.append(the_foreigner)
movies.append(black_panther)
movies.append(The_Hangover_Part_III)
fresh_tomatoes.open_movies_page(movies)

