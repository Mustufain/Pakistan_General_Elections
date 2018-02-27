from bs4 import BeautifulSoup
import pandas as pd
import urllib2
import csv, json, sys,pdfquery

## This script collects data of general elections of 2002,2008,2013
## It contains National Assembly and Provincial Assembly elections results

## @author: Mustufain
## email: abbasmustufain@gmail.com


def get2002_ElectionResults_NA(candidate_outputFile,vote_outputFile,party_outputFile):

    # National Assembly 2002 Elections

    getCandidateInformation_NA_2002(candidate_outputFile)
    getVoteInformation_NA_2002(vote_outputFile)
    getPartyPositionInfo_NA_2002(party_outputFile)



def get2008_ElectionResults_NA(cand_2008,vote_2008,party_2008):

    getCandidateInformation_NA_2008(cand_2008)
    getVoteInformation_NA_2008(vote_2008)
    getPartyPositionInfo_NA_2008(party_2008)


def get2013_ElectionResults_NA(cand_2013,vote_2013,party_2013):

    getCandidateInformation_NA_2013(cand_2013)
    #getVoteInformation_NA_2013(vote_2013)
    #getPartyPositionInfo_NA_2013(party_2013)


def getCandidateInformation_NA_2002(data):

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

            if 'FEDERAL CAPITAL' in row[1]:
                prov='FEDERAL'

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

def getVoteInformation_NA_2002(data):

    outlier_list = ['NA-130-Lahore-XIII', 'NA-126-Lahore-IX']
    voteKeys = ['Constituency_No', 'Constituency_Name', 'Valid_Votes', 'Rejected_Votes', 'Total_Votes',
                'Registered_Voters', 'Turnout(%)', 'Year']
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

                    turnout = row[4]
                    csvrow.append(turnout)

                else:

                    turnout = row[3]
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

def getPartyPositionInfo_NA_2002(data):

    csvKeys=['Party','No_Of_Seats_Secured','Total_Votes_Secured','Seats_Won(%)','Party_Votes_By_Total_Valid_Votes(%)','Year']

    output = csv.writer(data)
    output.writerow(csvKeys)
    start = False
    csvrow=[]
    with open('Party_Position_NA.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:


            row = filter(None,row)
            row = [x.rstrip(' ') for x in row]

            if row[0] == '1':

                start = True

            if row[0] == 'TOTAL':

                start = False

            if (start):

                #Append here to csv
                csvrow.append(row[1])
                csvrow.append(row[2])
                csvrow.append(row[3])
                csvrow.append(row[4])
                csvrow.append(row[5])
                csvrow.append('2002')
                output.writerow(csvrow)
                csvrow = []

def getCandidateInformation_NA_2008(data):

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
    subset=False
    count=0
    check=0

    with open('2008.csv', 'rb') as f:
        reader = csv.reader(f)

        for row in reader:

            row=filter(None,row)
            row=[x.rstrip() for x in row]

            csvrow = []
            try:
                if 'NA-1' in row[0]:
                    subset=True
            except Exception as e:
                pass

            if(subset):



                if (prev_value == 0):
                    prev_value = prev_value + 1

                try:
                    if 'NA-' in row[0]:

                        try:

                            if row[0] == 'NA-126-Lahore-IX':

                                const = 'NA-126'
                                city = 'Lahore-IX'
                                prev_value = 0

                            elif row[0] == 'NA-130-Lahore-XIII':

                                const = 'NA-130'
                                city = 'Lahore-XIII'
                                prev_value = 0

                            prev_value = 0
                            constituency = row[0]

                            if len(constituency.split(' ')) > 2:

                                const = constituency.split(' ')[0]
                                city = ''.join(constituency.split(' ')[1:len(constituency.split(' '))])

                            else:

                                const = constituency.split(' ')[0]
                                city = constituency.split(' ')[1]

                        except Exception as e:

                            pass
                except Exception as e:
                    pass



                if (prev_value > 0):

                    if 'Valid Votes' in row[0]:
                        prev_value = -1
                        csvrow = []

                    else:
                        try:
                            if len(row) == 5:
                                name = row[1] + row[2]
                                pa = row[3]
                                vp=row[4]

                            else:
                                name=row[1]
                                pa = row[2]
                                vp = row[3]

                            year = '2008'

                            if city == 'D.I.':
                                city = 'D.I.Khan'

                            count=count + 1
                            #print count
                            csvrow.append(const)
                            csvrow.append(city)
                            csvrow.append(name)
                            csvrow.append(pa)
                            csvrow.append(vp)
                            csvrow.append(year)

                            if count < 265:
                                csvrow.append('KPK')

                            if count >= 265 and count<=448:

                                csvrow.append('FATA')

                            if 'Islamabad' in city:
                                csvrow.append('FEDERAL')

                            if count > 448 and count<=1465 and 'Islamabad' not in city:
                                csvrow.append('PUNJAB')

                            if count > 1465 and count<=2062:
                                csvrow.append('SINDH')


                            if count > 2062 and count<=2204:
                                csvrow.append('BALOCHISTAN')

                            ## test (small hack)
                            if const=='NA-272':

                                check=check + 1
                            ##
                            if check < 6:

                                output.writerow(csvrow)

                        except Exception as e:

                            pass

def getVoteInformation_NA_2008(data):

    outlier_list = ['NA-130-Lahore-XIII', 'NA-126-Lahore-IX']
    voteKeys = ['Constituency_No', 'Constituency_Name', 'Valid_Votes', 'Rejected_Votes', 'Total_Votes',
                'Registered_Voters', 'Turnout(%)', 'Year']
    output = csv.writer(data)
    output.writerow(voteKeys)
    const_outlier = ['NA-243', 'NA-244', 'NA-245']

    const = ""
    city = ""
    constituency = ""
    year = "2008"
    valid_votes = ""
    rejected_votes = ""
    registered_votes = ""
    turnout = ""
    total_votes = ""
    csvrow = []
    subset = False
    check=-1
    startAppend=False
    end=0

    with open('2008.csv', 'rb') as f:

        reader = csv.reader(f)
        for row in reader:

            row=filter(None,row)
            row=[x.rstrip() for x in row]

            try:
                if 'NA-1' in row[0]:
                    subset = True
            except Exception as e:
                pass

            if (subset):


                startAppend = False

                try:

                    if 'NA-1 Peshawar-1' == row[0] and check<0:

                        check=check + 1
                        startAppend=True
                        const = row[0].split(' ')[0]
                        city = row[0].split(' ')[1]

                    if 'NA-' in row[0] and 'NA-1 Peshawar-1'!=row[0]:

                        startAppend = True
                        constituency = row[0]

                        if len(constituency.split(' ')) > 2:

                            const = constituency.split(' ')[0]
                            city = ''.join(constituency.split(' ')[1:len(constituency.split(' '))])

                            if city == 'D.I.':
                                city = 'D.I.Khan'


                        else:

                            const = constituency.split(' ')[0]
                            city = constituency.split(' ')[1]

                            if city == 'D.I.':
                                city = 'D.I.Khan'

                except Exception as e:

                    pass

            try :


                if '%' in row[0]:
                    turnout = row[1]
                    csvrow.append(turnout)

                if 'Valid Votes' == row[0]:
                    valid_votes = row[1]
                    csvrow.append(valid_votes)

                if 'Rejected Votes' == row[0]:
                    rejected_votes = row[1]
                    csvrow.append(rejected_votes)

                if 'Total Votes' == row[0]:
                    total_votes = row[1]
                    csvrow.append(total_votes)

                if 'Regd. Voters' == row[0]:
                    registered_votes = row[1]
                    csvrow.append(registered_votes)

                if (startAppend):
                    csvrow.append(const)
                    csvrow.append(city)


                if csvrow[0] == 'NA-119':   #outliers

                    csvrow.append("")
                    csvrow.append("")
                    csvrow.append("")
                    csvrow.append("")
                    csvrow.append("")

                if csvrow[0] == 'NA-207':   #outliers

                    csvrow.append("")
                    csvrow.append("")
                    csvrow.append("")
                    csvrow.append("")
                    csvrow.append("")

                if len(csvrow) == 7:
                    csvrow.append(year)

                if len(csvrow) == 8:

                    end = end + 1

                    if end < 272:

                        output.writerow(csvrow)
                        csvrow = []

            except Exception as e:
                pass
    return

def getPartyPositionInfo_NA_2008(data):

    csvKeys = ['Party', 'No_Of_Seats_Secured', 'Total_Votes_Secured', 'Seats_Won(%)',
               'Party_Votes_By_Total_Valid_Votes(%)', 'Year']

    output = csv.writer(data)
    output.writerow(csvKeys)
    csvrow=[]
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/Pakistani_general_election,_2008')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    party=soup.find("table", {"class" : "wikitable"})
    for row in party.findAll('tr'):
        col=row.findAll('td')
        csvrow=[]

        try:
            party=col[0].text
            votes=col[1].text
            percent=col[2].text
            seats= col[3].text
            seats_won_per=round(float(seats)/float(271)*100,1)
            year='2008'
            #print seats_won_per
            csvrow.append(party)
            csvrow.append(seats)
            csvrow.append(votes)
            csvrow.append(seats_won_per)
            csvrow.append(percent)
            csvrow.append(year)

            if party!='Total':

                output.writerow(csvrow)
        except Exception as e:
            pass

def getCandidateInformation_NA_2013(data):

    outlier_list = ['NA-130-Lahore-XIII', 'NA-126-Lahore-IX']
    csvKeys = ['Constituency_No', 'Constituency_Name', 'Candidate_Name', 'Political_Party', 'Votes_Polled', 'Year',
               'Province']
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
    subset = False
    count = 0
    check = 0
    row_outlier=['2','8640','8990']
    name_outlier=['Ch. Nisar Ali Khan','Ch. Jaffar Iqbal','Tahir Iqbal Ch.','Makhdoomzada S.B.A. Sultan','Syed Naveed QamarShah','Dr. Muhammad Farooq Sattar','Abdul Hakeem Balouch','Molana Qamar ud Din']
    cand_outlier=['Syed Haziq Ali Shah']
    test=0 #testing

    with open('Notification-National-Assembly.csv') as f:
        reader=csv.reader(f)
        for row in reader:
            row=filter(None,row)
            row=[x.rstrip() for x in row]

            csvrow = []
            try:
                if 'NA-1' in row[0]:
                    subset = True
            except Exception as e:
                pass

            if (subset and len(row)!=0):


                if (prev_value == 0):
                    prev_value = prev_value + 1

                try:
                    if 'NA-' in row[0]:

                        try:

                            if row[0] == 'NA-126-Lahore-IX':

                                const = 'NA-126'
                                city = 'Lahore-IX'
                                prev_value = 0

                            elif row[0] == 'NA-130-Lahore-XIII':

                                const = 'NA-130'
                                city = 'Lahore-XIII'
                                prev_value = 0

                            prev_value = 0
                            constituency = row[0]

                            if len(constituency.split(' ')) > 2:

                                const = constituency.split(' ')[0]
                                city = ''.join(constituency.split(' ')[1:len(constituency.split(' '))])

                            else:

                                const = constituency.split(' ')[0]
                                city = constituency.split(' ')[1]

                        except Exception as e:

                            pass
                except Exception as e:
                    pass

                if (prev_value > 0):
                    try:
                        if 'Total' in row:
                            prev_value = -1
                            csvrow = []
                    except Exception as e:
                        pass

                    else:
                        try:
                            if prev_value!=-1 and row[1] not in row_outlier:

                                if len(row) ==3:
                                    name=row[1]
                                    vp=row[2]

                                if len(row) ==4:

                                    firstString = row[1].lower()
                                    secondString=row[3].lower()

                                    if firstString == secondString or firstString in secondString or row[1] in name_outlier:

                                        name = row[1]
                                        vp = row[2]


                                    else:

                                        name=row[1]+row[2]
                                        vp=row[3]


                                pa = ""
                                year = '2013'

                                if city == 'D.I.':
                                    city = 'D.I.Khan'

                                count = count + 1

                                if name in cand_outlier:
                                    const='NA-39'
                                csvrow.append(const)
                                csvrow.append(city)
                                csvrow.append(name)
                                csvrow.append(pa)
                                csvrow.append(vp)
                                csvrow.append(year)

                            if count < 517:

                                prov='KPK'
                                #print count, ':', prov
                                csvrow.append(prov)

                            elif count >= 517 and count <= 808:
                                prov='FATA'
                                #print count, ':', prov
                                csvrow.append(prov)

                            elif 'ISLAMABAD' in city:
                                prov='FEDERAL'
                                #print count, ':', prov
                                csvrow.append(prov)

                            elif count > 885 and count <= 3159 and 'ISLAMABAD' not in city:
                                prov='PUNJAB'
                                #print count, ':', prov
                                csvrow.append(prov)

                            elif count > 3159 and count <= 4207:
                                prov='SINDH'
                                #print count, ':', prov
                                csvrow.append(prov)

                            elif count > 4207 and count <= 4494:
                                prov='BALOCHISTAN'
                                #print count, ':', prov
                                csvrow.append(prov)


                            ## test (small hack)
                            if const == 'NA-272':
                                check = check + 1
                            ##
                            if check < 14:
                                if len(csvrow)>1:  ##small hack

                                    output.writerow(csvrow)

                        except Exception as e:

                            pass





def getVoteInformation_NA_2013(data):

    return

def getPartyPositionInfo_NA_2013(data):
    csvKeys = ['Party', 'No_Of_Seats_Secured', 'Total_Votes_Secured', 'Seats_Won(%)',
               'Party_Votes_By_Total_Valid_Votes(%)', 'Year']

    output = csv.writer(data)
    output.writerow(csvKeys)
    csvrow = []
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/Pakistani_general_election,_2013')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    party = soup.findAll("table", {"class": "wikitable"})
    for row in party[2].findAll('tr'):
        col = row.findAll('td')
        csvrow = []

        try:
            party = col[0].text
            votes = col[1].text
            percent = col[2].text
            seats = col[3].text
            seats_won_per = round(float(seats) / float(271) * 100, 1)
            year = '2008'
            # print seats_won_per
            csvrow.append(party)
            csvrow.append(seats)
            csvrow.append(votes)
            csvrow.append(seats_won_per)
            csvrow.append(percent)
            csvrow.append(year)

            if party != 'Total':
                output.writerow(csvrow)
        except Exception as e:
            pass





if __name__ == '__main__':

    #fileOutputCand=sys.argv[1]       #candidate file
    #fileOutputVote = sys.argv[2]    #vote file
    #fileOutputParty = sys.argv[3]   #Party Position file



    #candidate_outputFile = open(fileOutputCand, 'w')
    #vote_outputFile = open(fileOutputVote,'w')
    #part_outputFile = open(fileOutputParty,'w')

    #cand_2008=open('canidate_2008.csv','w')
    #vote_2008 = open('votes_2008.csv','w')
    #party_2008=open('party_2008.csv','w')

    cand_2013=open('candidate_2013.csv','w')
    vote_2013 = open('votes_2013.csv', 'w')
    party_2013 = open('party_2013.csv', 'w')

    #get2002_ElectionResults_NA(candidate_outputFile,vote_outputFile,part_outputFile)
    #get2008_ElectionResults_NA(cand_2008,vote_2008,party_2008)


    get2013_ElectionResults_NA(cand_2013,vote_2013,party_2013)

