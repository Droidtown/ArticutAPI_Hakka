#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tempfile
import platform

try:
    from HAC_dict.xi_ien.pre_elementary_level.ACTION_verb import hac_ActionVerb as pre_elementary_hac_ActionVerb
    from HAC_dict.xi_ien.pre_elementary_level.CLAUSE_particle import hac_ClauseParticle as pre_elementary_hac_ClauseParticle
    from HAC_dict.xi_ien.pre_elementary_level.CLAUSE_Q import hac_ClauseQ as pre_elementary_hac_ClauseQ
    from HAC_dict.xi_ien.pre_elementary_level.ENTITY_classifier import hac_EntityClassifier as pre_elementary_hac_EntityClassifier
    from HAC_dict.xi_ien.pre_elementary_level.ENTITY_noun import hac_EntityNoun as pre_elementary_hac_EntityNoun
    from HAC_dict.xi_ien.pre_elementary_level.ENTITY_pronoun import hac_EntityPronoun as pre_elementary_hac_EntityPronoun
    from HAC_dict.xi_ien.pre_elementary_level.FUNC_conjunction import hac_FuncConjunction as pre_elementary_hac_FuncConjunction
    from HAC_dict.xi_ien.pre_elementary_level.FUNC_inner import hac_FuncInner as pre_elementary_hac_FuncInner
    from HAC_dict.xi_ien.pre_elementary_level.FUNC_inter import hac_FuncInter as pre_elementary_hac_FuncInter
    from HAC_dict.xi_ien.pre_elementary_level.FUNC_negation import hac_FuncNegation as pre_elementary_hac_FuncNegation 
    from HAC_dict.xi_ien.pre_elementary_level.IDIOM import hac_Idiom as pre_elementary_hac_Idiom
    from HAC_dict.xi_ien.pre_elementary_level.LOCATION import hac_Location as pre_elementary_hac_Location
    from HAC_dict.xi_ien.pre_elementary_level.MODIFIER import hac_Modifier as pre_elementary_hac_Modifier
    from HAC_dict.xi_ien.pre_elementary_level.RANGE_locality import hac_RangeLocality as pre_elementary_hac_RangeLocality
    from HAC_dict.xi_ien.pre_elementary_level.TIME_justtime import hac_TimeJusttime as pre_elementary_hac_TimeJusttime
    from HAC_dict.xi_ien.pre_elementary_level.TIME_season import hac_TimeSeason as pre_elementary_hac_TimeSeason

    from HAC_dict.xi_ien.elementary_level.ACTION_verb import hac_ActionVerb as elementary_hac_ActionVerb
    from HAC_dict.xi_ien.elementary_level.CLAUSE_particle import hac_ClauseParticle as elementary_hac_ClauseParticle
    from HAC_dict.xi_ien.elementary_level.CLAUSE_Q import hac_ClauseQ as elementary_hac_ClauseQ
    from HAC_dict.xi_ien.elementary_level.ENTITY_classifier import hac_EntityClassifier as elementary_hac_EntityClassifier
    from HAC_dict.xi_ien.elementary_level.ENTITY_noun import hac_EntityNoun as elementary_hac_EntityNoun
    from HAC_dict.xi_ien.elementary_level.ENTITY_pronoun import hac_EntityPronoun as elementary_hac_EntityPronoun
    from HAC_dict.xi_ien.elementary_level.FUNC_conjunction import hac_FuncConjunction as elementary_hac_FuncConjunction
    from HAC_dict.xi_ien.elementary_level.FUNC_inner import hac_FuncInner as elementary_hac_FuncInner
    from HAC_dict.xi_ien.elementary_level.FUNC_inter import hac_FuncInter as elementary_hac_FuncInter
    from HAC_dict.xi_ien.elementary_level.FUNC_negation import hac_FuncNegation as elementary_hac_FuncNegation 
    from HAC_dict.xi_ien.elementary_level.IDIOM import hac_Idiom as elementary_hac_Idiom
    from HAC_dict.xi_ien.elementary_level.LOCATION import hac_Location as elementary_hac_Location
    from HAC_dict.xi_ien.elementary_level.MODIFIER import hac_Modifier as elementary_hac_Modifier
    from HAC_dict.xi_ien.elementary_level.RANGE_locality import hac_RangeLocality as elementary_hac_RangeLocality
    from HAC_dict.xi_ien.elementary_level.TIME_justtime import hac_TimeJusttime as elementary_hac_TimeJusttime
    from HAC_dict.xi_ien.elementary_level.TIME_season import hac_TimeSeason as elementary_hac_TimeSeason

    from HAC_dict.xi_ien.intermediate_level.ACTION_verb import hac_ActionVerb as intermediate_hac_ActionVerb
    from HAC_dict.xi_ien.intermediate_level.CLAUSE_particle import hac_ClauseParticle as intermediate_hac_ClauseParticle
    from HAC_dict.xi_ien.intermediate_level.CLAUSE_Q import hac_ClauseQ as intermediate_hac_ClauseQ
    from HAC_dict.xi_ien.intermediate_level.ENTITY_classifier import hac_EntityClassifier as intermediate_hac_EntityClassifier
    from HAC_dict.xi_ien.intermediate_level.ENTITY_noun import hac_EntityNoun as intermediate_hac_EntityNoun
    from HAC_dict.xi_ien.intermediate_level.ENTITY_pronoun import hac_EntityPronoun as intermediate_hac_EntityPronoun
    from HAC_dict.xi_ien.intermediate_level.FUNC_conjunction import hac_FuncConjunction as intermediate_hac_FuncConjunction
    from HAC_dict.xi_ien.intermediate_level.FUNC_inner import hac_FuncInner as intermediate_hac_FuncInner
    from HAC_dict.xi_ien.intermediate_level.FUNC_inter import hac_FuncInter as intermediate_hac_FuncInter
    from HAC_dict.xi_ien.intermediate_level.FUNC_negation import hac_FuncNegation as intermediate_hac_FuncNegation 
    from HAC_dict.xi_ien.intermediate_level.IDIOM import hac_Idiom as intermediate_hac_Idiom
    from HAC_dict.xi_ien.intermediate_level.LOCATION import hac_Location as intermediate_hac_Location
    from HAC_dict.xi_ien.intermediate_level.MODIFIER import hac_Modifier as intermediate_hac_Modifier
    from HAC_dict.xi_ien.intermediate_level.RANGE_locality import hac_RangeLocality as intermediate_hac_RangeLocality
    from HAC_dict.xi_ien.intermediate_level.TIME_justtime import hac_TimeJusttime as intermediate_hac_TimeJusttime
    from HAC_dict.xi_ien.intermediate_level.TIME_season import hac_TimeSeason as intermediate_hac_TimeSeason

    from HAC_dict.xi_ien.highintermediate_level.ACTION_verb import hac_ActionVerb as highintermediate_hac_ActionVerb
    from HAC_dict.xi_ien.highintermediate_level.CLAUSE_particle import hac_ClauseParticle as highintermediate_hac_ClauseParticle
    from HAC_dict.xi_ien.highintermediate_level.CLAUSE_Q import hac_ClauseQ as highintermediate_hac_ClauseQ
    from HAC_dict.xi_ien.highintermediate_level.ENTITY_classifier import hac_EntityClassifier as highintermediate_hac_EntityClassifier
    from HAC_dict.xi_ien.highintermediate_level.ENTITY_noun import hac_EntityNoun as highintermediate_hac_EntityNoun
    from HAC_dict.xi_ien.highintermediate_level.ENTITY_pronoun import hac_EntityPronoun as highintermediate_hac_EntityPronoun
    from HAC_dict.xi_ien.highintermediate_level.FUNC_conjunction import hac_FuncConjunction as highintermediate_hac_FuncConjunction
    from HAC_dict.xi_ien.highintermediate_level.FUNC_inner import hac_FuncInner as highintermediate_hac_FuncInner
    from HAC_dict.xi_ien.highintermediate_level.FUNC_inter import hac_FuncInter as highintermediate_hac_FuncInter
    from HAC_dict.xi_ien.highintermediate_level.FUNC_negation import hac_FuncNegation as highintermediate_hac_FuncNegation 
    from HAC_dict.xi_ien.highintermediate_level.IDIOM import hac_Idiom as highintermediate_hac_Idiom
    from HAC_dict.xi_ien.highintermediate_level.LOCATION import hac_Location as highintermediate_hac_Location
    from HAC_dict.xi_ien.highintermediate_level.MODIFIER import hac_Modifier as highintermediate_hac_Modifier
    from HAC_dict.xi_ien.highintermediate_level.RANGE_locality import hac_RangeLocality as highintermediate_hac_RangeLocality
    from HAC_dict.xi_ien.highintermediate_level.TIME_justtime import hac_TimeJusttime as highintermediate_hac_TimeJusttime
    from HAC_dict.xi_ien.highintermediate_level.TIME_season import hac_TimeSeason as highintermediate_hac_TimeSeason

    from HAC_dict.xi_ien.advanced_level.ACTION_verb import hac_ActionVerb as advanced_hac_ActionVerb
    from HAC_dict.xi_ien.advanced_level.CLAUSE_particle import hac_ClauseParticle as advanced_hac_ClauseParticle
    from HAC_dict.xi_ien.advanced_level.CLAUSE_Q import hac_ClauseQ as advanced_hac_ClauseQ
    from HAC_dict.xi_ien.advanced_level.ENTITY_classifier import hac_EntityClassifier as advanced_hac_EntityClassifier
    from HAC_dict.xi_ien.advanced_level.ENTITY_noun import hac_EntityNoun as advanced_hac_EntityNoun
    from HAC_dict.xi_ien.advanced_level.ENTITY_pronoun import hac_EntityPronoun as advanced_hac_EntityPronoun
    from HAC_dict.xi_ien.advanced_level.FUNC_conjunction import hac_FuncConjunction as advanced_hac_FuncConjunction
    from HAC_dict.xi_ien.advanced_level.FUNC_inner import hac_FuncInner as advanced_hac_FuncInner
    from HAC_dict.xi_ien.advanced_level.FUNC_inter import hac_FuncInter as advanced_hac_FuncInter
    from HAC_dict.xi_ien.advanced_level.FUNC_negation import hac_FuncNegation as advanced_hac_FuncNegation 
    from HAC_dict.xi_ien.advanced_level.IDIOM import hac_Idiom as advanced_hac_Idiom
    from HAC_dict.xi_ien.advanced_level.LOCATION import hac_Location as advanced_hac_Location
    from HAC_dict.xi_ien.advanced_level.MODIFIER import hac_Modifier as advanced_hac_Modifier
    from HAC_dict.xi_ien.advanced_level.RANGE_locality import hac_RangeLocality as advanced_hac_RangeLocality
    from HAC_dict.xi_ien.advanced_level.TIME_justtime import hac_TimeJusttime as advanced_hac_TimeJusttime
    from HAC_dict.xi_ien.advanced_level.TIME_season import hac_TimeSeason as advanced_hac_TimeSeason

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
    from IreneHAKKA_dict.RANGE_locality import DT_RangeLocality

except:
    from .HAC_dict.xi_ien.pre_elementary_level.ACTION_verb import hac_ActionVerb as pre_elementary_hac_ActionVerb
    from .HAC_dict.xi_ien.pre_elementary_level.CLAUSE_particle import hac_ClauseParticle as pre_elementary_hac_ClauseParticle
    from .HAC_dict.xi_ien.pre_elementary_level.CLAUSE_Q import hac_ClauseQ as pre_elementary_hac_ClauseQ
    from .HAC_dict.xi_ien.pre_elementary_level.ENTITY_classifier import hac_EntityClassifier as pre_elementary_hac_EntityClassifier
    from .HAC_dict.xi_ien.pre_elementary_level.ENTITY_noun import hac_EntityNoun as pre_elementary_hac_EntityNoun
    from .HAC_dict.xi_ien.pre_elementary_level.ENTITY_pronoun import hac_EntityPronoun as pre_elementary_hac_EntityPronoun
    from .HAC_dict.xi_ien.pre_elementary_level.FUNC_conjunction import hac_FuncConjunction as pre_elementary_hac_FuncConjunction
    from .HAC_dict.xi_ien.pre_elementary_level.FUNC_inner import hac_FuncInner as pre_elementary_hac_FuncInner
    from .HAC_dict.xi_ien.pre_elementary_level.FUNC_inter import hac_FuncInter as pre_elementary_hac_FuncInter
    from .HAC_dict.xi_ien.pre_elementary_level.FUNC_negation import hac_FuncNegation as pre_elementary_hac_FuncNegation 
    from .HAC_dict.xi_ien.pre_elementary_level.IDIOM import hac_Idiom as pre_elementary_hac_Idiom
    from .HAC_dict.xi_ien.pre_elementary_level.LOCATION import hac_Location as pre_elementary_hac_Location
    from .HAC_dict.xi_ien.pre_elementary_level.MODIFIER import hac_Modifier as pre_elementary_hac_Modifier
    from .HAC_dict.xi_ien.pre_elementary_level.RANGE_locality import hac_RangeLocality as pre_elementary_hac_RangeLocality
    from .HAC_dict.xi_ien.pre_elementary_level.TIME_justtime import hac_TimeJusttime as pre_elementary_hac_TimeJusttime
    from .HAC_dict.xi_ien.pre_elementary_level.TIME_season import hac_TimeSeason as pre_elementary_hac_TimeSeason

    from .HAC_dict.xi_ien.elementary_level.ACTION_verb import hac_ActionVerb as elementary_hac_ActionVerb
    from .HAC_dict.xi_ien.elementary_level.CLAUSE_particle import hac_ClauseParticle as elementary_hac_ClauseParticle
    from .HAC_dict.xi_ien.elementary_level.CLAUSE_Q import hac_ClauseQ as elementary_hac_ClauseQ
    from .HAC_dict.xi_ien.elementary_level.ENTITY_classifier import hac_EntityClassifier as elementary_hac_EntityClassifier
    from .HAC_dict.xi_ien.elementary_level.ENTITY_noun import hac_EntityNoun as elementary_hac_EntityNoun
    from .HAC_dict.xi_ien.elementary_level.ENTITY_pronoun import hac_EntityPronoun as elementary_hac_EntityPronoun
    from .HAC_dict.xi_ien.elementary_level.FUNC_conjunction import hac_FuncConjunction as elementary_hac_FuncConjunction
    from .HAC_dict.xi_ien.elementary_level.FUNC_inner import hac_FuncInner as elementary_hac_FuncInner
    from .HAC_dict.xi_ien.elementary_level.FUNC_inter import hac_FuncInter as elementary_hac_FuncInter
    from .HAC_dict.xi_ien.elementary_level.FUNC_negation import hac_FuncNegation as elementary_hac_FuncNegation 
    from .HAC_dict.xi_ien.elementary_level.IDIOM import hac_Idiom as elementary_hac_Idiom
    from .HAC_dict.xi_ien.elementary_level.LOCATION import hac_Location as elementary_hac_Location
    from .HAC_dict.xi_ien.elementary_level.MODIFIER import hac_Modifier as elementary_hac_Modifier
    from .HAC_dict.xi_ien.elementary_level.RANGE_locality import hac_RangeLocality as elementary_hac_RangeLocality
    from .HAC_dict.xi_ien.elementary_level.TIME_justtime import hac_TimeJusttime as elementary_hac_TimeJusttime
    from .HAC_dict.xi_ien.elementary_level.TIME_season import hac_TimeSeason as elementary_hac_TimeSeason

    from .HAC_dict.xi_ien.intermediate_level.ACTION_verb import hac_ActionVerb as intermediate_hac_ActionVerb
    from .HAC_dict.xi_ien.intermediate_level.CLAUSE_particle import hac_ClauseParticle as intermediate_hac_ClauseParticle
    from .HAC_dict.xi_ien.intermediate_level.CLAUSE_Q import hac_ClauseQ as intermediate_hac_ClauseQ
    from .HAC_dict.xi_ien.intermediate_level.ENTITY_classifier import hac_EntityClassifier as intermediate_hac_EntityClassifier
    from .HAC_dict.xi_ien.intermediate_level.ENTITY_noun import hac_EntityNoun as intermediate_hac_EntityNoun
    from .HAC_dict.xi_ien.intermediate_level.ENTITY_pronoun import hac_EntityPronoun as intermediate_hac_EntityPronoun
    from .HAC_dict.xi_ien.intermediate_level.FUNC_conjunction import hac_FuncConjunction as intermediate_hac_FuncConjunction
    from .HAC_dict.xi_ien.intermediate_level.FUNC_inner import hac_FuncInner as intermediate_hac_FuncInner
    from .HAC_dict.xi_ien.intermediate_level.FUNC_inter import hac_FuncInter as intermediate_hac_FuncInter
    from .HAC_dict.xi_ien.intermediate_level.FUNC_negation import hac_FuncNegation as intermediate_hac_FuncNegation 
    from .HAC_dict.xi_ien.intermediate_level.IDIOM import hac_Idiom as intermediate_hac_Idiom
    from .HAC_dict.xi_ien.intermediate_level.LOCATION import hac_Location as intermediate_hac_Location
    from .HAC_dict.xi_ien.intermediate_level.MODIFIER import hac_Modifier as intermediate_hac_Modifier
    from .HAC_dict.xi_ien.intermediate_level.RANGE_locality import hac_RangeLocality as intermediate_hac_RangeLocality
    from .HAC_dict.xi_ien.intermediate_level.TIME_justtime import hac_TimeJusttime as intermediate_hac_TimeJusttime
    from .HAC_dict.xi_ien.intermediate_level.TIME_season import hac_TimeSeason as intermediate_hac_TimeSeason

    from .HAC_dict.xi_ien.highintermediate_level.ACTION_verb import hac_ActionVerb as highintermediate_hac_ActionVerb
    from .HAC_dict.xi_ien.highintermediate_level.CLAUSE_particle import hac_ClauseParticle as highintermediate_hac_ClauseParticle
    from .HAC_dict.xi_ien.highintermediate_level.CLAUSE_Q import hac_ClauseQ as highintermediate_hac_ClauseQ
    from .HAC_dict.xi_ien.highintermediate_level.ENTITY_classifier import hac_EntityClassifier as highintermediate_hac_EntityClassifier
    from .HAC_dict.xi_ien.highintermediate_level.ENTITY_noun import hac_EntityNoun as highintermediate_hac_EntityNoun
    from .HAC_dict.xi_ien.highintermediate_level.ENTITY_pronoun import hac_EntityPronoun as highintermediate_hac_EntityPronoun
    from .HAC_dict.xi_ien.highintermediate_level.FUNC_conjunction import hac_FuncConjunction as highintermediate_hac_FuncConjunction
    from .HAC_dict.xi_ien.highintermediate_level.FUNC_inner import hac_FuncInner as highintermediate_hac_FuncInner
    from .HAC_dict.xi_ien.highintermediate_level.FUNC_inter import hac_FuncInter as highintermediate_hac_FuncInter
    from .HAC_dict.xi_ien.highintermediate_level.FUNC_negation import hac_FuncNegation as highintermediate_hac_FuncNegation 
    from .HAC_dict.xi_ien.highintermediate_level.IDIOM import hac_Idiom as highintermediate_hac_Idiom
    from .HAC_dict.xi_ien.highintermediate_level.LOCATION import hac_Location as highintermediate_hac_Location
    from .HAC_dict.xi_ien.highintermediate_level.MODIFIER import hac_Modifier as highintermediate_hac_Modifier
    from .HAC_dict.xi_ien.highintermediate_level.RANGE_locality import hac_RangeLocality as highintermediate_hac_RangeLocality
    from .HAC_dict.xi_ien.highintermediate_level.TIME_justtime import hac_TimeJusttime as highintermediate_hac_TimeJusttime
    from .HAC_dict.xi_ien.highintermediate_level.TIME_season import hac_TimeSeason as highintermediate_hac_TimeSeason

    from .HAC_dict.xi_ien.advanced_level.ACTION_verb import hac_ActionVerb as advanced_hac_ActionVerb
    from .HAC_dict.xi_ien.advanced_level.CLAUSE_particle import hac_ClauseParticle as advanced_hac_ClauseParticle
    from .HAC_dict.xi_ien.advanced_level.CLAUSE_Q import hac_ClauseQ as advanced_hac_ClauseQ
    from .HAC_dict.xi_ien.advanced_level.ENTITY_classifier import hac_EntityClassifier as advanced_hac_EntityClassifier
    from .HAC_dict.xi_ien.advanced_level.ENTITY_noun import hac_EntityNoun as advanced_hac_EntityNoun
    from .HAC_dict.xi_ien.advanced_level.ENTITY_pronoun import hac_EntityPronoun as advanced_hac_EntityPronoun
    from .HAC_dict.xi_ien.advanced_level.FUNC_conjunction import hac_FuncConjunction as advanced_hac_FuncConjunction
    from .HAC_dict.xi_ien.advanced_level.FUNC_inner import hac_FuncInner as advanced_hac_FuncInner
    from .HAC_dict.xi_ien.advanced_level.FUNC_inter import hac_FuncInter as advanced_hac_FuncInter
    from .HAC_dict.xi_ien.advanced_level.FUNC_negation import hac_FuncNegation as advanced_hac_FuncNegation 
    from .HAC_dict.xi_ien.advanced_level.IDIOM import hac_Idiom as advanced_hac_Idiom
    from .HAC_dict.xi_ien.advanced_level.LOCATION import hac_Location as advanced_hac_Location
    from .HAC_dict.xi_ien.advanced_level.MODIFIER import hac_Modifier as advanced_hac_Modifier
    from .HAC_dict.xi_ien.advanced_level.RANGE_locality import hac_RangeLocality as advanced_hac_RangeLocality
    from .HAC_dict.xi_ien.advanced_level.TIME_justtime import hac_TimeJusttime as advanced_hac_TimeJusttime
    from .HAC_dict.xi_ien.advanced_level.TIME_season import hac_TimeSeason as advanced_hac_TimeSeason

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

    hacDICT = {"ACTION_verb"      : pre_elementary_hac_ActionVerb + elementary_hac_ActionVerb + intermediate_hac_ActionVerb + highintermediate_hac_ActionVerb + advanced_hac_ActionVerb,
               "CLAUSE_particle"  : pre_elementary_hac_ClauseParticle + elementary_hac_ClauseParticle + intermediate_hac_ClauseParticle + highintermediate_hac_ClauseParticle + advanced_hac_ClauseParticle,
               "CLAUSE_Q"         : pre_elementary_hac_ClauseQ + elementary_hac_ClauseQ + intermediate_hac_ClauseQ + highintermediate_hac_ClauseQ + advanced_hac_ClauseQ,
               "ENTITY_classifier": pre_elementary_hac_EntityClassifier + elementary_hac_EntityClassifier + intermediate_hac_EntityClassifier + highintermediate_hac_EntityClassifier + advanced_hac_EntityClassifier,
               "ENTITY_noun"      : pre_elementary_hac_EntityNoun + elementary_hac_EntityNoun + intermediate_hac_EntityNoun + highintermediate_hac_EntityNoun + advanced_hac_EntityNoun,
               "ENTITY_pronoun"   : pre_elementary_hac_EntityPronoun + elementary_hac_EntityPronoun + intermediate_hac_EntityPronoun + highintermediate_hac_EntityPronoun + advanced_hac_EntityPronoun,
               "FUNC_conjunction" : pre_elementary_hac_FuncConjunction + elementary_hac_FuncConjunction + intermediate_hac_FuncConjunction + highintermediate_hac_FuncConjunction + advanced_hac_FuncConjunction,
               "FUNC_inner"       : pre_elementary_hac_FuncInner + elementary_hac_FuncInner + intermediate_hac_FuncInner + highintermediate_hac_FuncInner + advanced_hac_FuncInner,
               "FUNC_inter"       : pre_elementary_hac_FuncInter + elementary_hac_FuncInter + intermediate_hac_FuncInter + highintermediate_hac_FuncInter + advanced_hac_FuncInter,
               "FUNC_negation"    : pre_elementary_hac_FuncNegation + elementary_hac_FuncNegation + intermediate_hac_FuncNegation + highintermediate_hac_FuncNegation + advanced_hac_FuncNegation,
               "IDIOM"            : pre_elementary_hac_Idiom + elementary_hac_Idiom + intermediate_hac_Idiom + highintermediate_hac_Idiom + advanced_hac_Idiom,
               "LOCATION"         : pre_elementary_hac_Location + elementary_hac_Location + intermediate_hac_Location + highintermediate_hac_Location + advanced_hac_Location,
               "MODIFIER"         : pre_elementary_hac_Modifier + elementary_hac_Modifier + intermediate_hac_Modifier + highintermediate_hac_Modifier + advanced_hac_Modifier,
               "RANGE_locality"   : pre_elementary_hac_RangeLocality + elementary_hac_RangeLocality + intermediate_hac_RangeLocality + highintermediate_hac_RangeLocality + advanced_hac_RangeLocality,
               "TIME_justtime"    : pre_elementary_hac_TimeJusttime + elementary_hac_TimeJusttime + intermediate_hac_TimeJusttime + highintermediate_hac_TimeJusttime + advanced_hac_TimeJusttime,
               "TIME_season"      : pre_elementary_hac_TimeSeason + elementary_hac_TimeSeason + intermediate_hac_TimeSeason + highintermediate_hac_TimeSeason + advanced_hac_TimeSeason
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