import fresh_tomatoes
import Media

#initializing the list of my movies..
valerian_and_the_city_of_thousand_planets = Media.movies("Valerian",
                                                        "and the city of thousand planets(2017)" \
                                                        "Laureline(Cara Delevine) and Valerian(Dane Dehaan)" \
                                                        "A dark force threatens Alpha,a vast metropolis and" \
                                                        "home to species from a thousand planets.Special" \
                                                        "operatives valerian and Laureline must race to" \
                                                        "identify the marauding menace and safeguard not just" \
                                                        "Alpha, but the future of the universe.", 
                                                        "https://i.ytimg.com/vi/BszXhUjJz00/maxresdefault.jpg",
                                                        "https://www.youtube.com/watch?v=NNrK7xVG3PM")



Jumanji_Welcome_to_the_jungle = Media.movies("Jumanji",
                                            "Welcome to the jungle(2017)" \
                                           "In a brand new jumanji adventure," \
                                            "4 high school kids discover an old" \
                                            "video game console and are drawn into" \
                                             "the game jungle setting",
                                            "https://img.youtube.com/vi/2QKg5SZ_35I/hqdefault.jpg",
                                            "https://www.youtube.com/watch?v=2QKg5SZ_35I")

Roman_J_Israel = Media.movies("Roman_j_israel",
                              "Roman J Israel, Esq is a somewhat socially isolated lawyer,"\
                              "perhaps a little on the autism spectrum side, who  not only"\
                              "is extremely bright (can give you obscure citations from the "\
                              "code of justice) but is idealistically principled to take on"\
                              " cases of the poor and disadvantaged."
                              "http://filmrap.net/wp-content/uploads/2017/11/Screen-Shot-2017-11-07-at-12.31.00-PM-3.png"
                              "https://www.youtube.com/watch?v=tGVIKqbEtdU" )


the_foreigner = Media.movies("The_foreigner",
                             "foreigner(2017)"\
                             "A man seeks revenge" \
                            "his daughter is killed" \
                             "and the police does nothing",
                            "https://i.ytimg.com/vi/r_rSAbYyIq0/maxresdefault.jpg",
                             "https://www.youtube.com/embed/LmImJ6ZUiqE")

Black_Panther = Media.movies("Black_panther", 
                            "After the death of his father,"\
                            "the king of wakanda, young t'challla"\
                            "returns home to the isolated high tech"\
                            "African nation to succeed to the throne"\
                            "and take his rightful place as king."\
                            "But when a powerful enemy reappears, t'challa"\
                            "mettle as king - and black panther is tested"\
                            "when he\s drawn into a formidable conflict that"\
                            "puts tbe fate of wakanda and the entire world at risk",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg"
                            "https://youtu.be/X_MUyHpojYE")

The_Hangover_Part_III = Media.movies("The_Hangover_Part_III"
                                    "This time, there's no wedding. No bachelor party." 
                                    "What could go wrong, right? But when the Wolfpack" 
                                     "hits the road, all bets are off in The Hangover 3" 
                                     "https://upload.wikimedia.org/wikipedia/en/c/ce/The_Hangover_Part_II_Soundtrack.jpg"
                                    "https://www.youtube.com/watch?v=KLAkxSjs8ZY")


#List of my movies..

movies = []
movies.append(valerian_and_the_city_of_thousand_planets)
movies.append(Jumanji_Welcome_to_the_jungle)
movies.append(Roman_j_israel)
movies.append(the_foreigner)
movies.append(black_panther)
movies.append(The_Hangover_Part_III)
fresh_tomatoes.open_movies_page(movies)

