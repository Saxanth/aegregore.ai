# Create, Login, Logout, Register, Delete
from surrealdb import Surreal

# We have many different databases in our project. So we need to create a new instance of the SurrealDB client for each database.
SURREAL_URL = "http://127.0.0.1:8000/rpc"

SURREAL_USER_NS  = "user"
SURREAL_CACHE_NS = "cache"
SURREAL_EMBED_NS = "embeddings"
SURREAL_NODES_NS = "nodes"

SURREAL_USERNAME = "root"
SURREAL_PASSWORD = "password"
SURREAL_NETWORK  = "db_network"