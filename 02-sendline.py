# import package
from songline import Sendline


token = 'm7wHTQVaFdLju5MHW4rQgLpXSBaOMRcylCyRdwXzTvJ'
messenger = Sendline(token)

#messenger.sendtext('ไม่วู้')
#messenger.sticker(173,2)

img = 'https://static.posttoday.com/media/content/2017/11/23/35B73BCDE4784DB6836C26E43BF54395_1000.jpg';

messenger.sendimage(img);
