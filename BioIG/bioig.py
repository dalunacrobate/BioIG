import requests, bs4, sys, os
from bs4   import BeautifulSoup

def cleartext(text):
    spec_chars = list(',?;:!§/\|<>*$£¤^¨^')
    for i in range(8):
        for i in spec_chars:
            if i in text:
                text = text.replace(i,'')
    return text

def get_info_from_bio(bio):
    lines = bio.split('\n')

    religions = [
        ('✡️','Judaism'),
        ('☪️','Islam'),
        ('☦️','Orthodox'),
        ('✝️','Christ'),
        ('🕋','Islam')
    ]

    hobbies = [
        ('🥊','Boxing'),
        ('🐎','Horses'),
        ('🐴','Horses'),
        ('🎾','Tennis'),
        ('⚽','Football'),
        ('🥋','Martial Arts'),
        ('🏀','Basketball'),
        ('🏈','American Football'),
        ('🏐','Volleyball'),
        ('🎻','Violin'),
        ('🎸','Guitar'),
        ('🎹','Piano'),
        ('🎣','Fishing'),
        ('⛷️','Ski')
    ]

    astrology_signs = [
        ('♈','Aries','March 21 - April 20'),
        ('♉','Taurus','April 21 - May 21'),
        ('♊','Gemini','May 22 - June 21'),
        ('♋','Cancer','June 22 - July 22'),
        ('♌','Leo','July 23 - August 22'),
        ('♍','Virgo','August 23 - September 23'),
        ('♎','Libra','September 24 - October 23'),
        ('♏','Scorpius','October 24 - November 22'),
        ('♐','Sagittarius','November 23 - December 21'),
        ('♑','Capricorn','December 22 - January 20'),
        ('♒','Aquarius','January 21 - February 19'),
        ('♓','Pisces','February 20 - March 20')
    ]

    ethnical_origins = [
        ('🇫🇷','France'),
        ('🇨🇭','Swiss'),
        ('🇨🇳','China'),
        ('🇧🇪','Belgium'),
        ('🇦🇱','Albania'),
        ('🇧🇬','Bulgaria'),
        ('🇧🇷','Brazil'),
        ('🇨🇦','Canada'),
        ('🇩🇪','Germany'),
        ('🇮🇱','Israel'),
        ('🇵🇸','Palestine'),
        ('🇺🇸','United States'),
        ('🇵🇹','Portugal'),
        ('🇱🇹','Lithuania'),
        ('🇵🇱','Poland'),
        ('🇷🇺','Russia'),
        ('🇪🇸','Spain'),
        ('🇹🇷','Turkey'),
        ('🇩🇿','Algeria'),
        ('🇲🇦','Morocco'),
        ('🇬🇵','Guadeloupe'),
        ('🇮🇳','India'),
        ('🇱🇺','Luxembourg'),
        ('🇳🇪','Niger'),
        ('🇳🇬','Nigeria'),
        ('🇶🇦','Quatar'),
        ('🇷🇪','Réunion'),
        ('🇷🇴','Romania'),
        ('🇹🇳','Tunisia'),
        ('🇾🇹','Mayotte'),
        ('🇿🇦','South Africa'),
        ('🇲🇽','Mexico'),
        ('🇨🇿','Czech Republic'),
        ('🇯🇵','Japan'),
        ('🇰🇪','Kenya'),
        ('🇰🇵','North Korea'),
        ('🇰🇷','South Korea'),
        ('🇯🇲','Jamaica'),
        ('🇮🇪','Ireland'),
        ('🇬🇷','Greece')
    ]

    emailss = [
            '@icloud.com',
            '@gmail.com',
            '@gmx.fr',
            '@yahoo.fr',
            '@yahoo.com',
            '@outlook.com'
            '@outlook.fr',
            '@hotmail.fr',
            '@hotmail.com',
            '@live.fr',
            '@live.com',
            '@sfr.fr',
            '@orange.fr',
            '@free.fr',
            '@aol.com',
            '@wanadoo.fr',
            '@neuf.fr',
            '@laposte.net',
            '@yandex.ru',
            '@club-internet.fr',
            '@msn.com',
            '@influencelife.fr',
            '@shaunaevents.com',
            '@we-events.fr',
            '@nabillapro.com',
            '@facebook.com',
            '@protonmail.com',
            '@protonmail.ch',
            '@thepauseagency.com',
            '@alexotime.com',
            '@tomorrowhub.com'
    ]

    bio_infos       = {}
    emails_final    = []
    snapchat_final  = []
    paypals         = []
    best_friend     = []
    ages            = []
    love_date_since = []
    school_list     = []
    city_list       = []
    lgbt_points     = []
    fb_list         = []
    twitter_list    = []
    flag_list       = []
    religions_targ  = []
    astro_sign      = []
    hobbies_emojis  = []
    love_situation  = []
    tiktok_list     = []

    for line in lines:
        line = line.replace('</a','').replace('<a href="/v','').replace('<a href="/t/','')
        line = line.lower()
        for i in religions:
            emoji, religionName = i
            if emoji in line or religionName.lower() in line:
                religions_targ.append(religionName)
        for i in astrology_signs:
            emoji, sign, date = i
            if emoji in line:
                astro_sign.append('{} | {}'.format(sign,date))
        for flagos in ethnical_origins:
            flag, country_full = flagos
            if flag in line:
                flag_list.append(country_full)
        for i in hobbies:
            emoji, name = i
            if emoji in line:
                hobbies_emojis.append(name)
        temp_list_love = []
        for chars in line:
            if chars == "/":
                temp_list_love.append('.')
        if "tik tok" in line or "tiktok" in line:
            if ":" in line:
                tiktok_list.append(cleartext(line.split(':')[1]))
            else:
                tiktok_list.append(cleartext(line.replace('tik tok','').replace('tiktok','')))
        if "en couple" in line or "🔒" in line or "🔐" in line:
            love_situation.append('Not Free | Taken')
        if "celib" in line:
            love_situation.append('Single | Free')
        if "🏳️‍🌈" in line or "🏳️‍⚧️" in line:
            lgbt_points.append('.')
        if "facebook" in line:
            if ":" in line:
                line = line.split(':')[1]
            fb_list.append(cleartext(line))
        if "twitter" in line:
            if ":" in line:
                line = line.split(':')[1]
            twitter_list.append(cleartext(line))
        if len(temp_list_love) == 2:
            love_date_since.append(line)
        if "📍" in line or "📌" in line:
            city_list.append(cleartext(line.replace('📍','').replace('📌','').replace(':','')))
        if "snapchat" in line or "snap" in line or "👻" in line or "sc : " in line or "sc:" in line:
            line = line.replace('👻','').strip()
            if ":" in line:
                line = line.split(':')[1].strip()
            snapchat_final.append(cleartext(line))
        if "📚" in line or "🎓" in line:
            school_list.append(cleartext(line.replace('📚','').replace('🎓','').strip()))
        if "yo" in line or "years old" in line or "years" in line or "🎂" in line or "anniv" in line:
            if "🎂" in line:
                line = line.replace('🎂','')
                if ":" in line:
                    line = line.split(':')[1]
                ages.append(cleartext(line))
            else:
                try:
                    if "years" in line:
                        age = int(line.split("years")[0].replace('years','').strip())
                    elif "yo" in line:
                        age = int(line.split("yo")[0].replace('yo','').strip())
                    elif 'y' in line:
                        age = int(line.split("y")[0].replace('y','').strip())
                    else:
                        age = int(line.split("years")[0].strip())
                    ages.append(cleartext(str(age)))
                except ValueError:
                    ages.append('Verify by yourself')
        if "paypal.me/" in line:
            paypal = ("paypal.me/"+line.split("paypal.me/")[1])
            paypals.append(paypal)
        if "@" in line:
            line = line.replace('📩','')
            temp_list_emails = []
        if "/" in line and '"' in line:
            line = (line.replace('/','@').split('"')[0])
            temp_list_emails.append('.')
            domain = '@'+line.split('@')[1]
            if "." not in domain:
                line = "@"+line.split("@")[1]
                if " " in line:
                    line = line.split(' ')[0]
                    best_friend.append(line)
                else:
                    for i in emailss:
                        if domain == i:
                            if line not in emails_final:
                                if ":" in line:
                                    line = line.split(':')[1].strip()
                                emails_final.append(line)
    
        if len(tiktok_list) == 0:
            bio_infos['tiktok_list'] = None
        else:
            bio_infos['tiktok_list'] = tiktok_list
        if len(love_situation) == 0:
            bio_infos['love_situation'] = None
        else:
            bio_infos['love_situation'] = love_situation
        if len(hobbies_emojis) == 0:
            bio_infos['Hobbies'] = None
        else:
            bio_infos['Hobbies'] = hobbies_emojis
        if len(religions_targ) == 0:
            bio_infos['religions'] = None
        else:
            bio_infos['religions'] = religions_targ
        if len(astro_sign) == 0:
            bio_infos['astrology'] = None
        else:
            bio_infos['astrology'] = astro_sign
        if len(flag_list) == 0:
            bio_infos['origins'] = None
        else:
            bio_infos['origins'] = flag_list
        if len(fb_list) == 0:
            bio_infos['fb_list'] = None
        else:
            bio_infos['fb_list'] = fb_list
        if len(twitter_list) == 0:
            bio_infos['twitter_list'] = None
        else:
            bio_infos['twitter_list'] = twitter_list
        if len(lgbt_points) == 0:
            bio_infos['lgbt_points'] = None
        else:
            bio_infos['lgbt_points'] = "a"
        if len(city_list) == 0:
            bio_infos['city_list'] = None
        else:
            bio_infos['city_list'] = city_list
        if len(school_list) == 0:
            bio_infos['school'] = None
        else:
            bio_infos['school'] = school_list[0].replace(':','')
        if len(snapchat_final) == 0:
            bio_infos['snapchat'] = None
        else:
            bio_infos['snapchat'] = snapchat_final[0].replace('snapchat','').replace('snap','').replace(':','').strip()
        if len(best_friend) == 0:
            bio_infos['best_friend'] = None
        else:
            bio_infos['best_friend'] = best_friend
        if len(ages) == 0:
            bio_infos['age'] = None
        else:
            bio_infos['age'] = str(ages[0])
        if len(emails_final) == 0:
            bio_infos['emails'] = None
        else:
            bio_infos['emails'] = emails_final
        if len(love_date_since) == 0:
            bio_infos['love_date'] = None
        else:
            bio_infos['love_date'] = love_date_since[0]
        if len(paypals) == 0:
            bio_infos['paypal'] = None
        else:
            bio_infos['paypal'] = paypals[0]
    return bio_infos
    
def getInstagramInfos(username):
    
    url = "https://smihub.com/v/{}".format(username.replace('@',''))

    r = requests.get(url=url)
    page = r.content.decode()
    features = "html.parser"
    soup = BeautifulSoup(page,features)

    bioo = str(soup.find('div',{'class':'user__info-desc'}))

    bioo = bioo.replace('<div','').replace('</div>','').replace('class="user__info-desc">','').strip()

    while "<br/" in bioo:
        bioo = bioo.replace('<br/','\n')

    while ">" in bioo:
        bioo = bioo.replace(">",'')
    
    return get_info_from_bio(bioo)

def banner():
    print("""
Author : Dalunacrobate
Url : https://github.com/dalunacrobate/BioIG
""")

def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

def main():
    if len(sys.argv)>1:
        clear()
        banner()
        data = getInstagramInfos(sys.argv[1])
        if data['paypal'] is not None:
            print("[+] Paypal :\n============\n- {}".format(data['paypal']))
        if data['emails'] is not None:
            print("[+] Emails :\n===========")
            for i in data['emails']:
                print("-", i)
        if data['age'] is not None:
            print("[+] Age :\n========\n{}".format(data['age']))
        if data['best_friend'] is not None:
            print("[+] Best Friends :\n=================")
            for i in data['best_friend']:
                print("-", i)
        if data['snapchat'] is not None:
            print("[+] Snapchat :\n=============\n- {}".format(data['snapchat']))
        if data['school'] is not None:
            print("[+] School :\n===========\n- {}".format(data['school']))
        if data['twitter_list'] is not None:
            print("[+] Twitter :\n============")
            for i in data['twitter_list']:
                print("-", i)
        if data['city_list'] is not None:
            print("[+] Localisation :\n=================")
            for i in data['city_list']:
                print("-", i)
        if data['lgbt_points'] is not None:
            print("[+] Probably LGBT")
        if data['fb_list'] is not None:
            print("[+] Facebook accounts :\n======================")
            for i in data['fb_list']:
                print("-", i)
        if data['origins'] is not None:
            print("[+] Origins :\n============")
            for i in data['origins']:
                print("-", i)
        if data['astrology'] is not None:
            print("[+] Astrologic sign :\n====================")
            for i in data['astrology']:
                print("-", i)
        if data['Hobbies'] is not None:
            print("[+] Hobbies :\n============")
            for i in data['Hobbies']:
                print("-", i)
        if data['religions'] is not None:
            print("[+] Religions :\n==============")
            for i in data['religions']:
                print("-", i)
        if data['tiktok_list'] is not None:
            print("[+] Tiktok :\n===========")
            for i in data['tiktok_list']:
                print("-", i)
        if data['love_situation'] is not None:
            print('[+] Love Situation :\n===================')
            for i in data['love_situation']:
                print("-", i)
        sys.exit('\n')
    else:
        sys.exit("[!] Invalid params\nExemple : bioig username")
main()
