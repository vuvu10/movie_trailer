import webbrowser


class movies():
	"""Below is the class for the movies"""

    def __init__(self, movie_title, movie_description, 
    			 movie_poster_image, trailer_youtube):
        self.title = movie_title
        self.description = movie_description
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
