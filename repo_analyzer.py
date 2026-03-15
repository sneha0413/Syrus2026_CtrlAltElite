import os

# correct relative path to dataset repo
REPO_PATH = "../shopstack-platform"

def search_repo(keywords):

    matches = []

    for root, dirs, files in os.walk(REPO_PATH):

        for file in files:

            if file.endswith(".js") or file.endswith(".ts") or file.endswith(".py"):

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf8", errors="ignore") as f:

                        content = f.read().lower()

                        for key in keywords:

                            if key in content:
                                matches.append(file_path)
                                break

                except:
                    pass

    return matches