class Settings:
    def __init__(self):
        self.job = None
        self.xgrid_min = None
        self.xgrid_max = None
        self.xgrid_points = None

    def __repr__(self):
        string = ""
        string += f"running job {self.job}"
        string += f"\n~~ xgrid parameters ~~"
        string += f"\n    xgrid-min: {self.xgrid_min}"
        string += f"\n    xgrid-max: {self.xgrid_max}"
        string += f"\n    xgrid-points: {self.xgrid_points}"
        return string

    def set_job(self,job):
        self.job = job

    def set_xgrid(self, args):
        self.xgrid_min = args["xgrid-min"]
        self.xgrid_max = args["xgrid-max"]
        self.xgrid_points = args["xgrid-points"]