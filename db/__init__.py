import os

NEON_URI = os.environ.get("DB_URI_NEON")
NEON_PASSWORD = os.environ.get("DB_PASSWORD_NEON")
if not NEON_URI or not NEON_PASSWORD:
    print("DB_URI_NEON and DB_PASSWORD_NEON environment variables must be set")

NEON_CONNECTION_URI = f"postgresql+psycopg2://FlatsDB_owner:{NEON_PASSWORD}@{NEON_URI}/FlatsDB?sslmode=require" if NEON_URI and NEON_PASSWORD else None
LOCAL_CONNECTION_URI = "postgresql+psycopg2://postgres:password@localhost/FlatsDB"