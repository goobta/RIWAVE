import sys
import election
import audit
import data_gen
import csv
import os

def main():
    num_votes = -1
    error_rate = -1
    election_resultsfile = ""
    audit_type = ""
    risklimit = -1
    outputfile_name = ""
    #num_candidates = sys.argv[3]
    num_candidates = -1

    # READ CANDIDATE NAMES and VOTE SHARES
    with open('experiment_parameters.csv', 'r') as csvfile:
        csvfile.readline()  # Skip first line
        readCSV = csv.reader(csvfile, delimiter=',')
        for num_votes, error_rate, num_candidates, election_resultsfile, audit_type,risk_limit, outputfile_read_name in readCSV:
            num_votes= int(num_votes)
            error_rate = int(error_rate)
            num_candidates = int(num_candidates)
            election_results_file = election_resultsfile
            audit_type = audit_type
            risk_limit = int(risk_limit)
            outputfile_name = outputfile_read_name

            candidate_vote_share = [0] * num_candidates
            candidate_names = [0] * num_candidates

            with open(election_results_file, 'r') as csvfile:
                indexer = 0
                csvfile.readline()  # Skip first line
                readCSV = csv.reader(csvfile, delimiter=',')
                for name, percentage in readCSV:
                    candidate_names[indexer] = name
                    candidate_vote_share[indexer] = percentage
                    indexer = indexer + 1

            for i in range(len(candidate_names)):
                print("CANDIDATE " + str(i) + " NAME " + candidate_names[i])
                print("CANDIDATE " + str(i) + " VOTE SHARE " + candidate_vote_share[i])

                    # TODO: REMOVE HARD_CODED VALUES
                    # TODO: DO THIS AFTER THE RESULTS COME IN
            with open(outputfile_name, 'a', newline='') as myfile:
                wr = csv.writer(myfile, delimiter=',')
                if (file_is_empty(outputfile_name)):
                    header = ['Number of Votes',
                              'Error rate',
                              'Number of Candidates',
                              'Election Results Filename',
                              'Audit type',
                              'Risk Limit',
                              'Number of Votes Counted',
                              'Audit Result']
                    wr.writerow(header)
                data = [str(num_votes),
                        str(error_rate),
                        str(num_candidates),
                        election_results_file,
                        audit_type,
                        str(risk_limit),
                        '100 Votes',
                        'Full Hand Count Required']
                wr.writerow(data)


    # num_votes = sys.argv[1]
    # error_rate = (sys.argv[2])
    # num_candidates = sys.argv[3]
    #
    #num_candidates_int = int(num_candidates)


    # Get vote shares for each candidate:
    # for i in range(0, num_candidates_int):
    #    # print(""+str(i))
    #     candidate_names[i]=sys.argv[4+i]

    # for i in range(0, num_candidates_int):
    #     candidate_vote_share[i]=sys.argv[4+num_candidates_int+i]

    # audit_type = sys.argv[4+2*num_candidates_int]
    # risk_limit = sys.argv[5+2*num_candidates_int]
    # outputfile_name=sys.argv[6+2*num_candidates_int]

    # audit_type = sys.argv[4]
    # risk_limit = sys.argv[5]
    # outputfile_name = sys.argv[6]

    #READ CANDIDATE NAMES and VOTE SHARES




    # print ("" + num_votes)
    # print ("" + num_candidates)




    # print("" + audit_type)
    # print("" +risk_limit)
    # print(outputfile_name)



    pres = data_gen.Pres2016()
    pres.gen_ballots(int(num_votes), int(error_rate)/100)

    e = pres.get_election()

# for i, ballot in enumerate(e.get_ballots()):
#     print("Ballot " + str(ballot.get_audit_seq_num()) + " Reported Value " + str(
#         ballot.get_reported_value().get_name()) + " Actual value " + str(ballot.get_actual_value().get_name()))

    rla = audit.RLA()
    rla.init(pres.get_reported_results())

    rla.set_parameters([1])
    rla.recompute(e.get_ballots(), pres.get_reported_results())



    print(rla.get_progress())


# # ===== Starting up the App =========
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWsindow()
#
# ui = UI.Ui_MainWindow()
# ui.init(e, rla)
# ui.setupUi(MainWindow)
#
# MainWindow.show()

#sys.exit(app.exec_())
def file_is_empty(path):
    return os.stat(path).st_size==0

if __name__ == "__main__":
    main()

    # if (os.stat(outputfile_name).st_size == 0):
    #     with open(outputfile_name, 'w', newline='') as fp:
    #         a = csv.writer(fp, delimiter=',')
    #         data = [['Me', 'You'],
    #                 ['293', '219'],
    #                 ['54', '13']]
    #         a.writerows(data)