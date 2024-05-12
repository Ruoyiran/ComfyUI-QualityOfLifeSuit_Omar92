# ----------------------------------------------------------
# update logic
import os
import json

# check if config file exists
if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")):
    # create config file
    config = {
        "branch": "master",
        "auto_update": True,
        "openai": {
            "api_key": "sk-#########################################",
            "models": ["gpt-3.5-turbo"],
            "azure_api_version": "",
            "azure_api_endpoint": ""
        }
    }
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json"), "w") as f:
        json.dump(config, f, indent=4)

# load config file
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json"), "r") as f:
    config = json.load(f)

# check if auto_update is set
if "auto_update" not in config:
    config["auto_update"] = False

# check if version is set
if "version" not in config:
    config["branch"] = "master"

if config["auto_update"] == True:
    try:
        from .update import update as update

        currentPath = os.path.dirname(os.path.realpath(__file__))
        # run update/update.py to update the node class mappings
        update.update(currentPath, branch_name=config["branch"])
    except ImportError:
        print("Failed to auto update `Quality of Life Suit` ")

# ----------------------------------------------------------

from .src.QualityOfLifeSuit_Omar92 import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_SUIT

try:
    from .src.QualityOfLife_deprecatedNodes import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_DEPRECATED
except ImportError:
    NODE_CLASS_MAPPINGS_DEPRECATED = {}

__all__ = ['NODE_CLASS_MAPPINGS_SUIT', 'NODE_CLASS_MAPPINGS_DEPRECATED', 'NODE_CLASS_MAPPINGS']
NODE_CLASS_MAPPINGS = {
    **NODE_CLASS_MAPPINGS_SUIT,
    **NODE_CLASS_MAPPINGS_DEPRECATED
}
