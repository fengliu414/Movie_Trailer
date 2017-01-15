import webbrowser


class Movie(object):

    """A class that contains info about movies

       Attributes:
           attr1(movie_title): The title of the movie
           attr2(movie_storyline): The story line of the movie
           attr3(poster_image): The url of the poster image
           attr4(trailer_youtube_url): The url of the movie trailer


    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

