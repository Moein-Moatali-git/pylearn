from media import Media


class Clip(Media):
    def __init__(self, name, director, IMDB_score, url, duration, casts,country):
        super().__init__(name, director, IMDB_score, url, duration, casts)
        self.country=country