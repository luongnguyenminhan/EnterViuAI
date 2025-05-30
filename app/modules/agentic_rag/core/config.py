"""
Configuration for the Agentic RAG module.
"""

import os
from pydantic import BaseModel

# Check if running in Docker environment
DOCKER_ENVIRONMENT = os.getenv('DOCKER_ENVIRONMENT', 'False').lower() == 'true'

# Qdrant configuration
# In Docker, use the service name; otherwise use localhost
QDRANT_HOST = 'qdrant' if DOCKER_ENVIRONMENT else 'localhost'
# Important: Use port 6334 for HTTP API (not 6333 which is for gRPC)
QDRANT_URL = os.getenv(
	'QDRANT_URL',
	'https://3b8399d1-fff9-4b31-9f6e-a5e4fcfffc77.us-east-1-0.aws.cloud.qdrant.io:6333',
)
QDRANT_API_KEY = os.getenv(
	'QDRANT_API_KEY',
	'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.qUBAYKVmnrDttHhgelrgCEtUsI_lP9uad5waFf2KBMs',
)
QDRANT_COLLECTION = os.getenv('QDRANT_COLLECTION', 'agentic_rag_kb')

# Embedding configuration
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'models/embedding-001')


class QdrantConfig(BaseModel):
	"""Qdrant configuration."""

	QdrantUrl: str = QDRANT_URL
	QdrantApiKey: str = QDRANT_API_KEY
	QdrantCollection: str = QDRANT_COLLECTION

	class Config:
		env_prefix = 'QDRANT_'


settings = QdrantConfig()
