from pathlib import Path

import json

class FetchJSONData:
    """Used to fetch data and parse it as we want. This is particular to .json type."""

    def __init__(self, path_name):
        """Initializes the instance with the atts it needs wiht the path as a param."""
        self.path = Path(f'{path_name}.json')

    def read_get_json(self):
        """Used to read the contents of the json file into memory."""
        json_content = json.loads(self.path)
        json_data = self.path.read_text(json_content)
        return json_data
    
