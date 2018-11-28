import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.environ.get("SLACK_API_TOKEN")
DEFAULT_REPLY = 'おみくじ引かない？'
PLUGINS = ['plugins']

