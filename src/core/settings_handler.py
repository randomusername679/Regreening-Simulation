import json

import configs.config as config

class SettingsHandler:
    def __init__(self, app):
        self.app = app

        self.last_updated = 0
        self.update_timer = 0

        self.visualise_mycorrhiza = None
        self.time_scale = None
        self.time_paused = None

        self.update_settings()

    @staticmethod
    def get_dict():
        with open(config.SETTINGS_PATH) as file:
            data = json.load(file)

        return data

    def update_settings(self):
        settings = self.get_dict()
        self.visualise_mycorrhiza = settings["visualise-mycorrhiza"]
        self.time_scale = settings["time-scale"]
        self.time_paused = settings["time-paused"]

    def update(self):
        self.update_timer += self.app.dt
        if self.update_timer >= config.SETTINGS_UPDATE_DEBOUNCE:
            self.update_timer = 0
            self.update_settings()