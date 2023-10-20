import os

from dotenv import load_dotenv

load_dotenv("config.env" if os.path.isfile("config.env") else "sample_config.env")

BOT_TOKEN = os.environ.get('BOT_TOKEN', '5620597185:AAFP-9SMEH8W0dl-sApENxh20hG3yg2UVAQ')
API_ID = int(os.environ.get('API_ID', '9774346'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQCVJQoAV8U1E7edwrs7_gZBxW10WYCXFquVtq5EFiEEjRjzgJ22adwZfp5dG5VXHT5swC4S2PpC5-lGsDeF53kjLqMbTgZAAmSPJjZQj2ZQ3STM0yZYt8KFpZfO566FUo3_qWUtnTG3d3Nj3yEGLFV-JNRU4UApjzKLdApLQoYz-irHdSuDnObbGGT8IYENwrDigoHY0WVpLK8nDYbes_TUXbKmR7SkJBYEY3wCx2wfq0acprN-S6ORYGuFyVSadXZgp-WAJeXD54eb7Az-9vk3iNUIX0hO5eCA9H18M_kVRi79fUC0VxXe6gVIZqLtM1r16fRjNNWXfusWM9MgOy9nE22qFgAAAAA2GAb2AA')
API_HASH = os.environ.get('API_HASH', 'a92aed7d74654a563af4b07efbcd88e9')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '907544310').split()))
LOG_GROUP_ID = int(os.environ.get('LOG_GROUP_ID', '-1001844573348'))
GBAN_LOG_GROUP_ID = int(os.environ.get('GBAN_LOG_GROUP_ID', '-1001844573348'))
MESSAGE_DUMP_CHAT = int(os.environ.get('MESSAGE_DUMP_CHAT'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('MONGO_URL')
ARQ_API_KEY = os.environ.get('ARQ_API_KEY')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
