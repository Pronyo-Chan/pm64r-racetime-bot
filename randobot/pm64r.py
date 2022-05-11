import json

import requests


class PM64R:
    """
    Class for interacting with pm64randomizer.com to generate seeds
    """
    seed_url = 'https://pm64randomizer.com/seed?id='
    seed_post_endpoint = 'https://paper-mario-randomizer-server.ue.r.appspot.com/randomizer_preset'
    preset_endpoint = 'https://paper-mario-randomizer-server.ue.r.appspot.com/preset-names'

    def __init__(self):
        self.presets = self.load_presets()

    def load_presets(self):
        """
        Load and return available seed presets.
        """
        presets = requests.get(url=self.preset_endpoint).text
        return presets

    def roll_seed(self, preset, is_spoiler_seed):
        """
        Generate a seed and return its public URL.
        """
        id = requests.post(
            url=self.seed_post_endpoint,
            json={"preset_name": f"{preset}", "spoiler_seed": is_spoiler_seed},
            headers={'Content-Type': 'application/json'}
        ).json()
        return id
