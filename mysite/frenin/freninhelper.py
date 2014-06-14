'''
from freninhelper import freninhelper
#fr=freninhelper('Crides')
#fr.is_valid
#fr.getMatches()
fr.saveMatches()


'''
import requests
import json
from pprint import pprint

class freninhelper(object):
    def __init__(self):
        pass
    def __init__(self,name):
        self.name = name.lower()
        by_match='https://eune.api.pvp.net/api/lol/eune/v1.3/game/by-summoner/{}/recent?api_key=1ad65669-6d27-49e3-94bc-bcab5fde0644'
        by_name='https://eune.api.pvp.net/api/lol/eune/v1.4/summoner/by-name/{}?api_key=1ad65669-6d27-49e3-94bc-bcab5fde0644'
        by_name=by_name.format(self.name)
        self.resp=requests.get(by_name)
        if self.resp.status_code==200:
            self.is_valid=True
        else:
            self.is_valid=False
        jresp=json.loads(self.resp.content)
        self.id=jresp[self.name]['id']
        by_match=by_match.format(self.id)
        self.resp_matches=requests.get(by_match)
        self.jresp_matches=json.loads(self.resp_matches.content)

    def getMatches(self):
        #pprint(self.jresp_matches)
        for match in self.jresp_matches['games']:
            print match['stats']['championsKilled'],match['stats']['numDeaths']
            for fellow in match['fellowPlayers']:
                print ""
                print fellow['summonerId']

#from freninhelper import SM
class SM(object):
    def __init__(self):
        import csv
        with open('data.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='-',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['State,Deaths,Kills'])
            spamwriter.writerow(['Crides,4,5,7,10'])
