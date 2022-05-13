import requests,random,time,threading,os

AUTHOR = """
THIS WAS DEVELOPED BY VIBEX#0001 A LONG TIME AGO
"""

class Captcha:

    def cap2():

        key = 'ENTER KEY'

        r = requests.post(
            f'http://2captcha.com/in.php?key={key}&method=hcaptcha&sitekey=4c672d35-0701-42b2-88c3-78380b0db560&pageurl=https://discord.com/api/v9/auth/register'
        )
        
        taskid = r.text.split('|')[1]

        while True:
            time.sleep(2)

            r = requests.post(
                f'http://2captcha.com/res.php?key={key}&action=get&id={taskid}'
            )
            if 'OK|' in r.text:
                fc_token = r.text.split('OK|')[1]
                return fc_token

class Email:

    def key():
        cookies = {
            'version': 'eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D',
            '__gads': 'ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg',
            'XSRF-TOKEN': 'eyJpdiI6Ikw5bm5EVS9wZXRCbm1pcU9JSkxPTUE9PSIsInZhbHVlIjoiaHpJSk9ZQXdGTHFmcDRaZXQrTHIvVVgvSlJvbVZ3dFpWeGpLVmZLQ01HNlZ6WWFjTEYvdWh2dXNrdGsrMklmNEEwbUFBenVENi9UWXJzMWZFaUdYYWlDWW9DT1p4bngxUHRvWldhOHdlY3dMU3JhbWtUZGtrRVZjT05jNXd3Vm4iLCJtYWMiOiI2NTM3YTYxYzU3NTU4OTQ5MjFlMGFiYjQzNjY0NzU0MTRmZGYxMzRmYmM3NDVlODUxZjI0NWUxNGI1NGZhMDE1In0%3D',
            'sonjj_session': 'eyJpdiI6ImZRRUQybVI1eUZxVUI3dnVmY2dhT3c9PSIsInZhbHVlIjoiYmVBcHVCbE0vVU1GZE1ySEl4YXV0eGxvRWhNNDVLZTlCdVFhL3haTEFDNUdoVUNIYVVWZjgwWTE5dzBtb0VBS3M3RndUbTZVMjVUS2dlY3BuOFRSWHhTaTJ2cFM2OE5pQzB3a0JkbjJXZUhNZFo0VEM0ZTdTaHNGbS8yejlpS1EiLCJtYWMiOiJkNWUwMWM3YzdhYjk0MzQ1Mjc3ZThjY2RlZTQzZmJjZjI1YjVhZGI4OWQ3ZjllNDJhOWI1YjllYmJiNTRmNDEwIn0%3D',
        }

        headers = {
            'authority': 'smailpro.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'version=eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D; __gads=ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg; XSRF-TOKEN=eyJpdiI6Ikw5bm5EVS9wZXRCbm1pcU9JSkxPTUE9PSIsInZhbHVlIjoiaHpJSk9ZQXdGTHFmcDRaZXQrTHIvVVgvSlJvbVZ3dFpWeGpLVmZLQ01HNlZ6WWFjTEYvdWh2dXNrdGsrMklmNEEwbUFBenVENi9UWXJzMWZFaUdYYWlDWW9DT1p4bngxUHRvWldhOHdlY3dMU3JhbWtUZGtrRVZjT05jNXd3Vm4iLCJtYWMiOiI2NTM3YTYxYzU3NTU4OTQ5MjFlMGFiYjQzNjY0NzU0MTRmZGYxMzRmYmM3NDVlODUxZjI0NWUxNGI1NGZhMDE1In0%3D; sonjj_session=eyJpdiI6ImZRRUQybVI1eUZxVUI3dnVmY2dhT3c9PSIsInZhbHVlIjoiYmVBcHVCbE0vVU1GZE1ySEl4YXV0eGxvRWhNNDVLZTlCdVFhL3haTEFDNUdoVUNIYVVWZjgwWTE5dzBtb0VBS3M3RndUbTZVMjVUS2dlY3BuOFRSWHhTaTJ2cFM2OE5pQzB3a0JkbjJXZUhNZFo0VEM0ZTdTaHNGbS8yejlpS1EiLCJtYWMiOiJkNWUwMWM3YzdhYjk0MzQ1Mjc3ZThjY2RlZTQzZmJjZjI1YjVhZGI4OWQ3ZjllNDJhOWI1YjllYmJiNTRmNDEwIn0%3D',
            'origin': 'https://smailpro.com',
            'referer': 'https://smailpro.com/advanced',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
            'x-xsrf-token': 'eyJpdiI6Ikw5bm5EVS9wZXRCbm1pcU9JSkxPTUE9PSIsInZhbHVlIjoiaHpJSk9ZQXdGTHFmcDRaZXQrTHIvVVgvSlJvbVZ3dFpWeGpLVmZLQ01HNlZ6WWFjTEYvdWh2dXNrdGsrMklmNEEwbUFBenVENi9UWXJzMWZFaUdYYWlDWW9DT1p4bngxUHRvWldhOHdlY3dMU3JhbWtUZGtrRVZjT05jNXd3Vm4iLCJtYWMiOiI2NTM3YTYxYzU3NTU4OTQ5MjFlMGFiYjQzNjY0NzU0MTRmZGYxMzRmYmM3NDVlODUxZjI0NWUxNGI1NGZhMDE1In0=',
        }

        json_data = {
            'domain': 'gmail.com',
            'username': 'random',
            'server': 'server-1',
            'type': 'alias',
        }

        response = requests.post('https://smailpro.com/app/key', headers=headers, cookies=cookies, json=json_data).json()
        return response["items"]

    def mail():
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://smailpro.com',
            'Referer': 'https://smailpro.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-rapidapi-ua': 'RapidAPI-Playground',
        }

        params = {
            'key': Email.key(),
            'rapidapi-key': 'f871a22852mshc3ccc49e34af1e8p126682jsn734696f1f081',
            'domain': 'gmail.com',
            'username': 'random',
            'server': 'server-1',
            'type': 'alias',
        }

        response = requests.get('https://public-sonjj.p.rapidapi.com/email/gm/get', headers=headers, params=params).json()
        return response['items']['email']
    
    def key2(mailx):
        cookies = {
            'version': 'eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D',
            '__gads': 'ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg',
            'XSRF-TOKEN': 'eyJpdiI6IjZINmRlVFp2SWhkV1Y5eFBIMXJzVUE9PSIsInZhbHVlIjoiaDZKenJGTzN5Y1M2V1hueDh5eHkxMjRuRUkvU3JPeWlzSjB5WnJJaUNrMnhWU0Z2Zk5DN3B4aE90MkdaM2pYcllXMHdrb3hhU01PWWkxWnFnMG5pNTFrMjJsemw3V0dSV2FHTTE1NDlnNnd3cDByMlVZOW5FanJIckp0Y0xiRW0iLCJtYWMiOiJlYTIzYzAwM2IyZThhNTQ5ZTdlZWUxYjExMjkwZjBlYjc4YWQ0MmYzZTFlNDliMWE0ZGY4M2RjNWRkMWU4NDU0In0%3D',
            'sonjj_session': 'eyJpdiI6Ik4raURLRFpxN2NxQW40Yzk0RHNDc0E9PSIsInZhbHVlIjoiNWx2Y3I2eXROUkwyUkRUc2ZOQmYzV01VWGFBeVFFdERvd1k5NjRtOVdwTFdFNWxPVU9NRVZ0UVJjZWpzZTRzWjcxUVVLTDdYWGZ5cnlyeUY4bm14U0d4YXdoQU5kZlA1b3pIbkxEbTd5RVVEc1FqRWhHUXpPYzd5Mk1pUHlFMTMiLCJtYWMiOiJjODQ1OGJlYTBkN2U1YmFmMjI5ZjQ0MjM2NzZiZjQ3N2MxYzUxODkzMjg4YWVlZjk2N2M5ZTk1OTI4NmVmYzY2In0%3D',
        }

        headers = {
            'authority': 'smailpro.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'version=eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D; __gads=ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg; XSRF-TOKEN=eyJpdiI6IjZINmRlVFp2SWhkV1Y5eFBIMXJzVUE9PSIsInZhbHVlIjoiaDZKenJGTzN5Y1M2V1hueDh5eHkxMjRuRUkvU3JPeWlzSjB5WnJJaUNrMnhWU0Z2Zk5DN3B4aE90MkdaM2pYcllXMHdrb3hhU01PWWkxWnFnMG5pNTFrMjJsemw3V0dSV2FHTTE1NDlnNnd3cDByMlVZOW5FanJIckp0Y0xiRW0iLCJtYWMiOiJlYTIzYzAwM2IyZThhNTQ5ZTdlZWUxYjExMjkwZjBlYjc4YWQ0MmYzZTFlNDliMWE0ZGY4M2RjNWRkMWU4NDU0In0%3D; sonjj_session=eyJpdiI6Ik4raURLRFpxN2NxQW40Yzk0RHNDc0E9PSIsInZhbHVlIjoiNWx2Y3I2eXROUkwyUkRUc2ZOQmYzV01VWGFBeVFFdERvd1k5NjRtOVdwTFdFNWxPVU9NRVZ0UVJjZWpzZTRzWjcxUVVLTDdYWGZ5cnlyeUY4bm14U0d4YXdoQU5kZlA1b3pIbkxEbTd5RVVEc1FqRWhHUXpPYzd5Mk1pUHlFMTMiLCJtYWMiOiJjODQ1OGJlYTBkN2U1YmFmMjI5ZjQ0MjM2NzZiZjQ3N2MxYzUxODkzMjg4YWVlZjk2N2M5ZTk1OTI4NmVmYzY2In0%3D',
            'origin': 'https://smailpro.com',
            'referer': 'https://smailpro.com/advanced',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
            'x-xsrf-token': 'eyJpdiI6IjZINmRlVFp2SWhkV1Y5eFBIMXJzVUE9PSIsInZhbHVlIjoiaDZKenJGTzN5Y1M2V1hueDh5eHkxMjRuRUkvU3JPeWlzSjB5WnJJaUNrMnhWU0Z2Zk5DN3B4aE90MkdaM2pYcllXMHdrb3hhU01PWWkxWnFnMG5pNTFrMjJsemw3V0dSV2FHTTE1NDlnNnd3cDByMlVZOW5FanJIckp0Y0xiRW0iLCJtYWMiOiJlYTIzYzAwM2IyZThhNTQ5ZTdlZWUxYjExMjkwZjBlYjc4YWQ0MmYzZTFlNDliMWE0ZGY4M2RjNWRkMWU4NDU0In0=',
        }

        json_data = {
            'email': mailx,
            'timestamp': 1650628073,
        }

        response = requests.post('https://smailpro.com/app/key', cookies=cookies, headers=headers, json=json_data).json()
        return response['items']
    
    def check_mail(mailx):

        xkey = Email.key2(mailx)

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://smailpro.com',
            'Referer': 'https://smailpro.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-rapidapi-ua': 'RapidAPI-Playground',
        }

        while True:
            try:

                response = requests.get(f'https://public-sonjj.p.rapidapi.com/email/gm/check?key={xkey}&rapidapi-key=f871a22852mshc3ccc49e34af1e8p126682jsn734696f1f081&email={mailx}&timestamp=1650628073', headers=headers).json()
                if response['items'] == []:
                    None
                else:
                    print(response)
            except:
                return False

class Discord:

    def fingerprint():
        response = requests.get("https://discord.com/api/v9/experiments").json()
        #print(response['fingerprint'])
        return response['fingerprint']

    def signup():

        lines = open("proxy.txt", "r").read().splitlines()
        proxy = random.choice(lines)
        proxies = {"http": "http://"+proxy, "https": "http://"+proxy}
        xfingerprint = Discord.fingerprint()
        mailx = Email.mail()
        username = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8))+''.join(random.choice("1234567890") for _ in range(4))
        password = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10))+''.join(random.choice("1234567890") for _ in range(4))
        solver = Captcha.cap2()

        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'cookie': '__dcfduid=faccec30911411ec9ee1353c7794579b; __sdcfduid=faccec31911411ec9ee1353c7794579bd1ad248cc7b3f013db0f374d2021253998de03b30c68fa8df53fba588bdd900a; _gcl_au=1.1.1794203985.1645227983; _ga=GA1.2.592214241.1645227984; _fbp=fb.1.1645227983983.206261331; __stripe_mid=b6d18eb8-f18d-45be-9eb4-5b2f064c58524e33b4; OptanonConsent=isIABGlobal=false&datestamp=Mon+Mar+28+2022+19%3A41%3A47+GMT%2B1100+(Australian+Eastern+Daylight+Time)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; __cf_bm=8fWr7Bda5tBIc8dClijIeqd4Gp4PMLwclmhUrbe2B7o-1650369480-0-AajYOzmWXxBGFp9hyFwnohxdDyXRoKBE7N/mv0dloKcglvBP1yguTgu9wdk04zJx0OO+2stGgXWJgkNi4sshC7JbzemsN8aNyGvOTOoJoUUbHNRWn8cZfX72fwz2CvUySw==',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/register',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-fingerprint': xfingerprint,
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMC4wLjQ4OTYuMTI3IFNhZmFyaS81MzcuMzYgRWRnLzEwMC4wLjExODUuNDQiLCJicm93c2VyX3ZlcnNpb24iOiIxMDAuMC40ODk2LjEyNyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuYmluZy5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5iaW5nLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJiaW5nIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEyNDUyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }

        json_data = {
            'fingerprint': xfingerprint,
            'email': mailx,
            'username': username,
            'password': password,
            'invite': None,
            'consent': True,
            'date_of_birth': '2000-01-01',
            'gift_code_sku_id': None,
            'captcha_key': solver,
            'promotional_email_opt_in': False,
        }
        try:

            response = requests.post('https://discord.com/api/v9/auth/register', headers=headers, json=json_data, proxies=proxies).json()
            print(response)
            token = response['token']
            if token:
                print(token)
                Email.check_mail(mailx)
                with open("tokens.txt", "a") as r:
                    r.write(f'{token}\n')
                    #Chack.test()
        except requests.exceptions.ConnectionError:
            print("Your Proxies Are Dead!")
        except:
            print("Failed To Solve Captcha!")

class Check:

    def test(token):

        cookies = {
            '__dcfduid': 'faccec30911411ec9ee1353c7794579b',
            '__sdcfduid': 'faccec31911411ec9ee1353c7794579bd1ad248cc7b3f013db0f374d2021253998de03b30c68fa8df53fba588bdd900a',
            '_gcl_au': '1.1.1794203985.1645227983',
            '_ga': 'GA1.2.592214241.1645227984',
            '_fbp': 'fb.1.1645227983983.206261331',
            '__stripe_mid': 'b6d18eb8-f18d-45be-9eb4-5b2f064c58524e33b4',
            '_gid': 'GA1.2.200945437.1650370674',
            'OptanonConsent': 'isIABGlobal=false&datestamp=Tue+Apr+19+2022+22%3A17%3A54+GMT%2B1000+(Australian+Eastern+Standard+Time)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false',
            '__cf_bm': 'BlOe8AOoAgVXd4MNrftyx4ScY6oiz0ZObKbMs2PIC10-1650449197-0-AfuL3nSPR+rBdA1IErfvH7JlXq5TFdnsMoCgMYxcSlLA1HwuZOXnYOgSoABdezvxHwcZdvejJX8PweJ1SfGRshis/FEhyEx4qL9BwwLw8aRrOt8Qkdlv8yX0sTdEbfCjsw==',
        }

        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': token,
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': '__dcfduid=faccec30911411ec9ee1353c7794579b; __sdcfduid=faccec31911411ec9ee1353c7794579bd1ad248cc7b3f013db0f374d2021253998de03b30c68fa8df53fba588bdd900a; _gcl_au=1.1.1794203985.1645227983; _ga=GA1.2.592214241.1645227984; _fbp=fb.1.1645227983983.206261331; __stripe_mid=b6d18eb8-f18d-45be-9eb4-5b2f064c58524e33b4; _gid=GA1.2.200945437.1650370674; OptanonConsent=isIABGlobal=false&datestamp=Tue+Apr+19+2022+22%3A17%3A54+GMT%2B1000+(Australian+Eastern+Standard+Time)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; __cf_bm=BlOe8AOoAgVXd4MNrftyx4ScY6oiz0ZObKbMs2PIC10-1650449197-0-AfuL3nSPR+rBdA1IErfvH7JlXq5TFdnsMoCgMYxcSlLA1HwuZOXnYOgSoABdezvxHwcZdvejJX8PweJ1SfGRshis/FEhyEx4qL9BwwLw8aRrOt8Qkdlv8yX0sTdEbfCjsw==',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg5MjMxOTg3Nzc0MDc4MTYwOSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4OTI2NjgzOTE4NTExNzE4NjAiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMC4wLjQ4OTYuMTI3IFNhZmFyaS81MzcuMzYgRWRnLzEwMC4wLjExODUuNDQiLCJicm93c2VyX3ZlcnNpb24iOiIxMDAuMC40ODk2LjEyNyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuYmluZy5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5iaW5nLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJiaW5nIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEyNDgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }

        json_data = {}

        response = requests.post('https://discord.com/api/v9/invites/WccuGMhNhf', headers=headers, cookies=cookies, json=json_data)
        print(response.text)

threads = input("Enter Amount Of Threads > ")
os.system("cls")
print("Generating Started...")

def thread():
    while True:
        Discord.signup()

for i in range(int(threads)):
    threading.Thread(target=thread).start()

