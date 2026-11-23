from recommendation_service import RecommendationService

MOVIES_FILE = "movies.txt"
HISTORY_FILE = "history.txt"
def main():
    service = RecommendationService(
        MOVIES_FILE,
        HISTORY_FILE
    )
    print("Введите ID просмотренных фильмов через запятую:")
    try:
        user_history = [
            int(movie_id.strip())
            for movie_id in input().split(",")
        ]
        recommendation = service.recommend(user_history)
        if recommendation:
            print(recommendation.title)
        else:
            print("Рекомендаций нет")
    except ValueError:
        print("Ошибка: необходимо вводить числовые ID")
if __name__ == "__main__":
    main()