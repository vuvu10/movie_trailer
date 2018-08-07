
import fresh_tomatoes
import Media

valerian_and_the_city_of_thousand_planets = Media.movies("Valerian",
                                                        "and the city of thousand planets(2017)" \
                                                        "Laureline(Cara Delevine) and Valerian(Dane Dehaan)" \
                                                        "A dark force threatens Alpha,a vast metropolis and" \
                                                        "home to species from a thousand planets.Special" \
                                                        "operatives valerian and Laureline must race to" \
                                                        "identify the marauding menace and safeguard not just" \
                                                        "Alpha, but the future of the universe.",
                                                      "https://i.ytimg.com/vi/BszXhUjJz00/maxresdefault.jpg",
                                                        "https://www.youtube.com/watch?v=BszXhUjJ")



Jumanji_Welcome_to_the_jungle = Media.movies("Jumanji",
                                            "Welcome to the jungle(2017)" \
                                           "In a brand new jumanji adventure," \
                                            "4 high school kids discover an old" \
                                            "video game console and are drawn into" \
                                             "the game jungle setting",
                                            "https://img.youtube.com/vi/2QKg5SZ_35I/hqdefault.jpg",
                                            "https://www.youtube.com/watch?v=2QKg5SZ_35I")


the_foreigner = Media.movies("The_foreigner",
                             "foreigner(2017)"\
                             "A man seeks revenge" \
                            "his daughter is killed" \
                             "and the police does nothing",
                            "https://i.ytimg.com/vi/r_rSAbYyIq0/maxresdefault.jpg",
                             "https://www.youtube.com/watch?v=33iuQu3UtjI")

movies = []
movies.append(valerian_and_the_city_of_thousand_planets)
movies.append(Jumanji_Welcome_to_the_jungle)
movies.append(the_foreigner)

fresh_tomatoes.open_movies_page(movies)

