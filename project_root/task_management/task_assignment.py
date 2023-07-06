```python
import trello
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class TaskAssignment:
    def __init__(self, api_key, token):
        self.client = trello.TrelloClient(api_key=api_key, token=token)
        self.model = RandomForestClassifier()

    def get_tasks(self, board_id):
        board = self.client.get_board(board_id)
        tasks = []
        for list_ in board.list_lists():
            for card in list_.list_cards():
                tasks.append((card.name, card.desc, card.member_id))
        return tasks

    def prepare_data(self, tasks):
        X = []
        y = []
        for task in tasks:
            X.append(task[:2])
            y.append(task[2])
        return X, y

    def train_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        print(f"Model Score: {self.model.score(X_test, y_test)}")

    def assign_task(self, task_name, task_desc):
        task = (task_name, task_desc)
        assigned_member = self.model.predict([task])
        return assigned_member

if __name__ == "__main__":
    task_assignment = TaskAssignment("your_api_key", "your_token")
    tasks = task_assignment.get_tasks("your_board_id")
    X, y = task_assignment.prepare_data(tasks)
    task_assignment.train_model(X, y)
    assigned_member = task_assignment.assign_task("New Task", "Task Description")
    print(f"Assigned Member ID: {assigned_member}")
```