import requests 
import json
import base64
import urllib3
from st2common.runners.base_action import Action

class sActs(Action):

    def run(self):
        URL = "https://192.168.9.174/auth/v1/tokens"
 
        user = 'st2admin'
        password = 'M1cr0123'
        usrPass = user+":"+password
        endcoded_u = base64.b64encode(usrPass.encode('utf-8'))
        #base64encodedData = new Buffer(user + ':' + password).toString('base64')
        headers = {
        'Authorization' : "Basic "+str(endcoded_u.decode('UTF-8'))
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        r = requests.post(url = URL , headers=headers, verify=False)
        res=r.text
        res1=json.loads(res)
        token = res1['token']

        url ="https://192.168.9.174/api/v1/actions"
        #base64encodedData = new Buffer(user + ':' + password).toString('base64')
        endcoded_u = base64.b64encode(token.encode('utf-8'))
        # #base64encodedData = new Buffer(user + ':' + password).toString('base64')
        headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'python-requests/2.9.1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'X-Auth-Token': token
        }
        # headers={'Content-Type':'application/json',
        #                'Authorization': 'Bearer {}'.format(token)}
        # header = {'Authorization': 'Bearer aa83dc33de6347ee990ca1ba2cd7cdf3' }
        result = requests.get(url,headers=headers, verify = False)
        res2=result.text
        res3=json.loads(res2)
        for i in range(243):
            print (res3[i]['name'])
        return True




