#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import platform
import re
import tempfile
import unicodedata
from pprint import pprint

from ArticutAPI import Articut
try:
    from .defaultDict import Hakka_Lexicon
    from .posShift import shiftRule
except:
    from defaultDict import Hakka_Lexicon
    from posShift import shiftRule

BASEPATH = os.path.dirname(os.path.abspath(__file__))

class ArticutHKK:
    def __init__(self, username="", apikey="", usernameENG="", apikeyENG=""):
        self.articut = Articut(username=username, apikey=apikey)
        self.articutENG = Articut(username=usernameENG, apikey=apikeyENG, url="https://nlu.droidtown.co")
        self.posPat = re.compile("<[^<]*>([^<]*)</([^<]*)>")
        self.TLPat = re.compile("\s?[\-a-zA-Záíúéóàìùèòâîûêôǎǐǔěǒāīūēō̋̍]+(-+[a-zA-Záíúéóàìùèòâîûêôǎǐǔěǒāīūēō̋̍]+)*\s?")
        self.userDefinedDICT = {}
        self.cjkPAT = re.compile('[\u4e00-\u9fff]')
        #self.moeCSV = [[t.replace("\n", "") for t in l.split(",")] for l  in open("{}/defaultDict/moe_dict/詞目總檔.csv".format(BASEPATH), "r", encoding="utf-8").readlines()]
        #self.DT_TL = Hakka_Lexicon.DT_TL
        self.purgePat = re.compile("</\w+(_\w+)?><\w+(_\w+)?>|</?\w+(_\w+)?>")
        self.shiftRule = shiftRule
        self.defaultDICT = Hakka_Lexicon.dictCombiner()
        #self.legacyLIST = []
        self.personPat = re.compile("(?<=<ENTITY_person>)[^<]+(?=</ENTITY_person>)")
    def _pos2Obj(self, posLIST):
        resultLIST = []
        for pos in posLIST:
            if '</' in pos:
                textPosLIST = [[p.group(1), p.group(2)] for p in self.posPat.finditer(pos)]
                # group(0) <ACTION_verb>結帳</ACTION_verb>
                # group(1) 結帳
                # group(2) ACTION_verb
                objLIST = []
                for txt, p in textPosLIST:
                    objLIST.append({
                        "text": txt,
                        "pos": p,
                    })
                if objLIST:
                    resultLIST.append(objLIST)
                else:
                    resultLIST.append([{
                        "text": pos,
                        "pos": 'PUNCTUATION',
                    }])
            else:
                resultLIST.append([{
                    "text": pos,
                    "pos": 'PUNCTUATION',
                }])
        return resultLIST

    def _2TL(self, posLIST):
        '''
        把 posLIST 裡的每一個詞，一一轉為 TL (台羅拼音)
        '''
        resultLIST = []
        for p in posLIST: #p 是一句
            for word in p:
                if "LATIN" in unicodedata.name(word["text"][0]):
                    resultLIST.append(word["text"])
                #elif word["text"] in self.DT_TL:
                    #resultLIST.append(self.DT_TL[word["text"]])
                elif word["text"] in [token[2] for token in self.moeCSV]:
                    tokenLIST = []
                    for token in self.moeCSV[1:]:
                        if token[2] == word["text"]:
                            tokenLIST.append(token[3])

                    if len(tokenLIST) > 1:
                        resultLIST.append("({})".format("/".join(tokenLIST)))
                    elif len(tokenLIST) == 1:
                        if "/" in tokenLIST[0]:
                            resultLIST.append("({})".format(tokenLIST[0]))
                        else:
                            resultLIST.append("{}".format(tokenLIST[0]))
                    else:
                        pass
                    tokenLIST = []
                else:
                    wordLIST = []
                    tokenLIST = []
                    for t in word["text"]:
                        for token in self.moeCSV:
                            if len(token[2]) == 1 and t == token[2]:
                                tokenLIST.append("{}".format(token[3]))

                        if len(tokenLIST) > 1:
                            wordLIST.append("({})".format("/".join(tokenLIST)))
                        elif len(tokenLIST) == 1:
                            wordLIST.append("{}".format(tokenLIST[0]))
                        tokenLIST = []
                    resultLIST.append("-".join(wordLIST))
        return resultLIST


    def _mixedInputDetector(self, inputSTR):
        TLLIST = [t.group() for t in self.TLPat.finditer(inputSTR)]
        with open(self.TaigiDictFILE.name) as f:
            userDefinedDICT = json.load(f)

        #<特殊區塊：如果使用者有購買英文版 Articut 的使用額度，將調用英文人名偵測。>
        #<否則本功能會在每小時 2000 字免費額度用盡後失效，待下一個小時的免費額度啟用時才恢復>
        knownLIST = []
        for i in TLLIST:
            resultDICT = self.articutENG.parse(i, level="lv1")
            if resultDICT["status"] == True and resultDICT["msg"] == "Success!":
                if "<ENTITY_person>{}</ENTITY_person>".format(i) in "".join(resultDICT["result_pos"]):
                    knownLIST.append(i)
                    userDefinedDICT["ENTITY_person"].append(i)
                    self.userDefinedDICT["ENTITY_person"].append(i)
            else:
                pass
        TLLIST = list(set(TLLIST)-set(knownLIST))
        #</特殊區塊：如果使用者有購買英文版 Articut 的使用額度，將調用英文人名偵測>
        #</否則本功能會在每小時 2000 字免費額度用盡後失效，待下一個小時的免費額度啟用時才恢復>

        if TLLIST == []:
            pass
        else:
            #with open(self.userDefinedDictFILE.name) as f:
                #userDefinedDICT = json.load(f)
            if "_ArticutTaigiUserDefined" in userDefinedDICT.keys():
                userDefinedDICT["_ArticutTaigiUserDefined"].extend(TLLIST)
            else:
                userDefinedDICT["_ArticutTaigiUserDefined"] = TLLIST
            if platform.system() == "Windows":
                self.userDefinedDictFILE = tempfile.NamedTemporaryFile(mode="w+", delete=False)
            else:
                self.userDefinedDictFILE = tempfile.NamedTemporaryFile(mode="w+")
            json.dump(userDefinedDICT, self.userDefinedDictFILE)
            self.userDefinedDictFILE.flush()
        return None

    def _spaceWalker(self, inputDICT):
        '''
        移除非 CJK 字元前後的空格
        '''
        fposPat = re.compile("<UserDefined>\s")
        pposPat = re.compile("\s</UserDefined>")
        posPat = re.compile("</?\w_?[^>]+?>")
        for i in range(0, len(inputDICT["result_pos"])):
            inputDICT["result_pos"][i] = re.sub(fposPat, " <UserDefined>", inputDICT["result_pos"][i])
            inputDICT["result_pos"][i] = re.sub(pposPat, "</UserDefined> ", inputDICT["result_pos"][i])
            inputDICT["result_pos"][i] = inputDICT["result_pos"][i].strip()
        try:
            inputDICT["result_pos"].remove("")
        except:
            pass

        tmpSTR = ""
        for i in range(0, len(inputDICT["result_pos"])):
            tmpSTR = tmpSTR + re.sub(posPat, "<DROIDTOWN_TKBD>", inputDICT["result_pos"][i])
            tmpSTR = tmpSTR.replace("<DROIDTOWN_TKBD><DROIDTOWN_TKBD>", "/").replace("<DROIDTOWN_TKBD> <DROIDTOWN_TKBD>", "/ /").replace("<DROIDTOWN_TKBD>", "/")
        inputDICT["result_segmentation"] = tmpSTR
        return inputDICT

    def _posShift(self, posLIST):
        for i in range (0, len(posLIST)):
            if len(posLIST[i]) == 1:
                pass
            else:
                for pat in self.shiftRule:
                    shiftLIST = [(g.start(), g.end(), g.group(0)) for g in reversed(list(pat[0].finditer(posLIST[i])))]
                    for s in shiftLIST:
                        adjustedSTR = s[2]
                        for adjust_s in pat[1]:
                            adjustedSTR = adjustedSTR.replace(adjust_s, pat[2][pat[1].index(adjust_s)])
                        posLIST[i] = "{}{}{}".format(posLIST[i][:s[0]], adjustedSTR, posLIST[i][s[1]:])
        return posLIST

    def _pos2Seg(self, posLIST):
        resultSTR = ""
        for s in posLIST:
            resultSTR = resultSTR + re.sub(self.purgePat, "╱", s)
        return resultSTR

    def parse(self, inputSTR, level="lv2", userDefinedDictFILE=None, convert=None):
        #for i in self.legacyLIST[0]:
            #inputSTR = inputSTR.replace(i, self.legacyLIST[1][self.legacyLIST[0].index(i)])

        if level=="lv3":
            tgLV = "lv3"
            level = "lv2"
            if convert == None:
                convert = "TL"
            else:
                if convert.upper() in ("TL", "POJ", "WORD"):
                    convert = convert.upper()
                else:
                    raise
        else:
            tgLV = level

        if platform.system() == "Windows":
            self.TaigiDictFILE = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        else:
            self.TaigiDictFILE = tempfile.NamedTemporaryFile(mode="w+")

        self.userDefinedDICT = self.defaultDICT
        if userDefinedDictFILE == None:
            pass
        else:
            with open(userDefinedDictFILE, encoding="utf-8") as f:
                userDefinedDICT = json.load(f)
            for k in userDefinedDICT.keys():
                try:
                    tmpLIST = userDefinedDICT[k]
                    for POS in self.defaultDICT.keys():
                        self.defaultDICT[POS] = list(set(self.defaultDICT[POS])-set(tmpLIST))
                    if k in self.userDefinedDICT.keys():
                        tmpLIST.extend(self.userDefinedDICT[k])
                    tmpLIST = list(set(tmpLIST))
                    self.userDefinedDICT[k].extend(tmpLIST)
                except KeyError:
                    self.userDefinedDICT[k] = tmpLIST

        #<利用 Articut 建立人名字典>
        checkingPersonDICT = self.articut.parse(inputSTR, level="lv1")
        personLIST = [p[-1] for p in [e[-1] for e in self.articut.getPersonLIST(checkingPersonDICT,  includePronounBOOL=False) if e != []] if p!=[]]
        if personLIST != []:
            self.userDefinedDICT["ENTITY_person"] = personLIST
        #</利用 Articut 建立人名字典>

        json.dump(self.userDefinedDICT, self.TaigiDictFILE)
        self.TaigiDictFILE.flush()

        self._mixedInputDetector(inputSTR)
        articutResultDICT = self.articut.parse(inputSTR, level=level, userDefinedDictFILE=self.TaigiDictFILE.name)
        articutResultDICT = self._spaceWalker(articutResultDICT)
        POScandidateLIST = []
        for tkn in articutResultDICT["result_segmentation"].split("/"):
            for k in self.userDefinedDICT.keys():
                if tkn in self.userDefinedDICT[k]:
                    POScandidateLIST.append(("<UserDefined>{}</UserDefined>".format(tkn), "<{0}>{1}</{0}>".format(k, tkn)))

        for i, s in enumerate(articutResultDICT["result_pos"]):
            for p in POScandidateLIST:
                articutResultDICT["result_pos"][i] = articutResultDICT["result_pos"][i].replace(p[0],p[1])
        print("src", articutResultDICT["result_pos"])
        articutResultDICT["result_pos"] = self._posShift(articutResultDICT["result_pos"])
        articutResultDICT["result_obj"] = self._pos2Obj(articutResultDICT["result_pos"])
        articutResultDICT["result_segmentation"] = self._pos2Seg(articutResultDICT["result_pos"])

        if tgLV in ("lv1", "lv2"):
            return articutResultDICT
        elif tgLV == "lv3":
            resultDICT = {"person": self.articut.getPersonLIST(articutResultDICT),
                          #"event": articutResultDICT["event"],
                          "time": self.articut.getTimeLIST(articutResultDICT),
                          "site": self.articut.getLocationStemLIST(articutResultDICT),
                          "entity":  self.articut.getNounStemLIST(articutResultDICT),
                          #"number": articutResultDICT["number"],
                          #"user_defined": articutResultDICT["user_defined"],
                          "utterance": [],
                          #"input": articutResultDICT["input"],
                          #"unit": articutResultDICT["unit"],
                          "exec_time": articutResultDICT["exec_time"],
                          "level": "lv3",
                          "version": articutResultDICT["version"],
                          "status": articutResultDICT["status"],
                          "msg": articutResultDICT["msg"],
                          "word_count_balance": articutResultDICT["word_count_balance"],
                          }
            # 呼叫一個 converter，把 resultDICT["result_obj"] 裡的詞彙一個一個轉成拼音。
            if convert == "TL":
                resultLIST = self._2TL(articutResultDICT["result_obj"])
            #elif convert == "POJ":
                #resultLIST = self._2POJ(articutResultDICT["result_obj"])
            #else: #convert == "WORD":
                #resultLIST = self._2Word(articutResultDICT["result_obj"])
            resultDICT["utterance"] = "╱".join(resultLIST)
            return resultDICT



if __name__ == "__main__":
    try:
        with open("./account.info", encoding="utf-8") as jF:
            accountDICT = json.load(jF)
    except:
        accountDICT = {"username":"", "apikey":""}

    accountDICT = {"username":accountDICT["username"], "apikey":accountDICT["apikey"]}
    articutHakka = ArticutHKK(username=accountDICT["username"], apikey=accountDICT["apikey"])
    #客語漢字 CWS/POS TEST
    inputSTR = "外背蚊仔恁多，門愛關好來。"
    #"佢轉來个時節歸身汗，就遽遽去洗身腳"
    #"略略仔發燒。"
    #"做護理師，愛有耐心。"
    #"醫院在車頭附近。"
    #"先生開个藥仔，愛記得照時間食。"
    #"這菜無洩藥仔，做得安心食。"
    #"這菜無射藥仔，做得安心食。"
    #"今晡日先生無同人看病。"
    #"洗好身，試著當鬆爽。"
    #"洗好身，感覺著蓋鬆爽。"
    #"佢人毋鬆爽，今晡日愛請假。"
    #"老弟想屙尿，緊尋便所。"
    #"佢去便所屙屎，你愛等一下仔無？"
    #"佢毋知食恁多麼个，打个屁當臭。"
    #"佢毋知食恁多麼个，打个屁卵蓋臭。"
    #"歸日仔頭那痛。"
    #"剃頭那毛。"
    #"厥頭那毛烏金烏金，還靚哦！"
    #"老吔！目珠花花。"
    #"講佢兩句，就目汁緊跌。"
    #"鼻公塞塞。"
    #"佢耳公聾聾，你講話愛較大聲兜仔。"
    #"佢耳公聾聾，你講話愛過大聲一息。"
    #"牙齒痛，愛去分先生看。"
    #"嬰兒仔正生牙齒。"
    #"朝晨䟘起來愛洗嘴洗面。"
    #"試著肩頭硬硬樣仔。"
    #"阿爸牽等吾个手。"
    #"老弟个手指分門夾著，痛到緊噭。"
    #"食著無淨俐个東西，肚屎痛緊走便所。"
    #"洗身該下腳愛洗淨。"
    #"阿姆企忒久，身體佇毋著。"
    #"佢跌倒，骨頭斷忒。"
    #"佢橫倒，骨頭斷核。"
    #"佢屋下有五儕人。"
    #"佢屋下有五個人。"
    #"厥聲當軟，聽著心情就異好。"
    #"厥聲蓋軟，聽著心情就盡好。"
    #"食飽夜來去散步好無？"
    #"盎仔插等一蕊花。"
    #"下禮拜愛考試，你知無？"
    #"逐擺就恁仔，搞到毋知好轉。"
    #"每擺就恁仔，搞到毋知好歸。"
    #"買隻等路送佢，分佢歡喜一下。"
    #"買一個妄想送佢，分佢歡喜一下。"
    #"你講佢怪怪？𠊎斯感覺毋出。"
    #"轉寒吔！你無感覺係無？"
    #"恁久無來，你還記得路無？"
    #"佢盡驚蛇哥。"
    #"毋使恁緊張。"
    #"緊張到舌嫲打結。"
    #"阿公盡好食腹內。"
    #"好食、好聽、好搞。"
    #"這擺旅行，若爺哀肯分你去無？"
    #"厥頭路當輕鬆。"
    #"快樂過日仔。"
    #"逐日就當快樂。"
    #"每日就蓋快樂。"
    #"𠊎愛睡目哩，無愛過接電話吔。"
    #"正餐愛食飽，莫緊食點心。"
    #"無人識。"
    #"看毋識。"
    #"你想清楚，正同𠊎講。"
    #"𠊎愛去市場，你有想愛買麼个無？"
    #"背細人仔去散步。"
    #"天時恁熱，你背恁多衫做麼个？"
    #"背書包仔去上課。"
    #"鳥仔飛入屋，逐毋出去。"
    #"錢囥在桌項，你自家拿。"
    #"錢放在桌頂，你自家拿。"
    #"行啊出去就毋記得哩！"
    #"行啊出去就毋記得吔！"
    #"日頭恁烈，毋好出去晒日頭。"
    #"衫恁短，肚臍走出來哩（吔）。"
    #"文章還寫毋出來。"
    #"手伸較（過）長兜仔（一息）。"
    #"佢伸手去拿東西。"
    #"打粄仔。"
    #"打球仔。"
    #"同這包餅仔打開來食。"
    #"記得愛帶等路（妄想）轉來（歸來）。"
    #"皮包仔毋記得帶著。"
    #"皮包仔添放核帶吔。"
    #"你在這等𠊎一下。"
    #"做得等一下仔（等一下）無？"
    #"佢兩儕（兩個人）盡相像，連同學都分毋出來。"
    #"直直行過去就到厥屋下吔！"
    #"佢摎（同）腳球踢過去。"
    #"定定仔行過來，毋好用走。"
    #"同該張凳仔徙過來放。"
    #"你在該講麼个？𠊎完全聽毋識。"
    #"你會講客話無？"
    #"毋好亂講話。"
    #"外背蚊仔恁多，門愛關好來。"
    #"地動當（蓋）搖，圍牆橫下來。"
    #"麼个東西跌下來？恁大聲。"

    resultDICT = articutHakka.parse(inputSTR, level="lv2")
    pprint(resultDICT)
