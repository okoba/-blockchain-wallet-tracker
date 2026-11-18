import json
import os

class UserSettings:
    def __init__(self, settings_file='user_db.json'):
        self.settings_file = settings_file
        self.users = self._load()
        
    def _load(self) -> dict:
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        return {}
        
    def save(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self.users, f)
            
    def add_user(self, chat_id: str):
        self.users[chat_id] = {'subscribed': True}
        self.save()
        
    def remove_user(self, chat_id: str):
        if chat_id in self.users:
            self.users[chat_id]['subscribed'] = False
            self.save()
