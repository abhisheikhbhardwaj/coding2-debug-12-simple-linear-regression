"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "caebc2fc7e14fb9194f69c51ddf1d974"
GRADE_HASH = "5f71794fc657610df3a5b8802074ed61b7d4d54333345efe00330dad0eb70074"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
