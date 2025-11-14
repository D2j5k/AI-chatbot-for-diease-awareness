import json

class UserPreferenceService:
    def __init__(self, db_path):
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.preferences = json.load(f)
        except FileNotFoundError:
            self.preferences = {}

    def get_user_language(self, user_id):
        return self.preferences.get(user_id, {}).get("language")

    def set_user_language(self, user_id, language):
        if user_id not in self.preferences:
            self.preferences[user_id] = {}
        self.preferences[user_id]["language"] = language
        with open(self.db_path, 'w') as f:
            json.dump(self.preferences, f, indent=2)
