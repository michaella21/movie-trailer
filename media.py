import webbrowser


class Movie():
    # This class creates an instance of a movie and its related information.

    def __init__(self, movie_title, movie_poster_url, movie_trailer_url,  movie_storyline, movie_director, movie_main_cast, year_released):
        self.title = movie_title
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
        self.storyline = movie_storyline
        self.director = movie_director
        self.main_cast = movie_main_cast
        self.released = year_released

    def show_trailer(self):
        # This method opens a pop-up for the given url for trailer.
        webbrowser.open(self.trailer_youtube_url)
