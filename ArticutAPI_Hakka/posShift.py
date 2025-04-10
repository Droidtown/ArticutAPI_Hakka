#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

shiftRule =[(re.compile("<ACTION_verb>歸</ACTION_verb><MODIFIER>暗</MODIFIER>"),("MODIFIER",),("TIME_justtime",)),
            (re.compile("<ACTION_verb>歸</ACTION_verb>((<ENTITY_noun>身</ENTITY_noun>)|(<TIME_justtime>暗</TIME_justtime>))"),("ACTION_verb",),("QUANTIFIER",)),
            (re.compile("((?<=</ENTITY_num>)|(?<=</QUANTIFIER>))<ENTITY_noun>身</ENTITY_noun>"),("ENTITY_noun",),("ENTITY_classifier",)),
            (re.compile("<ENTITY_noun>身</ENTITY_noun><ENTITY_noun>衫</ENTITY_noun>"),("<ENTITY_noun>身</ENTITY_noun>",),("<ENTITY_classifier>身</ENTITY_classifier>",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>((?=<ACTION_verb>)|(?=<MODIFIER>)|(?=<MODAL>)|(?=<FUNC_degreeHead>))"),("FUNC_inter",),("FUNC_negation",)),
            (re.compile("<FUNC_inter>無</FUNC_inter><ENTITY_noun>[味緒路]+</ENTITY_noun>"),("FUNC_inter",),("FUNC_negation",)),
            (re.compile("<FUNC_negation>無</FUNC_negation>(<ACTION_verb>會</ACTION_verb>)"),("FUNC_negation",),("FUNC_inter",)),           
            (re.compile("<FUNC_negation>無</FUNC_negation><ACTION_verb>[聲根據]+</ACTION_verb>"),("ACTION_verb",),("ENTITY_noun",)),           
            (re.compile("<FUNC_negation>毋</FUNC_negation><ENTITY_noun>理想</ENTITY_noun>"),("ENTITY_noun",),("MODIFIER",)),           
            (re.compile("<ENTITY_classifier>張</ENTITY_classifier>((<ACTION_verb>等</ACTION_verb>)|(<ENTITY_noun>茶</ENTITY_noun>))"), ("ENTITY_classifier",), ("ACTION_verb",)),
            (re.compile("(?<=[^<愛知做得]</ACTION_verb>)<ACTION_verb>等</ACTION_verb>"), ("ACTION_verb",), ("ASPECT",)),
            (re.compile("(?<=</ACTION_verb>)<FUNC_degreeHead>過</FUNC_degreeHead>"), ("FUNC_degreeHead",), ("ASPECT",)),
            (re.compile("<ACTION_verb>[在識]+</ACTION_verb>(?=<ACTION_verb>)"), ("ACTION_verb",), ("ASPECT",)),
            (re.compile("<MODIFIER>緊</MODIFIER>(?=<ACTION_verb>)"),("MODIFIER",),("TIME_justtime",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>$"),("FUNC_inter",),("CLAUSE_Q",)),
            (re.compile("<ACTION_verb>聽</ACTION_verb><CLAUSE_Q>無</CLAUSE_Q>"),("</ACTION_verb><CLAUSE_Q>","CLAUSE_Q",),("","ACTION_verb",)),
            (re.compile("<FUNC_negation>吂</FUNC_negation>$"),("FUNC_negation",),("CLAUSE_Q",)),
            (re.compile("<MODIFIER>大</MODIFIER><ACTION_verb>聲</ACTION_verb>"),("<MODIFIER>大</MODIFIER><ACTION_verb>聲</ACTION_verb>",), ("<MODIFIER>大聲</MODIFIER>",)),
            (re.compile("<MODIFIER>([^<])</MODIFIER><MODIFIER>\\1</MODIFIER>"), ("</MODIFIER><MODIFIER>",), ("",)),
            (re.compile("(<FUNC_degreeHead>[^<]+</FUNC_degreeHead>)<ENTITY_noun>[垃圾牛冰壁油金差]</ENTITY_noun>"),("ENTITY_noun",), ("MODIFIER",)),        
            (re.compile("(<FUNC_degreeHead>[異恁盡過當蓋]</FUNC_degreeHead>)<ENTITY_noun>派頭</ENTITY_noun>"),("ENTITY_noun",), ("MODIFIER",)),        
            (re.compile("(<FUNC_degreeHead>恁</FUNC_degreeHead>)<ENTITY_classifier>重</ENTITY_classifier>"),("ENTITY_classifier",), ("MODIFIER",)),        
            (re.compile("<FUNC_inter>無</FUNC_inter>(?=<DegreeP>)"),("FUNC_inter",),("FUNC_negation",)),
            (re.compile("</MODIFIER_color><MODIFIER_color>"), ("</MODIFIER_color><MODIFIER_color>",), ("",)),
            (re.compile("<FUNC_inner>還</FUNC_inner><ACTION_verb>得人惱</ACTION_verb>"),("FUNC_inner",), ("MODIFIER",)),
            (re.compile("<FUNC_inner>還</FUNC_inner><MODIFIER>[^<罅光光]+</MODIFIER>"),("<FUNC_inner>", "</FUNC_inner><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),            
            (re.compile("(<ENTITY_num>[^<]+</ENTITY_num>)<ACTION_verb>[領袋疊托行排]</ACTION_verb>"), ("ACTION_verb",), ("ENTITY_classifier",)),
            (re.compile("(?<=</ENTITY_num>)<ENTITY_noun>個人</ENTITY_noun>"),("<ENTITY_noun>個人</ENTITY_noun>",), ("<ENTITY_classifier>個</ENTITY_classifier><ENTITY_noun>人</ENTITY_noun>",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_noun>[竇頭]</ENTITY_noun>(?=<ENTITY_noun>)"), ("ENTITY_noun",), ("ENTITY_classifier",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>個銀</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>","ENTITY_num","ENTITY_classifier",), ("", "KNOWLEDGE_currency","KNOWLEDGE_currency",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>點鐘</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>","ENTITY_num","ENTITY_classifier",), ("","TIME_justtime","TIME_justtime",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>[^<]+</ENTITY_classifier><ENTITY_classifier>月</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>", "</ENTITY_classifier><ENTITY_classifier>","ENTITY_num","ENTITY_classifier",), ("", "","TIME_justtime","TIME_justtime")),
            (re.compile("<TIME_justtime>[^<]+</TIME_justtime><ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("</TIME_justtime><ENTITY_num>", "</ENTITY_num><ENTITY_classifier>","ENTITY_classifier",), ("","","TIME_justtime")),
            (re.compile("(?<=</ACTION_verb>)<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>擺</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>","ENTITY_num","ENTITY_classifier",), ("","ACTION_eventQuantifier","ACTION_eventQuantifier",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_noun>杯仔</ENTITY_noun><ENTITY_noun>[^<]+</ENTITY_noun>"), ("<ENTITY_noun>杯仔</ENTITY_noun>",), ("<ENTITY_classifier>杯</ENTITY_classifier><FUNC_inner>仔</FUNC_inner>",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>", "ENTITY_num"), ("", "ENTITY_classifier")),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_noun>尺</ENTITY_noun>"), ("ENTITY_noun",), ("ENTITY_measurement",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_measurement>[^<]+</ENTITY_measurement>"), ("</ENTITY_num><ENTITY_measurement>", "ENTITY_num"), ("", "ENTITY_measurement")),
            (re.compile("<ACTION_verb>([^<])</ACTION_verb><ACTION_verb>\\1</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>講</ACTION_verb><ACTION_verb>話</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>[害]+</ACTION_verb><ACTION_verb>死</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<FUNC_degreeHead>[恁盡過當蓋異]</FUNC_degreeHead><ACTION_verb>[^<驚想感謝牽成惱敢有到愁中意得惜會翕]+</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<FUNC_degreeHead>過</FUNC_degreeHead><ACTION_verb>得</ACTION_verb>"),("FUNC_degreeHead",), ("ACTION_verb",)),
            (re.compile("<FUNC_degreeHead>[^<]+</FUNC_degreeHead><MODIFIER>好食</MODIFIER>(?=<ENTITY_noun>)"),("<MODIFIER>好食</MODIFIER>",), ("<ACTION_verb>好</ACTION_verb><ACTION_verb>食</ACTION_verb>",)),
            (re.compile("<FUNC_degreeHead>[^<]+</FUNC_degreeHead><MODIFIER>好搞</MODIFIER>(?=<ENTITY_noun>)"),("<MODIFIER>好搞</MODIFIER>",), ("<ACTION_verb>好</ACTION_verb><ACTION_verb>搞</ACTION_verb>",)),
            (re.compile("<FUNC_degreeHead>過</FUNC_degreeHead><ACTION_verb>到</ACTION_verb>"), ("FUNC_degreeHead",), ("ACTION_verb",)),
            (re.compile("<FUNC_degreeHead>[恁盡過當蓋異]</FUNC_degreeHead><ACTION_verb>[^<]+</ACTION_verb>"), ("FUNC_degreeHead",), ("MODIFIER",)),
            (re.compile("(?<=</FUNC_degreeHead>)<ACTION_verb>贏</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("(<FUNC_degreeHead>當</FUNC_degreeHead>)<MODIFIER>大</MODIFIER><ENTITY_classifier>尾</ENTITY_classifier>"),("</MODIFIER><ENTITY_classifier>", "ENTITY_classifier",), ("", "MODIFIER",)),
            (re.compile("<ENTITY_num>十</ENTITY_num><ACTION_verb>分</ACTION_verb><MODIFIER>[^<]+</MODIFIER>"), ("<ENTITY_num>十</ENTITY_num><ACTION_verb>分</ACTION_verb>",), ("<FUNC_degreeHead>十分</FUNC_degreeHead>",)),
            (re.compile("<FUNC_inner>還</FUNC_inner><ENTITY_noun>壁</ENTITY_noun>"), ("<FUNC_inner>還</FUNC_inner><ENTITY_noun>壁</ENTITY_noun>",), ("<FUNC_degreeHead>還</FUNC_degreeHead><MODIFIER>壁</MODIFIER>",)),
            (re.compile("<MODIFIER>好</MODIFIER><ACTION_verb>計較</ACTION_verb>"),("MODIFIER",), ("ACTION_verb",)),
            (re.compile("<MODIFIER>好</MODIFIER><ACTION_verb>做王</ACTION_verb>"),("MODIFIER",), ("ACTION_verb",)),
            (re.compile("<TIME_justtime>當時</TIME_justtime><ACTION_verb>行</ACTION_verb>"),("<TIME_justtime>當時</TIME_justtime><ACTION_verb>行</ACTION_verb>",), ("<FUNC_degreeHead>當</FUNC_degreeHead><MODIFIER>時行</MODIFIER>",)),
            (re.compile("<FUNC_degreeHead>當</FUNC_degreeHead><MODIFIER>好</MODIFIER>(<ACTION_verb>[^<]+</ACTION_verb>)"),("FUNC_degreeHead", "MODIFIER"), ("MODIFIER", "ACTION_verb")),
            (re.compile("<FUNC_degreeHead>[^<]+</FUNC_degreeHead><MODIFIER>[^<]+</MODIFIER>"),("</FUNC_degreeHead><MODIFIER>", "<FUNC_degreeHead>", "</MODIFIER>"), ("", "<DegreeP>", "</DegreeP>")),
            (re.compile("<DegreeP>恁久</DegreeP><FUNC_inter>無</FUNC_inter>"),("FUNC_inter",),("FUNC_negation",)),           
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>起來</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>[^<會加愛]+</ACTION_verb><ACTION_verb>[著到]</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>加</ACTION_verb>(<ACTION_verb>著</ACTION_verb>)"), ("<ACTION_verb>加</ACTION_verb>",), ("<MODIFIER>加</MODIFIER>",)),
            (re.compile("<ASPECT>忒</ASPECT><MODIFIER>[^<]+</MODIFIER>"),("</ASPECT><MODIFIER>", "ASPECT", "MODIFIER"), ("", "DegreeP", "DegreeP")),
            (re.compile("<FUNC_degreeHead>過</FUNC_degreeHead><ASPECT>忒</ASPECT>"),("FUNC_degreeHead",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>[斷脫]</ACTION_verb><ASPECT>[忒核]</ASPECT>"),("</ACTION_verb><ASPECT>", "ASPECT",), ("", "ACTION_verb")),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><MODIFIER>飽</MODIFIER>"),("</ACTION_verb><MODIFIER>","MODIFIER"), ("","ACTION_verb")),
            (re.compile("(?<=</ACTION_verb>)<TIME_day>夜</TIME_day>"),("TIME_day",), ("ENTITY_noun",)),
            (re.compile("<ASPECT>好</ASPECT>(?=<CLAUSE_Q>)"),("ASPECT",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>[上下]</ACTION_verb><ENTITY_noun>禮拜</ENTITY_noun>"),("</ACTION_verb><ENTITY_noun>","ACTION_verb","ENTITY_noun"), ("","TIME_justtime","TIME_justtime")),
            (re.compile("(?<=</ENTITY_classifier>)<ACTION_verb>妄想</ACTION_verb>"),("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<ACTION_verb>打</ACTION_verb><ACTION_verb>結</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<DegreeP>盡好</DegreeP><ACTION_verb>食</ACTION_verb>"),("DegreeP",), ("ACTION_verb",)),
            (re.compile("(?<=擺</ENTITY_classifier>)<ACTION_verb>旅行</ACTION_verb>"),("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<ACTION_verb>包</ACTION_verb>(?=<ENTITY_noun>)"),("ACTION_verb",), ("ENTITY_classifier",)),
            (re.compile("<FUNC_determiner>這</FUNC_determiner><MODIFIER>滿</MODIFIER>"), ("MODIFIER",), ("ENTITY_classifier",)),
            (re.compile("<FUNC_determiner>這</FUNC_determiner><ENTITY_oov>題</ENTITY_oov>"), ("ENTITY_oov",), ("ENTITY_classifier",)),
            (re.compile("(<FUNC_determiner>這</FUNC_determiner>)<ACTION_verb>[領袋種]</ACTION_verb>"),("ACTION_verb",), ("ENTITY_classifier",)),
            (re.compile("(<FUNC_determiner>[這該]</FUNC_determiner>)<QUANTIFIER>兜</QUANTIFIER>"),("QUANTIFIER",), ("ENTITY_classifier",)),
            (re.compile("<ENTITY_noun>門</ENTITY_noun><ENTITY_noun>親事</ENTITY_noun>"), ("ENTITY_noun",), ("ENTITY_classifier",)),    
            (re.compile("<FUNC_determiner>[^<]+</FUNC_determiner><ENTITY_classifier>[^<]+</ENTITY_classifier>"),("</FUNC_determiner><ENTITY_classifier>","FUNC_determiner","ENTITY_classifier"), ("","ENTITY_DetPhrase","ENTITY_DetPhrase")),
            (re.compile("<ENTITY_pronoun>吾</ENTITY_pronoun><FUNC_degreeHead>太</FUNC_degreeHead>"),("FUNC_degreeHead",), ("ENTITY_pronoun",)),
            (re.compile("<ENTITY_pronoun>[^<]+</ENTITY_pronoun><ENTITY_pronoun>[哥]+</ENTITY_pronoun>"),("</ENTITY_pronoun><ENTITY_pronoun>",), ("",)),
            (re.compile("<ENTITY_pronoun>[^<]+</ENTITY_pronoun>(?=<ENTITY_pronoun>)"),("ENTITY_pronoun",), ("ENTITY_possessive",)),
            (re.compile("<FUNC_inter>無</FUNC_inter><ENTITY_noun>[人風雨辦法東西問題]+</ENTITY_noun>"),("FUNC_inter",), ("FUNC_negation",)),
            (re.compile("<MODIFIER>淰</MODIFIER><ACTION_verb>出來</ACTION_verb>"), ("MODIFIER",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>[^<愛擐會著]+</ACTION_verb><ACTION_verb>[出來下來入得著落去歸轉開來]+</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ENTITY_person>錢放</ENTITY_person>"),("<ENTITY_person>錢放</ENTITY_person>",), ("<ENTITY_noun>錢</ENTITY_noun><ACTION_verb>放</ACTION_verb>",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_classifier>頂</ENTITY_classifier>"),("ENTITY_classifier",), ("RANGE_locality",)),
            (re.compile("<ACTION_verb>晒</ACTION_verb><ENTITY_noun>日頭</ENTITY_noun>"),("</ACTION_verb><ENTITY_noun>","</ENTITY_noun>"), ("","</ACTION_verb>")),
            (re.compile("<ACTION_verb>打開</ACTION_verb><ACTION_verb>來</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<TIME_justtime>過後</TIME_justtime><ACTION_verb>背</ACTION_verb>"), ("<TIME_justtime>過後</TIME_justtime><ACTION_verb>背</ACTION_verb>",), ("<FUNC_degreeHead>過</FUNC_degreeHead><RANGE_locality>後背</RANGE_locality>",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>去</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>逐</ACTION_verb><ENTITY_noun>[禮拜暗晡]</ENTITY_noun>"), ("</ACTION_verb><ENTITY_noun>","ACTION_verb","ENTITY_noun"), ("","TIME_justtime","TIME_justtime")),
            (re.compile("<MODIFIER>每</MODIFIER><ENTITY_noun>禮拜</ENTITY_noun>"), ("</MODIFIER><ENTITY_noun>","MODIFIER","ENTITY_noun"), ("","TIME_justtime","TIME_justtime")),
            (re.compile("(?<=</ASPECT>)<ASPECT>等</ASPECT>"), ("ASPECT",), ("ACTION_verb",)),
            (re.compile("<ENTITY_pronoun>𠊎等</ENTITY_pronoun><TIME_justtime>一下</TIME_justtime>"), ("<ENTITY_pronoun>𠊎等</ENTITY_pronoun><TIME_justtime>一下</TIME_justtime>",), ("<ENTITY_pronoun>𠊎</ENTITY_pronoun><TIME_justtime>等一下</TIME_justtime>",)),
            (re.compile("<ENTITY_pronoun>𠊎等</ENTITY_pronoun><ACTION_verb>下來</ACTION_verb>"), ("<ENTITY_pronoun>𠊎等</ENTITY_pronoun><ACTION_verb>下來</ACTION_verb>",), ("<ENTITY_pronoun>𠊎</ENTITY_pronoun><TIME_justtime>等下</TIME_justtime><ACTION_verb>來</ACTION_verb>",)),
            (re.compile("<FUNC_degreeHead>過</FUNC_degreeHead><ENTITY_noun>[^<]+</ENTITY_noun>"), ("FUNC_degreeHead",), ("ACTION_verb",)),
            (re.compile("(<ACTION_verb>看</ACTION_verb><FUNC_negation>毋</FUNC_negation>)<ACTION_verb>著</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<MODAL>正</MODAL><ACTION_verb>著</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<MODIFIER>罅</MODIFIER><MODIFIER>[^<]+</MODIFIER>"), ("</MODIFIER><MODIFIER>",), ("",)),
            (re.compile("<CLAUSE_particle>([^<])</CLAUSE_particle><CLAUSE_particle>\\1</CLAUSE_particle>"), ("</CLAUSE_particle><CLAUSE_particle>",), ("",)),
            (re.compile("<ACTION_verb>著</ACTION_verb>(<ENTITY_oov>片</ENTITY_oov>)"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<ENTITY_noun>鉛筆</ENTITY_noun><ENTITY_noun>盒仔</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>",), ("",)),
            (re.compile("<QUANTIFIER>兜</QUANTIFIER><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("QUANTIFIER",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>歸</ACTION_verb><ENTITY_noun>個人</ENTITY_noun>"), ("<ACTION_verb>歸</ACTION_verb><ENTITY_noun>個人</ENTITY_noun>",), ("<QUANTIFIER>歸</QUANTIFIER><ENTITY_classifier>個</ENTITY_classifier><ENTITY_noun>人</ENTITY_noun>",)),
            (re.compile("<ENTITY_noun>個人</ENTITY_noun><ENTITY_oov>公</ENTITY_oov><FUNC_inner>仔</FUNC_inner>"), ("<ENTITY_noun>個人</ENTITY_noun><ENTITY_oov>公</ENTITY_oov><FUNC_inner>仔</FUNC_inner>",), ("<ENTITY_classifier>個</ENTITY_classifier><ENTITY_noun>人公仔</ENTITY_noun>",)),
            (re.compile("<ACTION_verb>著</ACTION_verb><FUNC_conjunction>抑</FUNC_conjunction><FUNC_negation>毋</FUNC_negation><ACTION_verb>著</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<ACTION_verb>寫</ACTION_verb><FUNC_negation>毋</FUNC_negation><ACTION_verb>著</ACTION_verb>"), ("<ACTION_verb>著</ACTION_verb>",), ("<MODIFIER>著</MODIFIER>",)),
            (re.compile("<ENTITY_classifier>有兜</ENTITY_classifier>"), ("<ENTITY_classifier>有兜</ENTITY_classifier>",), ("<ACTION_verb>有</ACTION_verb><QUANTIFIER>兜</QUANTIFIER>",)),
            (re.compile("(<ACTION_verb>有</ACTION_verb>)<QUANTIFIER>兜</QUANTIFIER><FUNC_inner>仔</FUNC_inner>"), ("</QUANTIFIER><FUNC_inner>","FUNC_inner",), ("","QUANTIFIER",)),
            (re.compile("<ACTION_verb>壞</ACTION_verb><MODIFIER>淨淨</MODIFIER>"), ("</ACTION_verb><MODIFIER>","ACTION_verb",), ("","MODIFIER",)),
            (re.compile("<MODIFIER_color>[^<]+</MODIFIER_color><ENTITY_noun>色</ENTITY_noun>"), ("</MODIFIER_color><ENTITY_noun>","ENTITY_noun",), ("","MODIFIER_color",)),
            (re.compile("<ACTION_verb>食</ACTION_verb><ACTION_verb>壞</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<DegreeP>還細</DegreeP><MODIFIER>細</MODIFIER>"), ("<DegreeP>還細</DegreeP><MODIFIER>細</MODIFIER>",), ("<FUNC_inner>還</FUNC_inner><MODIFIER>細細</MODIFIER>",)),
            (re.compile("<ENTITY_person>毋知愛</ENTITY_person>"), ("<ENTITY_person>毋知愛</ENTITY_person>",), ("<FUNC_negation>毋</FUNC_negation><ACTION_verb>知</ACTION_verb><ACTION_verb>愛</ACTION_verb>",)),
            (re.compile("<DegreeP>恁大</DegreeP><ENTITY_noun>力</ENTITY_noun>"), ("</DegreeP><ENTITY_noun>","ENTITY_noun",), ("","DegreeP",)),
            (re.compile("<ACTION_verb>同</ACTION_verb>(?=.*<ACTION_verb>[阿腦討食借講行行棋仔]+</ACTION_verb>)"), ("ACTION_verb",), ("FUNC_conjunction",)),
            (re.compile("<ACTION_verb>同</ACTION_verb><ENTITY_noun>人</ENTITY_noun>"), ("ACTION_verb",), ("FUNC_conjunction",)),
            (re.compile("<ACTION_verb>好好</ACTION_verb>(?=<ACTION_verb>)"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<ACTION_verb>[^<喊]+</ACTION_verb><FUNC_negation>毋</FUNC_negation><ACTION_verb>[^<慣]+</ACTION_verb>"), ("</ACTION_verb><FUNC_negation>","</FUNC_negation><ACTION_verb>",), ("","",)),
            (re.compile("<ACTION_verb>敢</ACTION_verb><FUNC_inner>還</FUNC_inner>"), ("ACTION_verb",), ("CLAUSE_Q",)),
            (re.compile("<ENTITY_oov>蘿蔔</ENTITY_oov><ENTITY_noun>湯</ENTITY_noun>"), ("</ENTITY_oov><ENTITY_noun>","ENTITY_oov",), ("", "ENTITY_noun",)),
            (re.compile("<ACTION_verb>同</ACTION_verb><ENTITY_noun>[^<]+</ENTITY_noun>$"), ("ACTION_verb",), ("FUNC_conjunction",)),
            (re.compile("<ACTION_verb>在</ACTION_verb><FUNC_determiner>該</FUNC_determiner>(?=<ACTION_verb>)"), ("FUNC_determiner",), ("LOCATION",)),
            (re.compile("<FUNC_inter>無</FUNC_inter><CLAUSE_Q>[幾多麼个幾久]+</CLAUSE_Q>"), ("FUNC_inter",), ("FUNC_negation",)),
            (re.compile("<FUNC_inter>係講</FUNC_inter>(?=.*<FUNC_conjunction>抑</FUNC_conjunction>)"), ("<FUNC_inter>係講</FUNC_inter>",), ("<AUX>係</AUX><ACTION_verb>講</ACTION_verb>",)),
            (re.compile("<ENTITY_noun>青天白日</ENTITY_noun>"), ("ENTITY_noun",), ("IDIOM",)),
            (re.compile("<ENTITY_noun>差</ENTITY_noun>(?=<ENTITY_num>)"), ("ENTITY_noun",), ("ACTION_verb",)),
            (re.compile("<MODIFIER>有孝</MODIFIER>(?=<ENTITY_pronoun>)"), ("MODIFIER",), ("ACTION_verb",)),
            (re.compile("<ENTITY_noun>責任</ENTITY_noun><ENTITY_nounHead>感</ENTITY_nounHead>"), ("</ENTITY_noun><ENTITY_nounHead>","ENTITY_nounHead",), ("", "ENTITY_noun",)),
            (re.compile("<ACTION_verb>請</ACTION_verb><ACTION_verb>問</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ENTITY_classifier>班</ENTITY_classifier><RANGE_locality>項</RANGE_locality>"), ("ENTITY_classifier",), ("ENTITY_noun",)),
            (re.compile("(<ACTION_verb>有</ACTION_verb>).*<MODIFIER>好食</MODIFIER>"), ("<MODIFIER>好食</MODIFIER>",), ("<MODAL>好</MODAL><ACTION_verb>食</ACTION_verb>",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_noun>罐仔</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>",), ("",)),
            (re.compile("<MODIFIER>[^<]+</MODIFIER><ACTION_verb>希望</ACTION_verb>"), ("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<MODIFIER>[^<]+</MODIFIER><ENTITY_noun>[裙門希望]+</ENTITY_noun>"), ("</MODIFIER><ENTITY_noun>","MODIFIER",), ("","ENTITY_noun",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_oov>店</ENTITY_oov>"), ("</ENTITY_noun><ENTITY_oov>","ENTITY_oov"), ("","ENTITY_noun",)),
            (re.compile("<ENTITY_noun>傳統</ENTITY_noun><ENTITY_noun>風俗</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>",), ("",)),
            (re.compile("<ENTITY_noun>門</ENTITY_noun><ENTITY_noun>親事</ENTITY_noun>"), ("ENTITY_noun",), ("ENTITY_classifier",)),
            (re.compile("<FUNC_negation>毋</FUNC_negation><MODIFIER>好</MODIFIER>(?=.*<ACTION_verb>)"), ("</FUNC_negation><MODIFIER>","MODIFIER",), ("","FUNC_negation",)),
            (re.compile("<MODIFIER>好食</MODIFIER><MODIFIER>晝</MODIFIER>"), ("<MODIFIER>好食</MODIFIER><MODIFIER>晝</MODIFIER>",), ("<MODIFIER>好</MODIFIER><ACTION_verb>食晝</ACTION_verb>",)),
            (re.compile("<MODIFIER>好</MODIFIER>(?=<ACTION_verb>(?!怕))"), ("MODIFIER",), ("MODAL",)),
            (re.compile("<MODIFIER>好</MODIFIER><MODIFIER>先</MODIFIER><ACTION_verb>食</ACTION_verb>"), ("<MODIFIER>好</MODIFIER>",), ("<MODAL>好</MODAL>",)),
            (re.compile("(?<=</ACTION_verb>)<MODIFIER>第</MODIFIER><ENTITY_num>[^<]+</ENTITY_num>"), ("</MODIFIER><ENTITY_num>","ENTITY_num",), ("","MODIFIER",)),
            (re.compile("</ENTITY_pronoun><TIME_justtime>一下</TIME_justtime><ENTITY_noun>課</ENTITY_noun>"), ("</ENTITY_pronoun><TIME_justtime>一下</TIME_justtime><ENTITY_noun>課</ENTITY_noun>",), ("</ENTITY_pronoun><TIME_justtime>一</TIME_justtime><ACTION_verb>下課</ACTION_verb>",)),
            (re.compile("<ACTION_verb>轉</ACTION_verb><ENTITY_noun>[屋家屋下]+</ENTITY_noun>"), ("</ACTION_verb><ENTITY_noun>","ENTITY_noun",), ("","ACTION_verb",)),
            (re.compile("<ENTITY_noun>畫</ENTITY_noun>((?=<ENTITY_classifier>)|(?=<ENTITY_noun>))"), ("ENTITY_noun",), ("ACTION_verb",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_noun>粥</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>",), ("",)),
            (re.compile("<MODIFIER>幾下</MODIFIER>(<ENTITY_classifier>隻</ENTITY_classifier>)"), ("MODIFIER",), ("QUANTIFIER",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ENTITY_classifier>張</ENTITY_classifier>"), ("ENTITY_classifier",), ("ACTION_verb",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><FUNC_degreeHead>過</FUNC_degreeHead><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("</ENTITY_num><FUNC_degreeHead>","</FUNC_degreeHead><ENTITY_classifier>","ENTITY_num",), ("","","ENTITY_classifier")),
            (re.compile("(?<=</ENTITY_noun>)<ENTITY_noun>肚</ENTITY_noun>"), ("ENTITY_noun",), ("RANGE_locality",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><CLAUSE_particle>啊</CLAUSE_particle><DegreeP>[^<]+</DegreeP>"), ("</ACTION_verb><CLAUSE_particle>","CLAUSE_particle",), ("","ACTION_verb",)),
            (re.compile("<ACTION_verb>切</ACTION_verb><ACTION_verb>做</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ENTITY_oov>[^<]+</ENTITY_oov><ENTITY_noun>卵</ENTITY_noun>"), ("</ENTITY_oov><ENTITY_noun>","ENTITY_oov",), ("","ENTITY_noun",)),
            (re.compile("<ACTION_verb>歸</ACTION_verb><ENTITY_noun>家</ENTITY_noun><ENTITY_noun>人</ENTITY_noun>"), ("<ENTITY_noun>家</ENTITY_noun>",), ("<ENTITY_classifier>家</ENTITY_classifier>",)),
            (re.compile("<ACTION_verb>[歸逐]+</ACTION_verb>((?=<ENTITY_classifier>)|(?=<TIME_justtime>))"), ("ACTION_verb",), ("QUANTIFIER",)),
            (re.compile("<ACTION_verb>[停唱抽借變有暈判駛]+</ACTION_verb><ENTITY_noun>[船血電歌仔錢天興趣罪車]+</ENTITY_noun>"), ("</ACTION_verb><ENTITY_noun>","ENTITY_noun"), ("","ACTION_verb",)),
            (re.compile("<DegreeP>盡遽</DegreeP><MODIFIER>燥</MODIFIER>"), ("</DegreeP><MODIFIER>","MODIFIER"), ("","DegreeP",)),
            (re.compile("<ACTION_verb>吹</ACTION_verb><MODIFIER>燥</MODIFIER>"), ("</ACTION_verb><MODIFIER>","MODIFIER"), ("","ACTION_verb",)),
            (re.compile("<ACTION_verb>著</ACTION_verb><ACTION_verb>領</ACTION_verb>"), ("<ACTION_verb>領</ACTION_verb>",), ("<ENTITY_classifier>領</ENTITY_classifier>",)),
            (re.compile("<FUNC_negation>無</FUNC_negation><CLAUSE_Q>麼个</CLAUSE_Q>"), ("CLAUSE_Q",), ("QUANTIFIER",)),
            (re.compile("<ENTITY_noun>[樹桌]+</ENTITY_noun><ACTION_verb>下</ACTION_verb>"), ("ACTION_verb",), ("RANGE_locality",)),
            (re.compile("<MODIFIER>尖</MODIFIER><ENTITY_noun>[^<]+</ENTITY_noun>"), ("MODIFIER",), ("ACTION_verb",)),
            (re.compile("<MODIFIER>共</MODIFIER><ENTITY_classifier>組</ENTITY_classifier>"), ("ENTITY_classifier",), ("ENTITY_noun",)),
            (re.compile("<MODIFIER>[^<好得儘採]+</MODIFIER><ENTITY_noun>[^<]+</ENTITY_noun>"), ("</MODIFIER><ENTITY_noun>","MODIFIER",), ("","ENTITY_noun",)),
            (re.compile("<MODIFIER>儘採</MODIFIER><ENTITY_noun>料理</ENTITY_noun>"), ("ENTITY_noun",), ("ACTION_verb",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_oov>港</ENTITY_oov>"), ("</ENTITY_noun><ENTITY_oov>","ENTITY_oov",), ("","ENTITY_noun",)),
            (re.compile("<ACTION_verb>紀念</ACTION_verb><ENTITY_noun>價值</ENTITY_noun>"), ("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<ENTITY_noun>客家</ENTITY_noun><ACTION_verb>研究</ACTION_verb>"), ("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<ENTITY_noun>[^<選手]+</ENTITY_noun><ENTITY_noun>[菜油票比賽袋箱仔糖湯課海報桌山風肉毛價值理想方面色絲研究水人物能力認證考試研究所]+</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>",), ("",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_oov>[炎部]+</ENTITY_oov>"), ("</ENTITY_noun><ENTITY_oov>","ENTITY_oov",), ("","ENTITY_noun")),
            (re.compile("(?<=</ACTION_verb>)<ENTITY_num>[^<]+</ENTITY_num><ACTION_verb>到</ACTION_verb>"), ("</ENTITY_num><ACTION_verb>","ENTITY_num","ACTION_verb",), ("","ACTION_eventQuantifier","ACTION_eventQuantifier",)),
            (re.compile("<FUNC_determiner>這</FUNC_determiner><ENTITY_noun>禮拜</ENTITY_noun>"), ("</FUNC_determiner><ENTITY_noun>","FUNC_determiner","ENTITY_noun",), ("","TIME_justtime","TIME_justtime",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ENTITY_noun>差</ENTITY_noun>"), ("ENTITY_noun",), ("MODIFIER",)),
            (re.compile("<ENTITY_pronoun>阿爸</ENTITY_pronoun><FUNC_degreeHead>較</FUNC_degreeHead><FUNC_negation>毋</FUNC_negation><MODIFIER>好</MODIFIER>"), ("MODIFIER",), ("ACTION_verb",)),
            (re.compile("<TIME_justtime>[^<]+</TIME_justtime><ENTITY_num>[^<]+</ENTITY_num>(?!<ENTITY_noun>歲</ENTITY_noun>)"), ("</TIME_justtime><ENTITY_num>","ENTITY_num",), ("","TIME_justtime",)),
            (re.compile("<FUNC_negation>毋</FUNC_negation><MODIFIER>好食</MODIFIER>"), ("<FUNC_negation>毋</FUNC_negation><MODIFIER>好食</MODIFIER>",), ("<FUNC_negation>毋好</FUNC_negation><ACTION_verb>食</ACTION_verb>",)),
            (re.compile("</ENTITY_pronoun>.*?<FUNC_negation>無</FUNC_negation><MODIFIER>好食</MODIFIER>"), ("<MODIFIER>好食</MODIFIER>",), ("<ACTION_verb>好</ACTION_verb><ACTION_verb>食</ACTION_verb>",)),
            (re.compile("<ACTION_verb>堆</ACTION_verb><ENTITY_oov>尿</ENTITY_oov>"), ("ACTION_verb",), ("ENTITY_classifier",)),
            (re.compile("<MODIFIER>第</MODIFIER><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("</MODIFIER><ENTITY_classifier>","MODIFIER","ENTITY_classifier",), ("","ENTITY_DetPhrase","ENTITY_DetPhrase",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><TIME_justtime>[禮拜年]</TIME_justtime>"), ("</ENTITY_num><TIME_justtime>","ENTITY_num",), ("","TIME_justtime",)),
            (re.compile("(?<=</ENTITY_classifier>)<ACTION_verb>炒</ACTION_verb><ENTITY_noun>蕹菜</ENTITY_noun>"), ("</ACTION_verb><ENTITY_noun>","ACTION_verb",), ("","ENTITY_noun",)),
            (re.compile("<LOCATION>[^<]+</LOCATION><ENTITY_classifier>站</ENTITY_classifier>"), ("</LOCATION><ENTITY_classifier>","ENTITY_classifier",), ("","LOCATION",)),
            (re.compile("<ENTITY_noun>好食冰</ENTITY_noun>"), ("<ENTITY_noun>好食冰</ENTITY_noun>",), ("<ACTION_verb>好</ACTION_verb><ACTION_verb>食</ACTION_verb><ENTITY_noun>冰</ENTITY_noun>",)),
            (re.compile("<FUNC_inner>又</FUNC_inner><ACTION_verb>[^<]+</ACTION_verb><FUNC_inner>又</FUNC_inner><MODIFIER>好</MODIFIER>"), ("MODIFIER",), ("ACTION_verb",)),
            (re.compile("<MODIFIER>[^<]+</MODIFIER><ENTITY_oov>[獎粄]+</ENTITY_oov>"), ("</MODIFIER><ENTITY_oov>", "MODIFIER", "ENTITY_oov",), ("","ENTITY_noun","ENTITY_noun",)),
            (re.compile("<ENTITY_person>毋知走</ENTITY_person>"), ("<ENTITY_person>毋知走</ENTITY_person>",), ("<FUNC_negation>毋</FUNC_negation><ACTION_verb>知</ACTION_verb><ACTION_verb>走</ACTION_verb>",)),
            (re.compile("<ENTITY_noun>[步豬腸]+</ENTITY_noun><FUNC_inner>仔</FUNC_inner>"), ("</ENTITY_noun><FUNC_inner>","FUNC_inner",), ("","ENTITY_noun",)),
            (re.compile("<CLAUSE_Q>幾</CLAUSE_Q>.*?<FUNC_inner>就</FUNC_inner>"), ("CLAUSE_Q",), ("QUANTIFIER",)),
            (re.compile("<ACTION_verb>拜</ACTION_verb><ENTITY_num>[^<]+</ENTITY_num>"), ("</ACTION_verb><ENTITY_num>","ACTION_verb","ENTITY_num",), ("","TIME_justtime","TIME_justtime")),
            (re.compile("<MODIFIER>當在該</MODIFIER><ACTION_verb>[^<]+</ACTION_verb>"), ("MODIFIER",), ("ASPECT",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>得到</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<TIME_justtime>禮拜日</TIME_justtime><ENTITY_classifier>日</ENTITY_classifier>"), ("<TIME_justtime>禮拜日</TIME_justtime><ENTITY_classifier>日</ENTITY_classifier>",), ("<TIME_justtime>禮拜</TIME_justtime><TIME_justtime>日日</TIME_justtime>",)),
            (re.compile("<FUNC_determiner>這</FUNC_determiner><TIME_justtime>禮拜</TIME_justtime>"), ("</FUNC_determiner><TIME_justtime>","FUNC_determiner",), ("","TIME_justtime",)),
            (re.compile("<ACTION_verb>[上下]</ACTION_verb><TIME_justtime>[禮拜一禮拜六]+</TIME_justtime>"), ("</ACTION_verb><TIME_justtime>","ACTION_verb",), ("","TIME_justtime",)),
            (re.compile("<ACTION_verb>[上下]</ACTION_verb><ENTITY_classifier>隻</ENTITY_classifier><ENTITY_classifier>月</ENTITY_classifier>"), ("</ACTION_verb><ENTITY_classifier>","</ENTITY_classifier><ENTITY_classifier>","ACTION_verb","ENTITY_classifier",), ("","","TIME_justtime","TIME_justtime",)),
            (re.compile("<ENTITY_noun>身體</ENTITY_noun><ACTION_verb>檢查</ACTION_verb>"), ("</ENTITY_noun><ACTION_verb>","ACTION_verb",), ("","ENTITY_noun",)),
            (re.compile("<CLAUSE_Q>嗄</CLAUSE_Q><ACTION_verb>[^<]+</ACTION_verb>"), ("CLAUSE_Q",), ("FUNC_inter",)),
            (re.compile("<ENTITY_classifier>包</ENTITY_classifier><ENTITY_noun>尿布仔</ENTITY_noun>"), ("ENTITY_classifier",), ("ACTION_verb",)),
            (re.compile("<AUX>係</AUX>.*?<FUNC_inner>斯</FUNC_inner>"), ("AUX","FUNC_inner",), ("FUNC_inter","AUX",)),
            (re.compile("<FUNC_inter>無</FUNC_inter><ENTITY_oov>責</ENTITY_oov><FUNC_inter>無</FUNC_inter><ENTITY_classifier>任</ENTITY_classifier>"), ("ENTITY_oov","ENTITY_classifier","FUNC_inter",), ("ENTITY_noun","ENTITY_noun","FUNC_negation",)),
            (re.compile("<QUANTIFIER>歸</QUANTIFIER><TIME_justtime>[^<]+</TIME_justtime><FUNC_inner>仔</FUNC_inner>"), ("</QUANTIFIER><TIME_justtime>","QUANTIFIER","</TIME_justtime><FUNC_inner>","FUNC_inner"), ("","TIME_justtime","", "TIME_justtime")),
            (re.compile("<MODIFIER>餓</MODIFIER><ACTION_verb>死</ACTION_verb>"), ("</MODIFIER><ACTION_verb>","MODIFIER",), ("","ACTION_verb",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>看</ACTION_verb><CLAUSE_particle>啊</CLAUSE_particle>"), ("</ACTION_verb><ACTION_verb>","</ACTION_verb><CLAUSE_particle>","ACTION_verb","CLAUSE_particle",), ("","","ACTION_quantifiedVerb","ACTION_quantifiedVerb",)),
            (re.compile("<QUANTIFIER>兜</QUANTIFIER>.*?<ENTITY_noun>飯碗</ENTITY_noun>"), ("QUANTIFIER",), ("ACTION_verb",)),
            (re.compile("<FUNC_inner>个</FUNC_inner><ACTION_verb>公告</ACTION_verb>"), ("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<FUNC_degreeHead>蓋</FUNC_degreeHead><ENTITY_noun>被</ENTITY_noun>"), ("FUNC_degreeHead",), ("ACTION_verb",)),
            (re.compile("^<ASPECT>核</ASPECT>"), ("ASPECT",), ("ENTITY_noun",)),
            (re.compile("<DegreeP>較大</DegreeP><ENTITY_noun>力</ENTITY_noun>"), ("<DegreeP>較大</DegreeP><ENTITY_noun>力</ENTITY_noun>",), ("<DegreeP>較大力</DegreeP>",)),
            (re.compile("<ACTION_verb>偷</ACTION_verb>(<ENTITY_noun>[^<]+</ENTITY_noun>).*?<FUNC_inter>毋過</FUNC_inter><ENTITY_noun>手</ENTITY_noun>"), ("<FUNC_inter>毋過</FUNC_inter>",), ("<FUNC_negation>毋</FUNC_negation><ACTION_verb>過</ACTION_verb>",)),
            (re.compile("<ACTION_verb>偷</ACTION_verb><ACTION_verb>[^<]+</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<MODIFIER>無法度</MODIFIER><ACTION_verb>[^<]+</ACTION_verb>"), ("MODIFIER",), ("FUNC_negation",)),
            (re.compile("<ENTITY_person>毋知仰</ENTITY_person><FUNC_inner>仔</FUNC_inner>"), ("<ENTITY_person>毋知仰</ENTITY_person><FUNC_inner>仔</FUNC_inner>",), ("<FUNC_negation>毋</FUNC_negation><ACTION_verb>知</ACTION_verb><CLAUSE_Q>仰仔</CLAUSE_Q>",)),
            (re.compile("<MODIFIER>[^<]+</MODIFIER><QUANTIFIER>都</QUANTIFIER>"), ("QUANTIFIER",), ("ACTION_verb",)),
            (re.compile("<TIME_justtime>緊</TIME_justtime><ACTION_verb>尞</ACTION_verb><MODIFIER>緊</MODIFIER><MODIFIER>懶尸</MODIFIER>"), ("<TIME_justtime>緊</TIME_justtime>","<MODIFIER>緊</MODIFIER>"), ("<FUNC_inner>緊</FUNC_inner>","<FUNC_inner>緊</FUNC_inner>",)),
            (re.compile("<ENTITY_person>錢正一</ENTITY_person><ENTITY_noun>息仔</ENTITY_noun>"), ("<ENTITY_person>錢正一</ENTITY_person><ENTITY_noun>息仔</ENTITY_noun>",), ("<ENTITY_noun>錢</ENTITY_noun><FUNC_inner>正</FUNC_inner><QUANTIFIER>一息仔</QUANTIFIER>",)),
            (re.compile("<ACTION_verb>敢</ACTION_verb><ACTION_verb>有</ACTION_verb>"), ("<ACTION_verb>敢</ACTION_verb>",), ("<CLAUSE_Q>敢</CLAUSE_Q>",)),
            (re.compile("<ACTION_verb>有</ACTION_verb><ACTION_verb>燒</ACTION_verb>"), ("<ACTION_verb>燒</ACTION_verb>",), ("<MODIFIER>燒</MODIFIER>",)),
            (re.compile("<CLAUSE_particle>阿</CLAUSE_particle><ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_oov>伯</ENTITY_oov>"), ("</CLAUSE_particle><ENTITY_noun>","</ENTITY_noun><ENTITY_oov>","CLAUSE_particle","ENTITY_oov",), ("","","ENTITY_noun","ENTITY_noun",)),
            (re.compile("<ACTION_verb>有</ACTION_verb><ACTION_verb>燒</ACTION_verb>"), ("<ACTION_verb>燒</ACTION_verb>",), ("<MODIFIER>燒</MODIFIER>",)),
            (re.compile("<ENTITY_noun>比賽</ENTITY_noun><MODIFIER>前</MODIFIER>"), ("ENTITY_noun","MODIFIER",), ("ACTION_verb","TIME_justtime",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_oov>器</ENTITY_oov>"), ("</ENTITY_noun><ENTITY_oov>","ENTITY_oov",), ("","ENTITY_noun",)),
            (re.compile("<MODIFIER_color>[^<]+</MODIFIER_color><ENTITY_classifier>燈</ENTITY_classifier>"), ("ENTITY_classifier",), ("ENTITY_noun",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_oov>科</ENTITY_oov>"), ("</ENTITY_noun><ENTITY_oov>","ENTITY_oov",), ("","ENTITY_noun",)),
            (re.compile("<ACTION_verb>愛</ACTION_verb><ACTION_verb>記得</ACTION_verb><FUNC_inner>還</FUNC_inner>"), ("FUNC_inner",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>分</ACTION_verb><ENTITY_pronoun>你</ENTITY_pronoun><ENTITY_noun>主意</ENTITY_noun>"), ("ENTITY_noun",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>做毋著</ACTION_verb>(<ENTITY_noun>[^<]+</ENTITY_noun>)"), ("<ACTION_verb>做毋著</ACTION_verb>",), ("<ACTION_verb>做</ACTION_verb><FUNC_negation>毋</FUNC_negation><MODIFIER>著</MODIFIER>",)),
            (re.compile("<TIME_justtime>兩點</TIME_justtime><ENTITY_noun>心</ENTITY_noun>"), ("<TIME_justtime>兩點</TIME_justtime><ENTITY_noun>心</ENTITY_noun>",), ("<ENTITY_num>兩</ENTITY_num><ENTITY_noun>點心</ENTITY_noun>",)),
            (re.compile("<ENTITY_noun>習慣</ENTITY_noun><ACTION_verb>[^<]+</ACTION_verb>"), ("ENTITY_noun",), ("ACTION_verb",)),
            (re.compile("<ENTITY_classifier>張</ENTITY_classifier><FUNC_negation>毋</FUNC_negation><ACTION_verb>落</ACTION_verb>"), ("ENTITY_classifier",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>收</ACTION_verb><MODAL>好</MODAL><ACTION_verb>來</ACTION_verb>"), ("MODAL",), ("MODIFIER",)),
            (re.compile("(<ACTION_verb>做</ACTION_verb>|<DegreeP>恁多</DegreeP>)<ACTION_verb>種</ACTION_verb>"), ("<ACTION_verb>種</ACTION_verb>",), ("<ENTITY_noun>種</ENTITY_noun>",)),
            (re.compile("<QUANTIFIER>歸</QUANTIFIER><ENTITY_classifier>身</ENTITY_classifier>"), ("ENTITY_classifier",), ("ENTITY_noun",)),
            (re.compile("<ENTITY_noun>花</ENTITY_noun><ASPECT>忒</ASPECT>"), ("ENTITY_noun",), ("ACTION_verb",)),
            (re.compile("<LOCATION>[^<]+</LOCATION><ENTITY_noun>[區市]+</ENTITY_noun>"), ("</LOCATION><ENTITY_noun>","ENTITY_noun",), ("","LOCATION",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_noun>[區市]+</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>","ENTITY_noun",), ("","LOCATION",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_noun>路</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>","ENTITY_noun",), ("","LOCATION",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_noun>樓</ENTITY_noun>"), ("</ENTITY_num><ENTITY_noun>","ENTITY_num",), ("","ENTITY_noun",)),
            (re.compile("<ENTITY_noun>文山</ENTITY_noun><ENTITY_noun>里</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>","ENTITY_noun",), ("","LOCATION",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_noun>國中</ENTITY_noun>"), ("</ENTITY_noun><ENTITY_noun>",), ("",)),
            (re.compile("<LOCATION>[^<]+</LOCATION><ENTITY_noun>大學</ENTITY_noun>"), ("</LOCATION><ENTITY_noun>","LOCATION",), ("","ENTITY_noun",)),
            (re.compile("<FUNC_inner>還</FUNC_inner>$"),("FUNC_inner",),("ACTION_verb",)),
            (re.compile("<MODIFIER>一等</MODIFIER><MODIFIER>[^<]+</MODIFIER>"),("</MODIFIER><MODIFIER>",),("",)),
            (re.compile("<CLAUSE_Q>做麼个</CLAUSE_Q>(<ENTITY_noun>[^<]+</ENTITY_noun>)"),("<CLAUSE_Q>做麼个</CLAUSE_Q>",),("<ACTION_verb>做</ACTION_verb><CLAUSE_Q>麼个</CLAUSE_Q>",)),
            (re.compile("<CLAUSE_Q>幾多</CLAUSE_Q><TIME_justtime>年</TIME_justtime><ACTION_verb>生</ACTION_verb>"),("</TIME_justtime><ACTION_verb>","TIME_justtime","ACTION_verb",),("","ENTITY_noun","ENTITY_noun",)),
            (re.compile("<ENTITY_person>項走</ENTITY_person><ENTITY_oov>相</ENTITY_oov><ACTION_verb>逐</ACTION_verb>"),("<ENTITY_person>項走</ENTITY_person><ENTITY_oov>相</ENTITY_oov><ACTION_verb>逐</ACTION_verb>",),("<RANGE_locality>項</RANGE_locality><ACTION_verb>走相逐</ACTION_verb>",)),
            (re.compile("<ENTITY_person>項畫</ENTITY_person>"),("<ENTITY_person>項畫</ENTITY_person>",),("<RANGE_locality>項</RANGE_locality><ACTION_verb>畫</ACTION_verb>",)),
            (re.compile("<ENTITY_num>十</ENTITY_num><ACTION_verb>過年</ACTION_verb>"),("</ENTITY_num><ACTION_verb>","ENTITY_num","ACTION_verb"),("","TIME_justtime","TIME_justtime")),
            (re.compile("<ENTITY_pronoun>[^<]+</ENTITY_pronoun><FUNC_inner>仔</FUNC_inner>"),("</ENTITY_pronoun><FUNC_inner>","FUNC_inner",),("","ENTITY_pronoun",)),
]