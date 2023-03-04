# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt



def tryAnother():
    import xmltodict
    import pprint

    # Open the file and read the contents


    with open('JS-002 (55pF)_20221128091004.result.xml', 'r', encoding='utf-8') as file:
        my_xml = file.read()

    # Use xmltodict to parse and convert
    # the XML document
    my_dict = xmltodict.parse(my_xml)
    x=[]
    y=[]
    i=0
    # Print the dictionary
    pprint.pprint(len(my_dict['result']['dataSection']['res'][9]['waveForm']['waveformContainer'][0]['rawWaveForm']['dp']), indent=2)
    #print((my_dict['result']['dataSection']))
    for i in range(len((my_dict['result']['dataSection']['res'][9]['waveForm']['waveformContainer'][0]['rawWaveForm']['dp']))):
        y.append(float(my_dict['result']['dataSection']['res'][9]['waveForm']['waveformContainer'][0]['rawWaveForm']['dp'][i]['@y']))
        x.append(float(my_dict['result']['dataSection']['res'][9]['waveForm']['waveformContainer'][0]['rawWaveForm']['dp'][i]['@x']))
        #x.append(i)
        #print(i)


    print(x)
    print(y)
    #plt.scatter(x, y, label="stars", color="green",
     #           marker="*", s=30)
    #plt.yscale('linear')

    fig, ax = plt.subplots()
    ax.plot(x, y)

    plt.xlabel('Over time')
    plt.ylabel("Pulses")
    plt.title("Pulse WaveForm")
    #plt.grid()
    plt.show()

def tryThis():

# Passing the path of the
# xml document to enable the
# parsing process
    tree = ET.parse('topnewsfeed.xml')

# getting the parent tag of
# the xml document
    root = tree.getroot()

# printing the root (parent) tag
# of the xml document, along with
# its memory location
    print(tree)
    print(root)

# printing the attributes of the
# first tag from the parent
  #  print(root[0].attrib)

# printing the text contained within
# first subtag of the 5th tag from
# the parent
    #print(root[5][0].text)

def loadRSS():
    # url of rss feed
    url = 'two.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel/item'):

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:

            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

        # append news dictionary to news items list
        newsitems.append(news)

    # return news items list
    return newsitems


def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(newsitems)

def printItems(newsitems, filename):


    with open(filename, 'r') as file:

        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)




def main():
    # load rss from web to update existing xml file
   # loadRSS()

    # parse xml file
   # newsitems = parseXML('topnewsfeed.xml')

    # store news items in a csv file
   # savetoCSV(newsitems, 'topnews.csv')

    #printItems(newsitems,'topnews.csv')
    tryAnother()


if __name__ == "__main__":
    # calling main function
    main()