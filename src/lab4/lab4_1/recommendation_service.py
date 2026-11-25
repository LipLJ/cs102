from lab4.lab4_1.movie import Movie

class RecommendationService:
    def __init__(self, movies_file, history_file):
        self.movies = self.load_movies(movies_file)
        self.histories = self.load_histories(history_file)
    def load_movies(self, filename):
        movies = {}
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                movie_id, title = line.split(",", 1)
                movies[int(movie_id)] = Movie(
                    int(movie_id),
                    title.strip()
                )
        return movies


    def load_histories(self, filename):
        histories = []
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    history = [
                        int(movie_id)
                        for movie_id in line.split(",")
                    ]
                    histories.append(history)
        return histories


    def recommend(self, user_history):
        watched = set(user_history)
        if not watched:
            return None
        scores = {}
        for history in self.histories:
            unique_history = set(history)
            common = watched & unique_history
            similarity = len(common) / len(watched)
            if similarity < 0.5:
                continue
            for movie_id in history:
                if movie_id not in watched:
                    scores[movie_id] = (scores.get(movie_id, 0) + similarity)
        if not scores:
            return None
        best_id = max(scores, key=scores.get)
        return self.movies.get(best_id)
