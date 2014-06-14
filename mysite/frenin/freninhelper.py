'''
from freninhelper import freninhelper
fr=freninhelper('foulspawn')
fr.getMatches()
#fr.is_valid
#fr.getMatches()
fr.saveMatches()


'''
import requests
import json
from pprint import pprint

class freninhelper(object):
    def __init__(self,name):
        print name
        self.name = name.lower()
        by_match='https://eune.api.pvp.net/api/lol/eune/v1.3/game/by-summoner/{}/recent?api_key=1ad65669-6d27-49e3-94bc-bcab5fde0644'
        by_name='https://eune.api.pvp.net/api/lol/eune/v1.4/summoner/by-name/{}?api_key=1ad65669-6d27-49e3-94bc-bcab5fde0644'
        by_name=by_name.format(self.name)
        self.resp=requests.get(by_name)
        print "got by name"
        if self.resp.status_code==200:
            self.is_valid=True
            print "is_valid was set"
            jresp=json.loads(self.resp.content)
            print "got self.id"
            self.id=jresp[self.name]['id']
            print "...formatting..."
            by_match=by_match.format(self.id)
            print "got self.resp_matches"
            self.resp_matches=requests.get(by_match)
            print "got self.jresp_matches"
            self.jresp_matches=json.loads(self.resp_matches.content)
            print "fin"
        else:
            self.is_valid=False

    def getMatches(self):
        #pprint(self.jresp_matches)
        #'''
        if self.is_valid:
            self.mrow=[]
            for match in self.jresp_matches['games']:
                try:
                    chKills=str(match['stats']['championsKilled'])
                except KeyError:
                    chKills='0'
                try:
                    nuDeaths=str(match['stats']['numDeaths'])
                except KeyError:
                    nuDeaths='0'
                gaId=str(match['gameId'])
                self.mrow += [gaId+','+chKills+','+nuDeaths]
                print chKills,nuDeaths
            #SM(self.mrow,"data.csv")
                #for fellow in match['fellowPlayers']:
                #    print ""
                #    print fellow['summonerId']#'''
        else:
            print "is_valid is false"

    def saveMatches(self,mrow,place):
        #mrow should be a list[] each row is on item
        SM(mrow,place)

    def getLast(self):
        if self.is_valid:
            try:
                chKills=str(self.jresp_matches['games'][0]['stats']['championsKilled'])
            except KeyError:
                chKills='0'
            try:
                nuDeaths=str(self.jresp_matches['games'][0]['stats']['numDeaths'])
            except KeyError:
                nuDeaths='0'
            self.last_match=self.name+chKills+nuDeaths
            return self.last_match
        

#from freninhelper import SM
class SM(object):#mrow should be a list[] each row is on item
    def __init__(self,mrow,place):
        import csv
        with open('freezing-ninja-LoL/mysite/frenin/static/frenin/'+place, 'wb') as csvfile:
            print "starting file writting"
        #with open('data.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='-',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['State,Kills,Deaths'])
            for i in range(9):
                spamwriter.writerow([mrow[i]])
