"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media


def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    roman_j_israel = media.Movie("Roman J. Israel, Esq.",
                                 "Roman J Israel is a  socially isolated lawyer",
                                 "http://filmrap.net/wp-content/uploads/"
                                 "2017/11/Screen-Shot-2017-11-07-at-12.31"
                                 ".00-PM-3.png",
                                 "https://www.youtube.com/watch?v=tGVIKqbEtdU",
                                 "September 10, 2017")

    valerian = media.Movie("Valerian",
                           "Valerian and the City of a Thousand Planets",
                           "https://i.ytimg.com"
                           "/vi/BszXhUjJz00/maxresdefault.jpg",
                           "https://youtube.com/watch?v=NNrK7xVG3PM2017",
                           "July 17, 2017")

    jumanji = media.Movie("Jumanji",
                          "4 high school kids discover video game console",
                          "http://t0.gstatic.com/"
                          "images?q=tbn:ANd9GcTT8Uml87HoFiuxzh8_LH5j3q2Q4Os803jFvF0uQ9gjmWKgqgdN",
                          "https://www.youtube.com/watch?v=2QKg5SZ_35I",
                          "December 5, 2017")

    the_foreigner = media.Movie("The Foreigner",
                                "A man seeks revenge of his daughter's murder",
                                "http://www.movienewsletters.net/"
                                "photos/NZL_234379R1.jpg",
                                "https://www.youtube.com/embed/LmImJ6ZUiqE",
                                "September 24, 2017")

    black_panther = media.Movie("Black_Panther",
                                "A son who returns Home after his father's death",
                                "https://upload.wikimedia.org/wikipedia/en/0/0c/"
                                "Black_Panther_film_poster.jpg",
                                "https://youtu.be/X_MUyHpojYE",
                                "January 29, 2018")

    hangover3 = media.Movie("The Hangover Part III",
                            "The Hangover Part III is a 2013 American comedy film",
                            "https://upload.wikimedia.org"
                            "/wikipedia/en/c/ce/The_Hangover_Part_II_Soundtrack.jpg",
                            "https://www.youtube.com/watch?v=KLAkxSjs8ZY",
                            "May 20, 2013")

    # Store the Movie objects in a list.
    movies = [roman_j_israel, valerian, jumanji, the_foreigner, black_panther, hangover3]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
