import requests #line:1
import json #line:2
import os #line:3
import time #line:4
from fake_useragent import UserAgent #line:5
import re #line:6
import uuid #line:7
from colorama import init ,Fore ,Style #line:8
import fade #line:9
def clean_filename (O000O000O000000O0 ):#line:11
    return re .sub (r'^([0-9])','',re .sub (r'[/:"*?<>|]','',O000O000O000000O0 )).replace ('^0','').replace ('^1','').replace ('^2','').replace ('^3','').replace ('^4','').replace ('^5','').replace ('^6','').replace ('^7','').replace ('^8','').replace ('^9','')#line:12
def check_if_player_exists (O0O00O000000O0O00 ,OO0OO000O0O00O000 ,OOOOOOOO0O000O000 ):#line:14
    if not os .path .exists (O0O00O000000O0O00 ):#line:15
        return False #line:16
    with open (O0O00O000000O0O00 ,'r',encoding ='utf-8')as O0OOOOO0OO0OOO0OO :#line:18
        OOOO00OO0O0OOO000 =O0OOOOO0OO0OOO0OO .readlines ()#line:19
    for OO00O000OOOO0OOOO ,OO0OOOOO000O0O0O0 in enumerate (OOOO00OO0O0OOO000 ):#line:21
        try :#line:22
            O0O0OO0OO000OOOOO =json .loads (OO0OOOOO000O0O0O0 )#line:23
        except json .JSONDecodeError :#line:24
            continue #line:25
        if O0O0OO0OO000OOOOO .get ('fivem')==OO0OO000O0O00O000 .get ('fivem'):#line:27
            O0OO00OO00OOO00O0 =['steam','name','live','xbl','license','license2','name','ip']#line:28
            OO000O00O0O0000OO =True #line:29
            for OOOOO0O00OO000O00 in O0OO00OO00OOO00O0 :#line:31
                OOO0OOO00000000OO =O0O0OO0OO000OOOOO .get (OOOOO0O00OO000O00 )#line:32
                OOO0O00OOO0OOOO00 =OO0OO000O0O00O000 .get (OOOOO0O00OO000O00 )#line:33
                if (OOO0OOO00000000OO is not None or OOO0O00OOO0OOOO00 is not None )and OOO0OOO00000000OO !=OOO0O00OOO0OOOO00 :#line:35
                    OO000O00O0O0000OO =False #line:36
                    break #line:37
            if OO000O00O0O0000OO :#line:39
                return True #line:40
    if OO0OO000O0O00O000 ['identifiers']in OOOOOOOO0O000O000 :#line:42
        return True #line:43
    return False #line:45
def get_server_info (OO00OOO0O00000OOO ,OOOO00OO00O0000OO ,O0OOO000O0O0OOOO0 ):#line:48
    O0O000OOO00OO00O0 =f'https://servers-frontend.fivem.net/api/servers/single/{OO00OOO0O00000OOO}'#line:49
    O00OO000OO0OOOOOO =UserAgent ()#line:50
    OOOOOOOOOO00O0O0O ={'User-Agent':O00OO000OO0OOOOOO .random ,'method':'GET'}#line:54
    try :#line:56
        OOO00O00OOO0OOOOO =requests .get (O0O000OOO00OO00O0 ,headers =OOOOOOOOOO00O0O0O ,proxies =OOOO00OO00O0000OO )#line:57
        if OOO00O00OOO0OOOOO .status_code ==200 :#line:59
            O0O00OOOO0OOO00O0 =OOO00O00OOO0OOOOO .json ()#line:60
            O0O0O0OOOOO000OOO =clean_filename (str (uuid .uuid4 ()))#line:61
            try :#line:63
                O0O0O0OOOOO000OOO =clean_filename (O0O00OOOO0OOO00O0 ['Data']['hostname'])[:100 ]#line:64
            except Exception as O0O0O0OO0O0OOO0O0 :#line:65
                print (O0O0O0OO0O0OOO0O0 )#line:66
            try :#line:68
                if len (O0O00OOOO0OOO00O0 ['Data']['vars']['sv_projectName'])>=10 :#line:69
                    O0O0O0OOOOO000OOO =clean_filename (O0O00OOOO0OOO00O0 ['Data']['vars']['sv_projectName'])[:100 ]#line:70
            except :#line:71
                pass #line:72
            if not os .path .exists ('dump'):#line:74
                os .makedirs ('dump')#line:75
            O0000O0O0O0OO0OO0 =f'dump/{O0O0O0OOOOO000OOO}.txt'#line:77
            for OOOOOOO0OO0OO0O0O in O0O00OOOO0OOO00O0 ['Data']['players']:#line:79
                OO00O0O0O0O000O00 =json .dumps (OOOOOOO0OO0OO0O0O ,ensure_ascii =False )#line:80
                O0OO0O000OO00OOOO =OOOOOOO0OO0OO0O0O ['identifiers']#line:81
                if not check_if_player_exists (O0000O0O0O0OO0OO0 ,OOOOOOO0OO0OO0O0O ,O0OOO000O0O0OOOO0 ):#line:83
                    with open (O0000O0O0O0OO0OO0 ,'a',encoding ='utf-8')as OOO0OOOOOOOO0OO0O :#line:84
                        OOO0OOOOOOOO0OO0O .write (OO00O0O0O0O000O00 )#line:85
                        OOO0OOOOOOOO0OO0O .write ('\n')#line:86
                    print (Fore .GREEN +f'[NEW]'+Style .RESET_ALL +f' {OOOOOOO0OO0OO0O0O["name"]} a été ajouté !')#line:88
                    O0OOO000O0O0OOOO0 .append (O0OO0O000OO00OOOO )#line:89
            print ('\n'+Fore .CYAN +'[AUTHOR]'+Style .RESET_ALL +' https://t.me/leak2panel pour plus'+Fore .MAGENTA +'\n[INFO]'+Style .RESET_ALL +f' Serveur id : {OO00OOO0O00000OOO}'+Fore .MAGENTA +'\n[INFO]'+Style .RESET_ALL +f' Enregistrées dans : {O0000O0O0O0OO0OO0}'+'\n')#line:91
        else :#line:93
            print (Fore .RED +f'\n[ERROR]'+Style .RESET_ALL +f" Message d'erreur ({OO00OOO0O00000OOO}: {OOO00O00OOO0OOOOO.status_code})\n")#line:94
    except Exception as O00000O0OOOO00000 :#line:96
        print (f'Erreur: {str(O00000O0OOOO00000)}')#line:97
def process_servers (OO0OOOO0000O0O0OO ,O0OO0OO00000O00OO ,OO00O000O0OO00O00 ):#line:99
    for O0OO000O0000O0000 ,OOOOOOOO000OOO00O in zip (OO0OOOO0000O0O0OO ,O0OO0OO00000O00OO ):#line:100
        get_server_info (O0OO000O0000O0000 ,OOOOOOOO000OOO00O ,OO00O000O0OO00O00 )#line:101
        time .sleep (0.5 )#line:102
def main ():#line:104
    with open ('serveur.txt','r')as O0O0OOOO000000O00 :#line:105
        O000O0OO0OO00O0OO =[O0OOO0O00OO000000 .strip ()for O0OOO0O00OO000000 in O0O0OOOO000000O00 .readlines ()]#line:106
    with open ('proxy.txt','r')as OO00OOOO000OO0O0O :#line:108
        OO0000OO0O000O0OO =[{'http':f'socks5://{OO0OO0O0OO0O0OO00.strip()}'}for OO0OO0O0OO0O0OO00 in OO00OOOO000OO0O0O ]#line:109
    OO0000O0OOO0O0O00 =0 #line:111
    O0O000O0O00O00OOO =len (OO0000OO0O000O0OO )#line:112
    OO0OOO0O000OO00O0 =[]#line:113
    while True :#line:115
        OOOO000O0OOO0O0OO =len (O000O0OO0OO00O0OO )//2 #line:116
        O0O0OOOOOO00O0O00 =O000O0OO0OO00O0OO [:OOOO000O0OOO0O0OO ]#line:117
        OOO0000OO0OO000OO =O000O0OO0OO00O0OO [OOOO000O0OOO0O0OO :]#line:118
        process_servers (O0O0OOOOOO00O0O00 ,OO0000OO0O000O0OO ,OO0OOO0O000OO00O0 )#line:120
        process_servers (OOO0000OO0OO000OO ,OO0000OO0O000O0OO ,OO0OOO0O000OO00O0 )#line:121
def startup ():#line:123
    os .system ("cls")#line:124
    OO0O00000O0000000 ='''
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀⠀⠀
⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀⠀⠀
⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀Aka   ⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀⠀⠀
⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀⠀⠀
⠀⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⡠⠀⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⡀⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⡀⠄⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''#line:153
    OO0000OOOO00OO0O0 =fade .purplepink (OO0O00000O0000000 )#line:154
    print (OO0000OOOO00OO0O0 )#line:155
    time .sleep (5 )#line:157
    main ()#line:158
startup ()#line:160
