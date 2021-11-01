from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import imaplib
import email
import datetime
import os
from threading import Timer
from email.header import decode_header
import html2text
import pathlib
from socket import gaierror
from .models import Message
from .serializers import MessageSerializer


# TODO ATTACHMENT
# TODO SATI - dobro je valjda
# TODO DA LI SVI REGULARNI RADE
# TODO AKO NEMA POVRATNE VREDNOSTI FUNKCIJE PROBAJ DA ZAPISES U FAJL
# TODO ZASTITI SIFRU

# TODO DA LI SE SLIKE NE CUVAJU - trebalo bi da da
# TODO VIDI DA PROMENIS VREMENSKU ZONU DA BUDE TEXAS -5
# TODO PROBAJ DA VIDIS DA SE PRAVE FAJLOVI SAMI ZA SVAKI RAZLICIT DAN
# TODO VIDI GDE HOCE DA SE CUVAJU FAJLOVI
# TODO SAKRIJ SIFRU
# TODO VIDI STA CE BITI SA FRONTOM KAKO CES PODATKE VRACATI DA LI PREKO API-JA DA LI CUVAS U FAJL
# TODO PITATI NA KOM OPERATIVNOM SISTEMU CE KORISTITI


# Create your views here.
class IndexView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        response = Response("mozee", content_type="application/json");
        return response;


switcher = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Avg": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}


def sort_by_date(message):
    return message.date


# def ajust_time_zone(date):
#     date_splited = date.split()
#     time = date_splited[4]
#     time_zone = int(int(date_splited[5]) / 100)
#     print("TIME ZONE ", time_zone)
#     print("TIME ZONE TIP ", type(time_zone))
#     hours = int(time.split(":")[0])
#     print("HOURS ", hours)
#
#     return date


def get_inbox():
    print("Read mail {}".format(datetime.datetime.now()))
    host = 'imap.gmail.com'
    username = 'info@flixautotransport.com'
    password = '4*qMN3uN!!5Ny(@'
    # username = 'isaija97@gmail.com'
    # password = 'isaisa123'

    try:
        mail = imaplib.IMAP4_SSL(host)
    except EOFError as e:
        print(e)
        print("greska")
    except gaierror:
        print('oops')

    # mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")

    _, search_data = mail.search(None,
                                 'UNSEEN');  # donja crta je unpacking, nece se koristiti prva povratna vrednost
    my_messages = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')  # email format
        _, b = data[0]
        email_message = email.message_from_bytes(b)

        for header in ['subject', 'to', 'from', 'date']:
            if header != 'date':
                is_utf = decode_header(email_message['subject'])[0][1]
                print("IDE GAS ", is_utf)
                print("IDE DRUGI GAS ", decode_header(email_message[header])[0][0])
                print("IDE DRUGI GAS TIP ", type(decode_header(email_message[header])[0][0]))

                if is_utf:
                    print("IS UTF")
                    # if type(decode_header(email_message[header])[0][0]) == 'bytes':
                    print("HEADER ", header)
                    print("DECODED ", decode_header(email_message[header])[0][0])
                    print("TYPE OF DECODED ", type(decode_header(email_message[header])[0][0]))
                    if isinstance(decode_header(email_message[header])[0][0], str):
                        print("STR JE")
                        email_data[header] = email_message[header]
                    else:
                        print("NIJE STR")
                        email_data[header] = decode_header(email_message[header])[0][0].decode()
                else:
                    print("IS NOT UTF")
                    email_data[header] = email_message[header]
            elif header == 'date':
                email_data[header] = email_message[header] + " TZ"
                print("ZADNJI DATUM ", email_message[header])
                # email_data[header] = ajust_time_zone(email_message[header])

            #     date = email_message[header].split()
            #     month = switcher.get(date[2], "Invalid month")
            #     email_data['date'] = date[1] + "." + str(month) + "." + date[3] + ". " + date[4] + " " + date[5]
            #     print("DATEE ", email_data['date']) #-0700,
            #     broj = int(date[5])
            #     print("BROJ ", broj)
            #     print("TIP BROJA ", type(broj))
            #     broj = broj / 100
            #     print("DOBAR BROJ ", int(broj))
            #     time_splited = date[4].split(":")
            #     print("SATI ", time_splited[0])
            #     hours = int(time_splited[0]) + broj
            #     hours = str(hours)
            #     time = hours + ":" + time_splited[1] + ":" + time_splited[2]
            #     email_data['date'] = date[1] + "." + str(month) + "." + date[3] + time
            #     print("VREME ", email_data["date"])

            print("{}: {}".format(header, email_message[header]))

        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                print("TYPE text/plain")
                body = part.get_payload(decode=True)
                print("BODY ", body.decode(errors='ignore'))  # errors='ignore'
                email_data['body'] = body.decode(errors='ignore')

            elif part.get_content_type() == "text/html":
                print("TYPE text/html")
                html_body = part.get_payload(decode=True)
                # print(html_body.decode())
                email_data['html_body'] = html_body.decode(errors='ignore')
                email_data['body'] = html2text.html2text(email_data['html_body'])

            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            if "image" in part.get_content_type() or "video" in part.get_content_type() or "audio" in part.get_content_type():
                continue
            file_name = part.get_filename()
            if bool(file_name):
                attachments_path = os.path.join(pathlib.Path().resolve(), "Attachments")
                try:
                    os.mkdir(attachments_path)
                except OSError as error:
                    print(error)

                date_splited = email_data["date"].split()
                directory = date_splited[1] + " " + date_splited[2] + " " + date_splited[3]
                dir_path = os.path.join(attachments_path, directory)
                try:
                    os.mkdir(dir_path)
                except OSError as error:
                    print(error)
                file_path = os.path.join(dir_path, file_name)
                print("PATH ", pathlib.Path().resolve())
                if not os.path.isfile(file_path):
                    fp = open(file_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                print('Downloaded "{file}" from email titled "{subject}".'.format(file=file_name,
                                                                                  subject=subject))

        # keys = email_data.keys()
        # if 'body' in keys:
        #     print("IMA BODY")
        # else:
        #     print("NEMA BODY")
        #     email_data['body'] = html2text.html2text(email_data['html_body'])
        print("BODY ", email_data['body'])
        my_messages.append(email_data)

        print("ALL MESS")
        for mess in my_messages:
            print(mess)
            Message.objects.create(subject=mess['subject'], receiver=mess['to'], sender=mess['from'], date=mess['date'],
                                   body=mess['body'], html_body=mess['html_body'])
    return my_messages


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

    def ret(self):
        return self.function()


class ReadMailsView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        print("starting...")

        try:
            rt = RepeatedTimer(10, get_inbox)
            print("FUNCTIONALITY ", rt.function)
        except EOFError as e:
            print(e)
        print("RT ", rt)
        print("FUNCTION ", rt.function)
        print("END ", rt)

        response = Response("ide gas", content_type="application/json");
        return response;


class UnreadMessagesView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        messages = Message.objects.filter(read=False)
        for message in messages:
            print(message.subject)
            print(message.body)
            message.read = True
            message.save()
        serializer_class = MessageSerializer(messages, many=True)
        response = Response(serializer_class.data, content_type="application/json")
        return response;


class AllMessagesView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        messages = Message.objects.all();
        for message in messages:
            print(message.subject)
            print(message.body)
        serializer_class = MessageSerializer(messages, many=True)
        response = Response(serializer_class.data, content_type="application/json")
        # response = Response("baza", content_type="application/json");
        return response;


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import PermissionDenied
import jwt
from .models import User
from .serializers import UserSerializer


class TestView(APIView):
    def get(self, request):
        print("USER VIEW")
        print(request.COOKIES)
        token = request.COOKIES.get('jwt')
        print("TOKEN ", token);
        if not token:
            raise PermissionDenied('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise PermissionDenied('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        print(user)
        print("Is superuser ", user.is_superuser)
        # return Response("idemo", content_type="application/json")
        return Response(serializer.data)
