from pathlib import Path

# ENV VARS
from config.env_util import get_env_vars

BASE_DIR = Path(__file__).resolve().parent
TEST_DOTENV_FILEPATH = f"/{BASE_DIR}/../.env.tests"
ENV_VARS = get_env_vars(path=TEST_DOTENV_FILEPATH)
