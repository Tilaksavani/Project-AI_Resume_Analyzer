def load_job_description(path="job_description.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
