class Movie:

    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title


    def __str__(self):
        return self.title