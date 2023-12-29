#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tempfile
import platform

try:
    from HAC_dict.xi_ien.pre_elementary_level import ACTION_verb as hac_ActionVerb
    from HAC_dict.xi_ien.pre_elementary_level import CLAUSE_particle as hac_ClauseParticle
    from HAC_dict.xi_ien.pre_elementary_level import CLAUSE_Q as hac_ClauseQ
    from HAC_dict.xi_ien.pre_elementary_level import ENTITY_classifier as hac_EntityClassifier
    from HAC_dict.xi_ien.pre_elementary_level import ENTITY_noun as hac_EntityNoun
    from HAC_dict.xi_ien.pre_elementary_level import ENTITY_pronoun as hac_EntityPronoun
    from HAC_dict.xi_ien.pre_elementary_level import FUNC_conjunction as hac_FuncConjunction
    from HAC_dict.xi_ien.pre_elementary_level import FUNC_inner as hac_FuncInner
    from HAC_dict.xi_ien.pre_elementary_level import FUNC_inter as hac_FuncInter
    from HAC_dict.xi_ien.pre_elementary_level import IDIOM as hac_Idiom
    from HAC_dict.xi_ien.pre_elementary_level import LOCATION as hac_Location
    from HAC_dict.xi_ien.pre_elementary_level import MODIFIER as hac_Modifier
    from HAC_dict.xi_ien.pre_elementary_level import RANGE_locality as hac_RangeLocality
    from HAC_dict.xi_ien.pre_elementary_level import TIME_justtime as hac_TimeJusttime
    from HAC_dict.xi_ien.pre_elementary_level import TIME_season as hac_TimeSeason

    from IreneHAKKA_dict.ACTION_eventQuantifier import DT_ActionEventQuantifier
    from IreneHAKKA_dict.ACTION_lightVerb import DT_ActionLightVerb
    from IreneHAKKA_dict.ACTION_quantifiedVerb import DT_ActionQuantifiedVerb
    from IreneHAKKA_dict.ACTION_verb import DT_ActionVerb
    from IreneHAKKA_dict.ASPECT import DT_Aspect
    from IreneHAKKA_dict.AUX import DT_Aux
    from IreneHAKKA_dict.CLAUSE_particle import DT_ClauseParticle
    from IreneHAKKA_dict.CLAUSE_Q import DT_ClauseQ
    from IreneHAKKA_dict.ENTITY_classifier import DT_EntityClassifier
    from IreneHAKKA_dict.ENTITY_DetPhrase import DT_EntityDetPhrase
    from IreneHAKKA_dict.ENTITY_measurement import DT_EntityMeasurement
    from IreneHAKKA_dict.ENTITY_noun import DT_EntityNoun
    from IreneHAKKA_dict.ENTITY_num import DT_EntityNum
    from IreneHAKKA_dict.ENTITY_person import DT_EntityPerson
    from IreneHAKKA_dict.ENTITY_possessive import DT_EntityPossessive
    from IreneHAKKA_dict.ENTITY_pronoun import DT_EntityPronoun
    from IreneHAKKA_dict.FUNC_degreeHead import DT_FuncDegreeHead
    from IreneHAKKA_dict.FUNC_inner import DT_FuncInner
    from IreneHAKKA_dict.FUNC_inter import DT_FuncInter
    from IreneHAKKA_dict.FUNC_negation import DT_FuncNegation
    from IreneHAKKA_dict.FUNC_conjunction import DT_FuncConjunction
    from IreneHAKKA_dict.IDIOM import DT_Idiom
    from IreneHAKKA_dict.LOCATION import DT_Location
    from IreneHAKKA_dict.TIME_justtime import DT_TimeJusttime
    from IreneHAKKA_dict.MODAL import DT_Modal
    from IreneHAKKA_dict.MODIFIER import DT_Modifier
    from IreneHAKKA_dict.MODIFIER_color import DT_ModifierColor
    from IreneHAKKA_dict.QUANTIFIER import DT_Quantifier
    from IreneHAKKA_dict.RANGE_period import DT_RangePeriod
    from IreneHAKKA_dict.RANGE_Locality import DT_RangeLocality

except:
    from .HAC_dict.xi_ien.pre_elementary_level.ACTION_verb import hac_ActionVerb
    from .HAC_dict.xi_ien.pre_elementary_level.CLAUSE_particle import hac_ClauseParticle
    from .HAC_dict.xi_ien.pre_elementary_level.CLAUSE_Q import hac_ClauseQ
    from .HAC_dict.xi_ien.pre_elementary_level.ENTITY_classifier import hac_EntityClassifier
    from .HAC_dict.xi_ien.pre_elementary_level.ENTITY_noun import hac_EntityNoun
    from .HAC_dict.xi_ien.pre_elementary_level.ENTITY_pronoun import hac_EntityPronoun
    from .HAC_dict.xi_ien.pre_elementary_level.FUNC_conjunction import hac_FuncConjunction
    from .HAC_dict.xi_ien.pre_elementary_level.FUNC_inner import hac_FuncInner
    from .HAC_dict.xi_ien.pre_elementary_level.FUNC_inter import hac_FuncInter
    from .HAC_dict.xi_ien.pre_elementary_level.IDIOM import hac_Idiom
    from .HAC_dict.xi_ien.pre_elementary_level.LOCATION import hac_Location
    from .HAC_dict.xi_ien.pre_elementary_level.MODIFIER import hac_Modifier
    from .HAC_dict.xi_ien.pre_elementary_level.RANGE_locality import hac_RangeLocality
    from .HAC_dict.xi_ien.pre_elementary_level.TIME_justtime import hac_TimeJusttime
    from .HAC_dict.xi_ien.pre_elementary_level.TIME_season import hac_TimeSeason

    from .IreneHAKKA_dict.ACTION_eventQuantifier import DT_ActionEventQuantifier
    from .IreneHAKKA_dict.ACTION_lightVerb import DT_ActionLightVerb
    from .IreneHAKKA_dict.ACTION_quantifiedVerb import DT_ActionQuantifiedVerb
    from .IreneHAKKA_dict.ACTION_verb import DT_ActionVerb
    from .IreneHAKKA_dict.ASPECT import DT_Aspect
    from .IreneHAKKA_dict.AUX import DT_Aux
    from .IreneHAKKA_dict.CLAUSE_particle import DT_ClauseParticle
    from .IreneHAKKA_dict.CLAUSE_Q import DT_ClauseQ
    from .IreneHAKKA_dict.ENTITY_classifier import DT_EntityClassifier
    from .IreneHAKKA_dict.ENTITY_DetPhrase import DT_EntityDetPhrase
    from .IreneHAKKA_dict.ENTITY_measurement import DT_EntityMeasurement
    from .IreneHAKKA_dict.ENTITY_noun import DT_EntityNoun
    from .IreneHAKKA_dict.ENTITY_num import DT_EntityNum
    from .IreneHAKKA_dict.ENTITY_person import DT_EntityPerson
    from .IreneHAKKA_dict.ENTITY_possessive import DT_EntityPossessive
    from .IreneHAKKA_dict.ENTITY_pronoun import DT_EntityPronoun
    from .IreneHAKKA_dict.FUNC_degreeHead import DT_FuncDegreeHead
    from .IreneHAKKA_dict.FUNC_inner import DT_FuncInner
    from .IreneHAKKA_dict.FUNC_inter import DT_FuncInter
    from .IreneHAKKA_dict.FUNC_negation import DT_FuncNegation
    from .IreneHAKKA_dict.FUNC_conjunction import DT_FuncConjunction
    from .IreneHAKKA_dict.IDIOM import DT_Idiom
    from .IreneHAKKA_dict.LOCATION import DT_Location
    from .IreneHAKKA_dict.TIME_justtime import DT_TimeJusttime
    from .IreneHAKKA_dict.MODAL import DT_Modal
    from .IreneHAKKA_dict.MODIFIER import DT_Modifier
    from .IreneHAKKA_dict.MODIFIER_color import DT_ModifierColor
    from .IreneHAKKA_dict.QUANTIFIER import DT_Quantifier
    from .IreneHAKKA_dict.RANGE_period import DT_RangePeriod
    from .IreneHAKKA_dict.RANGE_locality import DT_RangeLocality


def dictCombiner():
    '''
    Combine moe dictionary and DroidtownTG_dict
    '''
    combinedDICT = {"ACTION_verb"           : None,
                    "ACTION_lightVerb"      : None,
                    "ACTION_quantifiedVerb" : None,
                    "ACTION_eventQuantifier": None,
                    "ASPECT"                : None,
                    "AUX"                   : None,
                    "CLAUSE_particle"       : None,
                    "CLAUSE_Q"              : None,
                    "ENTITY_classifier"     : None,
                    "ENTITY_DetPhrase"      : None,
                    "ENTITY_measurement"    : None,
                    "ENTITY_noun"           : None,
                    "ENTITY_num"            : None,
                    "ENTITY_person"         : None,
                    "ENTITY_possessive"     : None,
                    "ENTITY_pronoun"        : None,
                    "FUNC_conjunction"      : None,
                    "FUNC_degreeHead"       : None,
                    "FUNC_inner"            : None,
                    "FUNC_inter"            : None,
                    "FUNC_negation"         : None,
                    "FUNC_conjunction"      : None,
                    "IDIOM"                 : None,
                    "LOCATION"              : None,
                    "MODAL"                 : None,
                    "MODIFIER"              : None,
                    "MODIFIER_color"        : None,
                    "QUANTIFIER"            : None,
                    "RANGE_locality"        : None,
                    "RANGE_period"          : None,
                    "TIME_justtime"         : None,
                    "TIME_season"           : None
                    }

    hacDICT = {"ACTION_verb"      : hac_ActionVerb,
               "CLAUSE_particle"  : hac_ClauseParticle,
               "CLAUSE_Q"         : hac_ClauseQ,
               "ENTITY_classifier": hac_EntityClassifier,
               "ENTITY_noun"      : hac_EntityNoun,
               "ENTITY_pronoun"   : hac_EntityPronoun,
               "FUNC_conjunction" : hac_FuncConjunction,
               "FUNC_inner"       : hac_FuncInner,
               "FUNC_inter"       : hac_FuncInter,
               "IDIOM"            : hac_Idiom,
               "LOCATION"         : hac_Location,
               "MODIFIER"         : hac_Modifier,
               "RANGE_locality"   : hac_RangeLocality,
               "TIME_justtime"    : hac_TimeJusttime,
               "TIME_season"      : hac_TimeSeason
    }

    DTDICT = {"ACTION_verb"           : DT_ActionVerb,
              "ACTION_lightVerb"      : DT_ActionLightVerb,
              "ACTION_quantifiedVerb" : DT_ActionQuantifiedVerb,
              "ACTION_eventQuantifier": DT_ActionEventQuantifier,
              "ASPECT"                : DT_Aspect,
              "AUX"                   : DT_Aux,
              "CLAUSE_particle"       : DT_ClauseParticle,
              "CLAUSE_Q"              : DT_ClauseQ,
              "ENTITY_classifier"     : DT_EntityClassifier,
              "ENTITY_DetPhrase"      : DT_EntityDetPhrase,
              "ENTITY_measurement"    : DT_EntityMeasurement,
              "ENTITY_noun"           : DT_EntityNoun,
              "ENTITY_num"            : DT_EntityNum,
              "ENTITY_person"         : DT_EntityPerson,
              "ENTITY_possessive"     : DT_EntityPossessive,
              "ENTITY_pronoun"        : DT_EntityPronoun,
              "FUNC_degreeHead"       : DT_FuncDegreeHead,
              "FUNC_inner"            : DT_FuncInner,
              "FUNC_inter"            : DT_FuncInter,
              "FUNC_negation"         : DT_FuncNegation,
              "FUNC_conjunction"      : DT_FuncConjunction,
              "IDIOM"                 : DT_Idiom,
              "LOCATION"              : DT_Location,
              "TIME_justtime"         : DT_TimeJusttime,
              "MODAL"                 : DT_Modal,
              "MODIFIER"              : DT_Modifier,
              "MODIFIER_color"        : DT_ModifierColor,
              "QUANTIFIER"            : DT_Quantifier,
              "RANGE_period"          : DT_RangePeriod,
              "RANGE_locality"        : DT_RangeLocality
    }


    for POS in combinedDICT.keys():
        try:
            tmpLIST = hacDICT[POS]
            for k in DTDICT.keys():
                tmpLIST = list(set(tmpLIST)-set(DTDICT[k]))
            if POS in DTDICT.keys():
                tmpLIST.extend(DTDICT[POS])
            tmpLIST = list(set(tmpLIST))
            combinedDICT[POS] = tmpLIST
        except KeyError:
            combinedDICT[POS] = DTDICT[POS]

        #try:
            #tmpLIST = []
            #for p in posLIST:
                #if re.search(self.cjkPAT, p.strip()):
                    #tmpLIST.append(p.strip())
                #else:
                    #for w in (p.strip().lower(), p.strip().upper(), p.strip().title(), p.strip().capitalize(), p.strip()):
                        #tmpLIST.append(" {}".format(w))
                        #tmpLIST.append("{} ".format(w))
                        #tmpLIST.append(" {} ".format(w))
                        #tmpLIST.append("{}".format(w))
            #if tmpLIST != []:
                #combinedDICT[POS].extend(tmpLIST)
            #combinedDICT[POS] = list(set(combinedDICT[POS]))
        #except FileNotFoundError:
            #pass

    #if platform.system() == "Windows":
        #defaultDictFILE = tempfile.NamedTemporaryFile(mode="w+", delete=False)
    #else:
        #defaultDictFILE = tempfile.NamedTemporaryFile(mode="w+")
    #json.dump(combinedDICT, defaultDictFILE)
    #defaultDictFILE.flush()


    return combinedDICT


if __name__ == "__main__":
    combinedDICT = dictCombiner()
    print(combinedDICT["TIME_justtime"])