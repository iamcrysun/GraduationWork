import os
from enum import Enum

# Paths & Dirs
CONFIGS_PATH = os.path.abspath("./Server/configs")
ENVS_PATH = os.path.abspath("./Server/envs")
STATIC_FILES_PATH = os.path.abspath("./media")
# Versions

API_VERSION = "0.1.6"

# Security & Crypt
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class TokenAppointments(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


class TokenTypes(str, Enum):
    BEARER = "bearer"
