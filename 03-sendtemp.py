# import package
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from songline import Sendline
from uncleengineer import thaistock


def Temperature(pid) :

    url = 'https://www.tmd.go.th/province.php?id={}'.format(pid);

    webopen = req(url); #open web
    page_html = webopen.read(); #read html
    webopen.close();

    data = soup(page_html, 'html.parser'); #convert to soup

    # print(data);

    province = data.select("span.title")
    province = province[0].text

    temp = data.find_all('td',{'class': 'strokeme'});
    temp = temp[0].text # .text for trim tag

    return 'จังหวัด: {}, อุณหภูมิ: {}'.format(province, temp);



# //// college text;

alltext = '';

for i in range(1,10) :
    try:
        text = Temperature(i)
        alltext = alltext + text + '\n' #add each text to alltext;
    except:
        print('Not found');

# //// test alltext

# print(alltext);


token = 'm7wHTQVaFdLju5MHW4rQgLpXSBaOMRcylCyRdwXzTvJ';
messenger = Sendline(token);

# //// send line

# messenger.sendtext(alltext);
# messenger.sendtext(thaistock('PTT'));
