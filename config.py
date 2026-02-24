import os

# Read the Flask secret key from an environment variable in production.
# The hard-coded fallback is only for development/testing; do NOT use
# this value in production. Set `RAVINTOLA_SECRET_KEY` in the environment.
secret_key = os.environ.get(
	"RAVINTOLA_SECRET_KEY",
	"dev-secret-key-please-change-this-in-production",
)
