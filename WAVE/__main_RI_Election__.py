import election
import audit
import data_gen
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import UI


if __name__ != "__main__":
    sys.exit(1)

rispecial = data_gen.Rispecial()

e = rispecial.get_election()

for i, ballot in enumerate(e.get_ballots()):
    print("Ballot " + str(ballot.get_audit_seq_num()) + " Reported Value " + str(
ballot.get_reported_value().get_name()) + " Actual value " + str(ballot.get_actual_value().get_name()))

rla = audit.RLA()
rla.init(rispecial.get_reported_results())

rla.set_parameters([1])
rla.recompute(e.get_ballots(), rispecial.get_reported_results())

#print(rla.get_progress())

# ===== Starting up the App =========
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = UI.Ui_MainWindow()
ui.init(e, rla)
ui.setupUi(MainWindow)

MainWindow.show()

sys.exit(app.exec_())
