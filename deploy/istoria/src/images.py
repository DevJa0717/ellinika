import json, os
IMAGES = json.load(open(os.path.join(os.path.dirname(__file__), "images.json"))) if os.path.exists(os.path.join(os.path.dirname(__file__), "images.json")) else {}
