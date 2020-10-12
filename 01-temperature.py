# import package
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup


# m7wHTQVaFdLju5MHW4rQgLpXSBaOMRcylCyRdwXzTvJ

def Temperature(pid) :

    url = 'https://www.tmd.go.th/province.php?id={}'.format(pid);

    webopen = req(url); #open web
    page_html = webopen.read(); #read html
    webopen.close();

    data = soup(page_html, 'html.parser'); #convert to soup

    # print(data);

    '''
    <TD width='100%' align='left' style='FONT-SIZE:40px;
    color: #F6E207; padding-left:25px;' class='strokeme'>28.2 &deg;C</TD>
    '''

    province = data.select("span.title")
    province = province[0].text

    temp = data.find_all('td',{'class': 'strokeme'});
    temp = temp[0].text # .text for trim tag

    print(province, temp);

    #bkk = ' กรุงเทพ';
    #print(bkk);
    #bkk = bkk.strip();
    #print(bkk);
    #bkk = bkk.replace(' ', '');
    #print(bkk);
    #bkk = bkk.replace('พ', 'ย');
    #print(bkk);

#Temperature(37)

for i in range(77) :
    print(i)
    try:
        Temperature(i);
    except:
        print('Not Found');
    print('---')


