import json

import requests


class PM64R:
    """
    Class for interacting with pm64randomizer.com to generate seeds
    """
    #seed_url = 'https://uat-dot-paper-mario-randomizer-app.ue.r.appspot.com/seed?id='    
    #seed_post_endpoint = 'https://uat-dot-paper-mario-randomizer-server.ue.r.appspot.com/randomizer_preset'    
    #seed_get_endpoint = 'https://uat-dot-paper-mario-randomizer-server.ue.r.appspot.com/randomizer_settings'    
    #preset_endpoint = 'https://uat-dot-paper-mario-randomizer-server.ue.r.appspot.com/preset-names'
    #reveal_spoiler_endpoint = 'https://uat-dot-paper-mario-randomizer-server.ue.r.appspot.com'

    seed_url = 'https://pm64randomizer.com/seed?id='
    seed_post_endpoint = 'https://paper-mario-randomizer-server.ue.r.appspot.com/randomizer_preset'
    seed_get_endpoint = 'https://paper-mario-randomizer-server.ue.r.appspot.com/randomizer_settings'
    preset_endpoint = 'https://paper-mario-randomizer-server.ue.r.appspot.com/preset-names'
    reveal_spoiler_endpoint = 'https://paper-mario-randomizer-server.ue.r.appspot.com/reveal_spoiler'

    def __init__(self, api_key):
        self.presets = self.load_presets()
        self.api_key = api_key

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
    
    def reveal_spoiler_log(self, seed_id):
        """
        Makes the spoiler log available for specified seed. To be called at end of race.
        """
        requests.post(
            url=self.reveal_spoiler_endpoint,
            json={"api_key": f"{self.api_key}", "seed_id": seed_id},
            headers={'Content-Type': 'application/json'}
        )

    def get_seed_hash(self, seed_id):
        """
        Get a seed's hash identifier.
        """
        response = requests.get(
            url=f'{self.seed_get_endpoint}/{seed_id}',
            headers={'Content-Type': 'application/json'}
        ).json()
        items = ', '.join(response["SeedHashItems"])
        return items
