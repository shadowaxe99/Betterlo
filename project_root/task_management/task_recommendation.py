```python
import trello
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class TaskRecommender:
    def __init__(self, api_key, token):
        self.client = trello.TrelloClient(api_key=api_key, token=token)
        self.vectorizer = TfidfVectorizer()

    def get_board_tasks(self, board_id):
        board = self.client.get_board(board_id)
        tasks = [card.name for card in board.get_cards()]
        return tasks

    def fit(self, tasks):
        self.vectorizer.fit(tasks)

    def recommend_tasks(self, task, top_n=5):
        tasks = self.get_board_tasks()
        tasks.append(task)

        tfidf_matrix = self.vectorizer.transform(tasks)
        cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix).flatten()
        related_task_indices = cosine_similarities.argsort()[:-top_n:-1]

        return [(index, tasks[index]) for index in related_task_indices]

if __name__ == "__main__":
    api_key = "your_api_key"
    token = "your_token"
    board_id = "your_board_id"

    recommender = TaskRecommender(api_key, token)
    tasks = recommender.get_board_tasks(board_id)
    recommender.fit(tasks)

    task = "Design the homepage"
    print(recommender.recommend_tasks(task))
```