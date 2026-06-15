from clone_repo import clone_repository

path = clone_repository(
    "https://github.com/pallets/flask"
)

print("Repository cloned to:", path)