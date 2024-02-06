import os
from dotenv import load_dotenv


def get_enviroment_variables():
    load_dotenv()

    environment_variables = {
        'BASE_API': os.getenv('BASE_API')
    }

    return environment_variables