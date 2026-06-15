from git import Repo
import uuid
import os


def clone_repository(url):

    repo_path = os.path.join(
        "repos",
        str(uuid.uuid4())
    )

    os.makedirs(
        "repos",
        exist_ok=True
    )

    Repo.clone_from(
        url,
        repo_path
    )

    return repo_path