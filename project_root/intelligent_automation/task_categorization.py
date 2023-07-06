```python
import trello
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

class TaskCategorizer:
    def __init__(self, api_key, token, board_id):
        self.client = trello.TrelloClient(api_key=api_key, token=token)
        self.board = self.client.get_board(board_id)
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def fetch_tasks(self):
        tasks = []
        for list_ in self.board.list_lists():
            for card in list_.list_cards():
                tasks.append(card.description)
        return tasks

    def categorize_tasks(self, num_categories):
        tasks = self.fetch_tasks()
        tfidf = self.vectorizer.fit_transform(tasks)
        model = KMeans(n_clusters=num_categories, init='k-means++', max_iter=100, n_init=1)
        model.fit(tfidf)
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = self.vectorizer.get_feature_names_out()
        categories = {}
        for i in range(num_categories):
            category_terms = [terms[ind] for ind in order_centroids[i, :10]]
            categories[i] = category_terms
        return categories

    def tag_tasks(self, num_categories):
        categories = self.categorize_tasks(num_categories)
        tasks = self.fetch_tasks()
        tfidf = self.vectorizer.transform(tasks)
        predictions = model.predict(tfidf)
        for i, task in enumerate(tasks):
            task.add_label(categories[predictions[i]])
```
