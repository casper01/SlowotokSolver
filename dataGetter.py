import requests
import settings
import json
import re


class DataDownloader:
    @staticmethod
    def downloadLetters():
        """
        Download letters directly from slowotok.pl server
        """
        url = 'https://slowotok.pl/Account/LogOn?ReturnUrl=%2fplay%2fboard'
        values = {
            'Email': settings.USER_EMAIL,
            'Password': settings.USER_PASS
        }
        r = requests.post(url, data=values)
        data = json.loads(r.text)
        return data['Letters']

    @staticmethod
    def getLocalLetters():
        """
        Get letters from local file.
        Extract all letters of html that are actual game letters
        Those letters are between 2 tags.
        So we search for letter after > (closing tag) and before next  < (opening tag) 
        """
        with open(settings.READFILE, 'r') as f:
            text = f.read()
        return re.findall('(?<=>)[A-Z,Ą,Ć,Ę,Ł,Ń,Ó,Ś,Ź,Ż](?=<)', text)
