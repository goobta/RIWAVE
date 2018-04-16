import audit
import election

class Comparision(audit.Audit):
    name = "Comparision RLA"
    status_codes = ["In Progress",
                    "Election Results Verified",
                    "Full Hand Count Required"]

    def __init__(self):
        pass

    def init(self, results):
        pass

    def get_progress(self):
        pass

    def get_status(self):
        pass

    @staticmethod
    def get_name():
        pass

    def get_parameters(self, param):
        pass

   
   def set_parameters(self, param):
       pass

   def compute(self, ballot):
       pass

   def recompute(self, ballots, results):
       pass
   
   def get_current_result(self):
       pass
