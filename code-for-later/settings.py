class Settings:
    def __init__(self):
        self.job = None

    def __repr__(self):
        string = ""
        string += f"running job {self.job}"
        return string

    def set_job(self,job):
        self.job = job