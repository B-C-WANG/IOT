# coding=utf-8
import sys
import time
import poplib
import smtplib
import os
import sys
import time
import poplib
import smtplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr



__g_codeset = sys.getdefaultencoding()
if "ascii" == __g_codeset:
    __g_codeset = locale.getdefaultlocale()[1]


from email.mime.text import MIMEText
import email.mime.multipart
import email.mime.base
import random

def decode_str(s):
  value, charset = decode_header(s)[0]
  if charset:
    value = value.decode(charset)
  return value


def print_info(msg, indent=0):
    data = []
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            #print('%s%s: %s' % (' ' * indent, header, value))
            data.append(value)

    sender = data[0].split('<')[1].split('>')[0]
    info = data[2]
    print(sender, info)
    return sender, info

class emailSend():
    def __init__(self,smtp,sender,password):
        self.smtp = smtp
        self.sender = sender
        self.password = password

    #send text message, return 1 if succeed.
    def send_text(self,subject,_from,_to,information):
        try:
            print('Email is trying to sending')
            SMTPserver = self.smtp
            sender = self.sender
            password = self.password
            message = information
            msg = MIMEText(message)

            msg['Subject'] = subject
            msg['From'] = _from
            msg['To'] = _to

            mailserver = smtplib.SMTP(SMTPserver, 25)
            mailserver.login(sender, password)
            mailserver.sendmail(sender, _to, msg.as_string())
            mailserver.quit()
            print('Send success!')

            return 1
        except:
            print("Send failed.")
            return 0

class email_receive():
    def __init__(self,pop,user,password):
        self.pop = pop
        self.user = user
        self.password = password
        self.info_set = ()
#   写入文件，每一段时间检测的最新邮件数目，等待时间，总共receive的时间
    def receive_mail(self,write_info_to_file,mail_number_detect):

        p = poplib.POP3(self.pop)
        p.user(self.user)
        p.pass_(self.password)
        ret = p.stat()
        #print (ret)
        number = int(ret[0])

        sender_list = []
        information = []

        iter = min(mail_number_detect,number)


        for i in range(iter):
            j = number - i
            resp, lines, octets = p.retr(j)

            temp = lines
            #print("temp is",temp)

            if not temp in self.info_set:
                self.info_set+=(temp,)
                msg_content = ''
                for i in lines:
                    msg_content += i.decode('utf-8') + '\r\n'
                msg = Parser().parsestr(msg_content)
                sender, info = print_info(msg, 0)
                sender_list.append(sender)
                information.append(info)

        file = open(write_info_to_file,"w")
        _str = ""
        #print("info_set is",self.info_set)
        for i in self.info_set:
            for j in i:
                _str=_str+str(j)
            _str+="分隔符"
        file.write(_str)
        file.close()
        print(sender_list, information)
        p.quit()
        return sender_list, information






#测试
def test1():
    temp  = emailSend(smtp='**@**.com',
                          sender='***',password='***')
    temp.send_text(subject="***",_from="***",_to="***@***.com",information="***")



#每5秒检测前三个邮件，如果是新邮件，return的sender和information就是有效的，一开始会返回三个已有的邮件
#邮件信息会存储在write_info_to_file这个文件中，
def test2():
    temp = email_receive(pop= '***@***.com',
    user='***@***.com',
    password='***')

    for i in range(3):
        temp.receive_mail(write_info_to_file="***.txt",mail_number_detect=3)
        time.sleep(5)



test2()

