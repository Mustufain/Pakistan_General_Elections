from bs4 import BeautifulSoup
import pandas as pd
import urllib2
import csv, json, sys

## This script collects data of general elections of 2002,2008,2013
## It contains National Assembly and Provincial Assembly elections results

## @author: Mustufain
## email: abbasmustufain@gmail.com


def get2002_ElectionResults(candidate_outputFile,vote_outputFile):

    # National Assembly 2002 Elections

    getCandidateInformation(candidate_outputFile)
    getVoteInformation(vote_outputFile)



def get2008_ElectionResults():

    return

def get2013_ElectionResults():

    return

def getCandidateInformation(data):

    outlier_list = ['NA-130-Lahore-XIII', 'NA-126-Lahore-IX']
    csvKeys = ['Constituency_No', 'Constituency_Name', 'Candidate_Name', 'Political_Party', 'Votes_Polled', 'Year',
               'Province', 'Sex']
    output = csv.writer(data)
    output.writerow(csvKeys)

    prev_value = -1
    const = ""
    city = ""
    constituency = ""
    name = ""
    pa = ""
    vp = ""
    year = ""
    prov = ""

    with open('National.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:

            csvrow = []

            if 'NWFP' in row[1]:
                prov = 'KPK'

            if 'FEDERALLY ADMINISTERED' in row[1]:
                prov = 'FATA'

            if 'PUNJAB' in row[1]:
                prov = 'PUNJAB'

            if 'SINDH PROVINCE' in row[1]:
                prov = 'SINDH'

            if 'BALOCHISTAN PROVINCE' in row[1]:
                prov = 'BALOCHISTAN'

            if (prev_value == 0):
                prev_value = prev_value + 1

            if 'NA-' in row[1:len(row)][1]:

                try:

                    prev_value = 0
                    constituency = row[1:len(row)]

                    if len(constituency[0].split(' ')) > 2:

                        const = constituency[0].split(' ')[0]
                        city = ''.join(constituency[0].split(' ')[1:len(constituency[0].split(' '))])

                    else:

                        const = constituency[1].split(' ')[0]
                        city = constituency[1].split(' ')[1]

                except Exception as e:

                    pass

            if 'NA-' in row[1:len(row)][0]:

                if row[1:len(row)][0] == 'NA-126-Lahore-IX':

                    const = 'NA-126'
                    city = 'Lahore-IX'
                    prev_value = 0

                elif row[1:len(row)][0] == 'NA-130-Lahore-XIII':

                    const = 'NA-130'
                    city = 'Lahore-XIII'
                    prev_value = 0

                else:
                    try:

                        prev_value = 0
                        constituency = row[1:len(row)]
                        if len(constituency[0].split(' ')) > 2:

                            const = constituency[0].split(' ')[0]
                            city = ''.join(constituency[0].split(' ')[1:len(constituency[0].split(' '))])

                        else:
                            const = constituency[0].split(' ')[0]
                            city = constituency[0].split(' ')[1]

                    except Exception as e:

                        pass




            if (prev_value > 0):

                if 'Valid Votes' in row[1:len(row)]:
                    prev_value = -1
                    csvrow = []

                else:

                    name = row[1:len(row)][0]
                    pa = row[1:len(row)][1]
                    vp = row[1:len(row)][2]
                    year = '2002'

                    if city == 'D.I.':
                        city = 'D.I.Khan'

                    csvrow.append(const)
                    csvrow.append(city)
                    csvrow.append(name)
                    csvrow.append(pa)
                    csvrow.append(vp)
                    csvrow.append(year)
                    csvrow.append(prov)
                    output.writerow(csvrow)


    return

def getVoteInformation(data):

    outlier_list = ['NA-130-Lahore-XIII', 'NA-126-Lahore-IX']
    voteKeys = ['Constituency_No', 'Constituency_Name', 'Valid_Votes', 'Rejected_Votes', 'Total_Votes',
                'Registered_Voters', 'Turnout', 'Year']
    output = csv.writer(data)
    output.writerow(voteKeys)
    const_outlier=['NA-243','NA-244','NA-245']


    const = ""
    city = ""
    constituency = ""
    year="2002"
    valid_votes = ""
    rejected_votes = ""
    registered_votes = ""
    turnout = ""
    total_votes = ""
    csvrow = []

    with open('National.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:


            startAppend = False


            if 'NA-' in row[1:len(row)][1]:

                startAppend = True
                try:

                    constituency = row[1:len(row)]

                    if len(constituency[0].split(' ')) > 2:

                        const = constituency[0].split(' ')[0]
                        city = ''.join(constituency[0].split(' ')[1:len(constituency[0].split(' '))])


                        if city == 'D.I.':
                            city = 'D.I.Khan'


                    else:

                        const = constituency[1].split(' ')[0]
                        city = constituency[1].split(' ')[1]

                        if city == 'D.I.':
                            city = 'D.I.Khan'

                except Exception as e:

                    pass

            if 'NA-' in row[1:len(row)][0]:


                startAppend = True

                if row[1:len(row)][0] == 'NA-126-Lahore-IX':

                    const = 'NA-126'
                    city = 'Lahore-IX'

                elif row[1:len(row)][0] == 'NA-130-Lahore-XIII':

                    const = 'NA-130'
                    city = 'Lahore-XIII'

                else:

                    try:

                        constituency = row[1:len(row)]
                        if len(constituency[0].split(' ')) > 2:

                            const = constituency[0].split(' ')[0]
                            city = ''.join(constituency[0].split(' ')[1:len(constituency[0].split(' '))])

                            if city == 'D.I.':
                                city = 'D.I.Khan'

                        else:

                            const = constituency[0].split(' ')[0]
                            city = constituency[0].split(' ')[1]

                            if city == 'D.I.':
                                city = 'D.I.Khan'

                    except Exception as e:

                        pass



            if '%' in row[1:len(row)][-1]:

                if csvrow[0] in const_outlier:

                    turnout = row[4] + row[5]
                    csvrow.append(turnout)

                else:

                    turnout = row[3] + row[4]
                    csvrow.append(turnout)


            if 'Valid Votes' == [x.rstrip(' ') for x in row[1:len(row)]][1] :

                valid_votes = row[1:len(row)][2]
                csvrow.append(valid_votes)

            if 'Rejected Votes' == [x.rstrip(' ') for x in row[1:len(row)]][1] :

                if csvrow[0] in const_outlier:

                    rejected_votes = row[1:len(row)][3]
                    csvrow.append(rejected_votes)

                else:
                    rejected_votes = row[1:len(row)][2]
                    csvrow.append(rejected_votes)

            if 'Total Votes' == [x.rstrip(' ') for x in row[1:len(row)]][1]:

                total_votes = row[1:len(row)][2]
                csvrow.append(total_votes)

            if 'Registered Voters' == [x.rstrip(' ') for x in row[1:len(row)]][1]:

                registered_votes = row[1:len(row)][2]
                csvrow.append(registered_votes)

            if (startAppend):
                csvrow.append(const)
                csvrow.append(city)


            if len(csvrow)== 7:

                csvrow.append(year)

            if len(csvrow) == 8 :
                #print csvrow
                output.writerow(csvrow)
                csvrow = []

    return

if __name__ == '__main__':

    fileOutputCand=sys.argv[1]       #candidate file
    fileOutputVote = sys.argv[2]    #vote file

    candidate_outputFile = open(fileOutputCand, 'w')
    vote_outputFile = open(fileOutputVote,'w')
    get2002_ElectionResults(candidate_outputFile,vote_outputFile)

