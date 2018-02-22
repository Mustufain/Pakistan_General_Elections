from bs4 import BeautifulSoup
import pandas as pd
import urllib2
import csv, json, sys

## This script collects data of general elections of 2002,2008,2013
## It contains National Assembly and Provincial Assembly elections results

## @author: Mustufain
## email: abbasmustufain@gmail.com


def get2002_ElectionResults(data,outputFile):

    # National Assembly 2002 Elections

    outlier_list=['NA-130-Lahore-XIII','NA-126-Lahore-IX']
    csvKeys=['Constituency_No','Constituency_Name','Candidate_Name','Political_Party','Votes_Polled','Year','Province','Sex']
    output = csv.writer(outputFile)
    output.writerow(csvKeys)
    prev_value=-1
    csvrow=[]
    const= ""
    city= ""
    constituency = ""
    name = ""
    pa = ""
    vp = ""
    year = ""
    count = 0
    prov = ""
    with open('National.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            count = count + 1

            csvrow = []

            if 'NWFP' in row[1]:
                prov = 'KPK'

            if 'FEDERALLY ADMINISTERED' in row[1]:

                prov = 'FATA'

            if 'PUNJAB' in row[1]:

                prov = 'PUNJAB'

            if 'SINDH PROVINCE' in row [1]:

                prov = 'SINDH'

            if 'BALOCHISTAN PROVINCE' in row[1]:

                prov = 'BALOCHISTAN'

            if (prev_value==0):

                prev_value = prev_value + 1

            if 'NA-' in row[1:len(row)][1]:

                try :


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
                    try :

                        prev_value=0
                        constituency = row[1:len(row)]
                        if len(constituency[0].split(' ')) > 2 :

                            const = constituency[0].split(' ')[0]
                            city = ''.join(constituency[0].split(' ')[1:len(constituency[0].split(' '))])

                        else:
                            const=constituency[0].split(' ')[0]
                            city=constituency[0].split(' ')[1]

                    except Exception as e:

                        pass

            #if '%' in row[1:len(row)][-1]: #use this when preparing votes.csv file

               #print row[1:len(row)]
               #prev_value = -1
               #csvrow=[]



            if (prev_value >0):

                if 'Valid Votes' in row[1:len(row)]:
                    prev_value = -1
                    csvrow = []

                else:

                    name = row[1:len(row)][0]
                    pa= row[1:len(row)][1]
                    vp=row[1:len(row)][2]
                    year='2002'

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

def get2008_ElectionResults():

    return

def get2013_ElectionResults():

    return


if __name__ == '__main__':

    #fileInput=sys.argv[1]       #xml file
    #fileOutput = sys.argv[2]    #csv file

    with open('output.json') as data_file:
        data = json.load(data_file)

    outputFile = open('candidates.csv', 'w')
    get2002_ElectionResults(data,outputFile)

