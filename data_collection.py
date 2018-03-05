from bs4 import BeautifulSoup
import pandas as pd
import urllib2
import csv, json, sys,pdfquery
import re

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
    getVoteInformation_NA_2013(vote_2013)
    getPartyPositionInfo_NA_2013(party_2013)


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
                print csvrow
                output.writerow(csvrow)
                csvrow = []



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

    csvKeys = ['Constituency_No', 'Constituency_Name', 'Candidate_Name', 'Political_Party', 'Votes_Polled', 'Year',
               'Province']
    output = csv.writer(data)
    output.writerow(csvKeys)
    city = ""
    const= ""
    year = "2013"
    prov = ""
    csvrow=[]
    url_list=[]
    check=0
    base_url='http://www.electionpakistani.com/ge2013/NA-'
    outlier_list=['NA-210','NA-230','NA-262','NA-269']

    for i in range(1,273):
        count=i
        url=base_url+str(count)+'.htm'
        url_list.append(url)
    count=0
    na=0
    for url in url_list:
        print url
        check = 0
        na=na+1
        const='NA-'+str(na)
        city=""
        response=urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        try:

            table = soup.find('table',id="AutoNumber1")
            rows = table.findAll('tr')
            if len(rows)  == 1:
                if const in outlier_list:
                    rows = soup.findAll('tr')
                    append=-1

                    for row in rows:

                        csvrow = []
                        csvrow.append(const)
                        csvrow.append(city)
                        font_face = row.findAll('font')
                        for font in font_face:

                            font = font.text.encode('utf-8')
                            if font != "":
                                fonttext = ' '.join(font.split())
                                if fonttext == 'Votes':
                                    append = append + 1

                                if append == 0:
                                    if fonttext != 'Votes':
                                        csvrow.append(fonttext)
                        if len(csvrow) > 2:
                            csvrow.append(year)
                            csvrow.append("")
                            output.writerow(csvrow)

                elif const=='NA-254':
                    rows = soup.findAll('tr')
                    for row in rows:
                        csvrow = []
                        csvrow.append(const)
                        csvrow.append(city)
                        spans = row.findAll('span')
                        for span in spans:
                            span = span.text.encode('utf-8')
                            if span != "":
                                spantext = ' '.join(span.split())
                                if 'NA 254' not in spantext:
                                    csvrow.append(spantext)

                        if len(csvrow) > 2:
                            csvrow.append(year)
                            csvrow.append("")
                            output.writerow(csvrow)


                else:
                    raise Exception('This is the exception you expect to handle')
            else:
                for row in rows:   #skip first row
                    check=check+1

                    if (check >1):
                        count= count + 1
                        csvrow=[]
                        csvrow.append(const)
                        csvrow.append(city)
                        spans=row.findAll('span')

                        if len(spans) > 0:
                            if const=='NA-1' or const=='NA-3':
                                spanCount = 0
                                for span in spans:
                                    spanCount = spanCount + 1
                                    span = span.text.encode('utf-8')
                                    spantext = ' '.join(span.split())
                                    csvrow.append(spantext)

                                if spanCount == 2:
                                    fonts = row.findAll('font')

                                    if len(fonts) == 3:
                                        csvrow.append(fonts[2].text.encode('utf-8'))
                                    else:
                                        csvrow.append(fonts[0].text.encode('utf-8'))

                                csvrow.append(year)
                                csvrow.append("")
                                output.writerow(csvrow)
                            else:
                                # just for testing purposes
                                fonts = row.findAll('font')
                                if len(fonts) > 0:
                                    fonts = row.findAll('font')
                                    for font in fonts:
                                        font = font.text.encode('utf-8')
                                        fonttext = ' '.join(font.split())
                                        csvrow.append(fonttext)
                                    csvrow.append(year)

                                csvrow.append("")
                                output.writerow(csvrow)
                         #############################

                        else: #if no span tag then search for font tag

                            csvrow = []
                            csvrow.append(const)
                            csvrow.append(city)
                            font_face = row.findAll('font')
                            for font in font_face:

                                font = font.text.encode('utf-8')
                                if font != "":
                                    fonttext = ' '.join(font.split())
                                    csvrow.append(fonttext)

                            if len(csvrow) > 2:
                                if const == 'NA-38':
                                    csvrow.append("")
                                csvrow.append(year)
                                output.writerow(csvrow)


        except Exception as e :

            if const=='NA-138':

                table = soup.find('table', {"class": "MsoNormalTable"})
                rows = table.findAll('tr')
                for row in rows:
                    check = check + 1
                    if (check > 1):
                        count = count + 1
                        csvrow = []
                        csvrow.append(const)
                        csvrow.append(city)
                        fonts = row.findAll('font')
                        if len(fonts) > 0:
                            for font in fonts:
                                font = font.text.encode('utf-8')
                                fonttext = ' '.join(font.split())
                                if fonttext != "":
                                    csvrow.append(fonttext)
                            csvrow.append(year)
                            csvrow.append("")
                            output.writerow(csvrow)


            else:

                table = soup.find('table',  {"class" : "MsoNormalTable"})
                rows = table.findAll('tr')
                for row in rows:
                    check = check + 1
                    if (check > 1):
                        count = count + 1
                        csvrow = []
                        csvrow.append(const)
                        csvrow.append(city)
                        spans = row.findAll('span')
                        for span in spans:
                            span = span.text.encode('utf-8')
                            spantext = ' '.join(span.split())
                            if spantext!="":
                                csvrow.append(spantext)
                        csvrow.append(year)

                        csvrow.append("")
                        output.writerow(csvrow)   #scraped from hamariweb.com










def getVoteInformation_NA_2013(data):

    subset=False
    voteKeys = ['Constituency_No', 'Constituency_Name', 'Valid_Votes', 'Rejected_Votes', 'Total_Votes',
                'Registered_Voters', 'Turnout(%)', 'Year']
    output = csv.writer(data)
    output.writerow(voteKeys)
    valid_votes = ""
    rejected_votes = ""
    registered_votes = ""
    turnout = ""  # total/registered * 100
    total_votes = ""
    prev_value=0
    const=""
    city=""
    startAppend=False
    csvrow=[]
    outlier_check=0
    outlier_list=['NA-38','NA-46','NA-83','NA-237','NA-254']
    outlier_list2 = ['NA-229','NA-230']
    outlier_list3=['NA-103']
    year='2013'
    check=0
    check1=0
    count=0
    base_url='http://test1947.ecp.gov.pk/ConstResult.aspx?Const_Id=NA-'
    vote_url= []
    for i in range(1,272):
        count=i
        url=base_url+str(count)+'&type=NA'
        vote_url.append(url)

    #for url in vote_url:
    response = urllib2.urlopen('http://test1947.ecp.gov.pk/ConstResult.aspx?Const_Id=NA-1&type=NA')
    html = response.read()
    #print html
    soup = BeautifulSoup(html, 'html.parser')
    table=soup.findAll("table")
    print table


    # with open('Notification-National-Assembly.csv') as f:
    #     reader=csv.reader(f)
    #     for row in reader:
    #         row=filter(None,row)
    #         row=[x.rstrip() for x in row]
    #
    #         try:
    #             if 'NA-1' in row[0]:
    #                 subset = True
    #         except Exception as e:
    #             pass
    #
    #         if (subset and len(row) != 0):
    #
    #             startAppend = False
    #
    #             try:
    #                 if 'NA-' in row[0]:
    #                     startAppend = True
    #                     try:
    #
    #                         if row[0] == 'NA-126-Lahore-IX':
    #
    #                             const = 'NA-126'
    #                             city = 'Lahore-IX'
    #
    #
    #                         elif row[0] == 'NA-130-Lahore-XIII':
    #
    #                             const = 'NA-130'
    #                             city = 'Lahore-XIII'
    #
    #
    #
    #                         constituency = row[0]
    #
    #                         if len(constituency.split(' ')) > 2:
    #
    #                             const = constituency.split(' ')[0]
    #                             city = ''.join(constituency.split(' ')[1:len(constituency.split(' '))])
    #
    #                         else:
    #
    #                             const = constituency.split(' ')[0]
    #                             city = constituency.split(' ')[1]
    #
    #                     except Exception as e:
    #
    #                         pass
    #             except Exception as e:
    #                 pass
    #
    #             try:
    #
    #                 if (startAppend):
    #                     csvrow.append(const)
    #                     csvrow.append(city)
    #
    #                 if const in outlier_list:
    #
    #                     csvrow.append("")
    #                     csvrow.append("")
    #                     csvrow.append("")
    #                     csvrow.append("")
    #                     csvrow.append("")
    #                     csvrow.append(year)
    #                     output.writerow(csvrow)
    #                     csvrow = []
    #                     const=""
    #
    #
    #                 elif const in outlier_list3:
    #
    #                     check1=check1 + 1
    #                     if check1 == 3:
    #                         csvrow.append("")
    #                         csvrow.append("")
    #                         csvrow.append("")
    #                         csvrow.append("")
    #                         csvrow.append("")
    #                         csvrow.append(year)
    #                         output.writerow(csvrow)
    #                         csvrow = []
    #                         const = ""
    #
    #
    #                 elif const in outlier_list2:
    #                     check=check + 1
    #                     if (check == 18):
    #                         valid_votes = row[0]
    #                         rejected_votes = row[1]
    #                         total_votes = row[2]
    #                         csvrow.append(valid_votes)
    #                         csvrow.append(rejected_votes)
    #                         csvrow.append(total_votes)
    #                         csvrow.append("")
    #                         csvrow.append("")
    #                         csvrow.append(year)
    #                         output.writerow(csvrow)
    #                         csvrow = []
    #                         check=0
    #
    #                     elif check == 16 and const!='NA-229':
    #
    #                         valid_votes = row[0]
    #                         rejected_votes = row[1]
    #                         total_votes = row[2]
    #                         csvrow.append(valid_votes)
    #                         csvrow.append(rejected_votes)
    #                         csvrow.append(total_votes)
    #                         csvrow.append("")
    #                         csvrow.append("")
    #                         csvrow.append(year)
    #                         output.writerow(csvrow)
    #                         csvrow = []
    #                         check = 0
    #
    #                 else:
    #
    #                     if 'Total' in row:
    #
    #                         valid_votes = row[1]
    #                         rejected_votes=row[2]
    #                         total_votes = row[3]
    #                         csvrow.append(valid_votes)
    #                         csvrow.append(rejected_votes)
    #                         csvrow.append(total_votes)
    #                         csvrow.append("")
    #                         csvrow.append("")
    #                         csvrow.append(year)
    #                         output.writerow(csvrow)
    #                         csvrow=[]
    #
    #             except Exception as e:
    #                 pass



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
            year = '2013'
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

    #cand_2002 = open('canidate_2002.csv', 'w')
    #vote_2002 = open('votes_2002.csv', 'w')
    #party_2002 = open('party_2002.csv', 'w')

    #cand_2008=open('canidate_2008.csv','w')
    #vote_2008 = open('votes_2008.csv','w')
    #party_2008=open('party_2008.csv','w')

    #cand_2013=open('candidate_2013.csv','w')
    #vote_2013 = open('votes_2013.csv', 'w')
    #party_2013 = open('party_2013.csv', 'w')

    #get2002_ElectionResults_NA(cand_2002,vote_2002,party_2002)
    #get2008_ElectionResults_NA(cand_2008,vote_2008,party_2008)

    #get2013_ElectionResults_NA(cand_2013,vote_2013,party_2013)  #NA-7 vote not recorded of last candidate, NA-38 election postponed


    print "fuck"
