import streamlit as st


st.set_page_config(
    page_title="VB Calc - Referências",
    page_icon=":book:"
)


logo_ext_color = "imagens/logo_extended_color.png"
logo_ext_bw = "imagens/logo_extended_bw.png"
logo_only_color = "imagens/logo_only_color.png"
logo_only_bw = "imagens/logo_only_bw.png"
logo_vbcalc = "imagens/VBCalc_logo.png"
logo_vbcalc2 = "imagens/VBCalc_logo_ext.png"

# st.sidebar.image(logo_vbcalc, use_column_width=True)
st.sidebar.image(logo_vbcalc2, use_column_width=True)

st.sidebar.link_button("Apoie o VB Calc.", "https://biolivre.com.br/vbcardiologia", type="primary", use_container_width=True)
with st.sidebar:
    st.page_link("main.py", label="Home")
    st.page_link("pages/sedacao.py", label="Analgesia e Sedação")
    st.page_link("pages/bloqueadores.py", label="Bloq. Neuromuscular")
    st.page_link("pages/dva.py", label="Drogas Vasoativas")
    st.page_link("pages/nitratos.py", label="Nitratos")
    st.page_link("pages/ref.py", label="Referências")
    st.page_link("pages/tutorial.py", label="Tutorial")
    st.page_link("pages/termos.py", label="Termos de Uso")
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **[Dr. Vinícius Beleze](https://instagram.com/drviníciusbeleze)**")



"""
# Referências

19 de agosto de 2024 

---

# Analgesia e Sedação:

## Cetamina:

1. Buchheit JL, Yeh DD, Eikermann M, Lin H. Impact of low-dose ketamine on the usage of continuous opioid infusion for the treatment of pain in adult mechanically ventilated patients in surgical intensive care units. J Intensive Care Med. 2019;34(8):646-651. doi:10.1177/0885066617706907 [PubMed 28468568]
2. Garber PM, Droege CA, Carter KE, Harger NJ, Mueller EW. Continuous infusion ketamine for adjunctive analgosedation in mechanically ventilated, critically ill patients. Pharmacotherapy. 2019;39(3):288-296. doi:10.1002/phar.2223 [PubMed 30746728]
3. Groetzinger LM, Rivosecchi RM, Bain W, et al. Ketamine infusion for adjunct sedation in mechanically ventilated adults. Pharmacotherapy. 2018;38(2):181-188. doi:10.1002/phar.2065 [PubMed 29193185]
4. Barr J, Fraser GL, Puntillo K, et al. Clinical practice guidelines for the management of pain, agitation, and delirium in adult patients in the intensive care unit. Crit Care Med. 2013;41(1):263-306. doi:10.1097/CCM.0b013e3182783b72 [PubMed 23269131]
5. Devlin JW, Skrobik Y, Gélinas C, et al; Society of Critical Care Medicine. Clinical practice guidelines for the prevention and management of pain, agitation/sedation, delirium, immobility, and sleep disruption in adult patients in the ICU. Crit Care Med. 2018;46(9):e825-e873. doi:10.1097/CCM.0000000000003299 [PubMed 30113379]

## Dexmedetomidina:

1. Gerlach AT, Dasta JF, Steinberg S, Martin LC, Cook CH. A new dosing protocol reduces dexmedetomidine-associated hypotension in critically ill surgical patients. *J Crit Care*. 2009;24(4):568-574. doi:10.1016/j.jcrc.2009.05.015 [PubMed [19682844](https://www.uptodate.com/contents/dexmedetomidine-drug-information/abstract-text/19682844/pubmed)]
2. Hughes CG, Mailloux PT, Devlin JW, et al; MENDS2 Study Investigators. Dexmedetomidine or propofol for sedation in mechanically ventilated adults with sepsis. *N Engl J Med.* 2021;384(15):1424-1436. doi:10.1056/NEJMoa2024922 [PubMed [33528922](https://www.uptodate.com/contents/dexmedetomidine-drug-information/abstract-text/33528922/pubmed)]
3. Jakob SM, Ruokonen E, Grounds RM, et al; Dexmedetomidine for Long-Term Sedation Investigators. Dexmedetomidine vs midazolam or propofol for sedation during prolonged mechanical ventilation: two randomized controlled trials. *JAMA*. 2012;307(11):1151-1160. doi:10.1001/jama.2012.304 [PubMed [22436955](https://www.uptodate.com/contents/dexmedetomidine-drug-information/abstract-text/22436955/pubmed)]
4. Riker RR, Shehabi Y, Bokesch PM, et al; SEDCOM (Safety and Efficacy of Dexmedetomidine Compared With Midazolam) Study Group. Dexmedetomidine vs midazolam for sedation of critically ill patients: a randomized trial. *JAMA*. 2009;301(5):489-99. doi:10.1001/jama.2009.56 [PubMed [19188334](https://www.uptodate.com/contents/dexmedetomidine-drug-information/abstract-text/19188334/pubmed)]
5. Shehabi Y, Ruettimann U, Adamson H, Innes R, Ickeringill M. Dexmedetomidine infusion for more than 24 hours in critically ill patients: sedative and cardiovascular effects. *Intensive Care Med*. 2004;30(12):2188-2196. doi:10.1007/s00134-004-2417-z [PubMed [15338124](https://www.uptodate.com/contents/dexmedetomidine-drug-information/abstract-text/15338124/pubmed)]
6. Shehabi Y, Howe BD, Bellomo R, et al; ANZICS Clinical Trials Group and the SPICE III Investigators. Early sedation with dexmedetomidine in critically ill patients. *N Engl J Med*. 2019;380(26):2506-2517. doi:10.1056/NEJMoa1904710 [PubMed [31112380](https://www.uptodate.com/contents/dexmedetomidine-drug-information/abstract-text/31112380/pubmed)]

## Esmolol:

1. Whelton PK, Carey RM, Aronow WS, et al. 2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA guideline for the prevention, detection, evaluation, and management of high blood pressure in adults: a report of the American College of Cardiology/American Heart Association Task Force on clinical practice guidelines. Hypertension. 2018;71(6):e13-e115. doi:10.1161/HYP.0000000000000065 [PubMed 29133356]
2. Marik PE, Varon J. Hypertensive crises: challenges and management. Chest. 2007;131(6):1949-1962. doi:10.1378/chest.06-2490 [PubMed 17565029]
3. Marik PE, Rivera R. Hypertensive emergencies: an update. Curr Opin Crit Care. 2011;17(6):569-580. doi:10.1097/MCC.0b013e32834cd31d [PubMed 21986463]
4. Peixoto AJ. Acute severe hypertension. N Engl J Med. 2019;381(19):1843-1852. doi:10.1056/NEJMcp1901117 [PubMed 31693807]
5. Varon J. Treatment of acute severe hypertension: current and newer agents. Drugs. 2008;68(3):283-297. doi:10.2165/00003495-200868030-00003 [PubMed 18257607]

## Fentanil:

1. Pandharipande P, McGrane S. Pain control in the critically ill adult patient. Post TW, ed. UpToDate. Waltham, MA: UpToDate Inc. [http://www.uptodate.com](http://www.uptodate.com/). Accessed February 13, 2023.
2. Barr J, Fraser GL, Puntillo K, et al; American College of Critical Care Medicine. Clinical practice guidelines for the management of pain, agitation, and delirium in adult patients in the intensive care unit. *Crit Care Med*. 2013;41(1):263-306. doi:10.1097/CCM.0b013e3182783b72 [PubMed [23269131](https://www.uptodate.com/contents/fentanyl-drug-information/abstract-text/23269131/pubmed)]

## Midazolam:

1. Kress JP, Pohlman AS, O'Connor MF, Hall JB. Daily interruption of sedative infusions in critically ill patients undergoing mechanical ventilation. *N Engl J Med*. 2000;342(20):1471-1477. doi:10.1056/NEJM200005183422002 [PubMed [10816184](https://www.uptodate.com/contents/midazolam-drug-information/abstract-text/10816184/pubmed)]
2. Barr J, Fraser GL, Puntillo K, et al. Clinical practice guidelines for the management of pain, agitation, and delirium in adult patients in the intensive care unit. *Crit Care Med.* 2013;41(1):263-306. doi:10.1097/CCM.0b013e3182783b72 [PubMed [23269131](https://www.uptodate.com/contents/midazolam-drug-information/abstract-text/23269131/pubmed)]
3. Tietze KJ, Fuchs B. Sedative-analgesic medications in critically ill adults: Properties, dose regimens, and adverse effects. Post TW, ed. UpToDate. Waltham, MA: UpToDate Inc. [http://www.uptodate.com](http://www.uptodate.com/). Accessed January 24, 2020.

## Propofol:

1. Jakob SM, Ruokonen E, Grounds RM, et al; Dexmedetomidine for Long-Term Sedation Investigators. Dexmedetomidine vs midazolam or propofol for sedation during prolonged mechanical ventilation: two randomized controlled trials. *JAMA*. 2012;307(11):1151-1160. doi:10.1001/jama.2012.304 [PubMed [22436955](https://www.uptodate.com/contents/propofol-drug-information/abstract-text/22436955/pubmed)]
2. Kress JP, Pohlman AS, O'Connor MF, Hall JB. Daily interruption of sedative infusions in critically ill patients undergoing mechanical ventilation. *N Engl J Med*, 2000;342(20):1471-1477. doi:10.1056/NEJM200005183422002 [PubMed [10816184](https://www.uptodate.com/contents/propofol-drug-information/abstract-text/10816184/pubmed)]
3. Roberts RJ, Barletta JF, Fong JJ, et al. Incidence of propofol-related infusion syndrome in critically ill adults: a prospective, multicenter study. *Crit Care*. 2009;13(5):R169. doi:10.1186/cc8145 [PubMed [19874582](https://www.uptodate.com/contents/propofol-drug-information/abstract-text/19874582/pubmed)]
4. Barr J, Fraser GL, Puntillo K, et al; American College of Critical Care Medicine. Clinical practice guidelines for the management of pain, agitation, and delirium in adult patients in the intensive care unit. *Crit Care Med*. 2013;41(1):263-306. doi:10.1097/CCM.0b013e3182783b72 [PubMed [23269131](https://www.uptodate.com/contents/propofol-drug-information/abstract-text/23269131/pubmed)]
5. Devlin JW, Skrobik Y, Gélinas C, et al. Clinical practice guidelines for the prevention and management of pain, agitation/sedation, delirium, immobility, and sleep disruption in adult patients in the ICU. *Crit Care Med*. 2018;46(9):e825-e873. doi: 10.1097/CCM.0000000000003299 [PubMed [30113379](https://www.uptodate.com/contents/propofol-drug-information/abstract-text/30113379/pubmed)]

# Bloqueadores Neuromusculares:

## Rocurônio:

1. Aldhaeefi M, Dube KM, Kovacevic MP, Szumita PM, Lupi KE, DeGrado JR. Evaluation of rocuronium continuous infusion in critically ill patients during the COVID-19 pandemic and drug shortages. J Pharm Pract. 2021:8971900211033138. doi:10.1177/08971900211033138 [PubMed 34281428]
2. Alhazzani W, Belley-Cote E, Møller MH, et al. Neuromuscular blockade in patients with ARDS: a rapid practice guideline. Intensive Care Med. 2020;46(11):1977-1986. doi:10.1007/s00134-020-06227-8 [PubMed 33104824]
3. Murray MJ, Cowen J, DeBlock H, et al; Task Force of the American College of Critical Care Medicine (ACCM) of the Society of Critical Care Medicine (SCCM), American Society of Health-System Pharmacists, American College of Chest Physicians. Clinical practice guidelines for sustained neuromuscular blockade in the adult critically ill patient. Crit Care Med. 2002;30(1):142-156. doi:10.1097/00003246-200201000-00021 [PubMed 11902255]

# Drogas Vasoativas:

## Dobutamina:

1. Peberdy MA, Callaway CW, Neumar RW, et al; American Heart Association. Part 9: post-cardiac arrest care: 2010 American Heart Association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care. *Circulation*. 2010;122(18)(suppl 3):S768-S786. doi:10.1161/CIRCULATIONAHA.110.971002 [PubMed [20956225](https://www.uptodate.com/contents/dobutamine-drug-information/abstract-text/20956225/pubmed)]
2. Annane D, Vignon P, Renault A, et al; CATS Study Group. Norepinephrine plus dobutamine versus epinephrine alone for management of septic shock: a randomised trial. *Lancet*. 2007;370(9588):676-684. doi:10.1016/S0140-6736(07)61344-0 [PubMed [17720019](https://www.uptodate.com/contents/dobutamine-drug-information/abstract-text/17720019/pubmed)]
3. Manaker S. Use of vasopressors and inotropes. Post TW, ed. UpToDate. Waltham, MA: UpToDate Inc. [http://www.uptodate.com](http://www.uptodate.com/). Accessed October 7, 2021.
4. Mouncey PR, Osborn TM, Power GS, et al. Protocolised Management In Sepsis (ProMISe): a multicentre randomised controlled trial of the clinical effectiveness and cost-effectiveness of early, goal-directed, protocolised resuscitation for emerging septic shock. *Health Technol Assess*. 2015;19(97):i-xxv,1-150. doi:10.3310/hta19970 [PubMed [26597979](https://www.uptodate.com/contents/dobutamine-drug-information/abstract-text/26597979/pubmed)]
5. Dellinger RP, Levy MM, Rhodes A, et al. Surviving Sepsis Campaign: international guidelines for management of severe sepsis and septic shock: 2012. *Crit Care Med*. 2013;41(2):580-637. doi:10.1097/CCM.0b013e31827e83af [PubMed [23353941](https://www.uptodate.com/contents/dobutamine-drug-information/abstract-text/23353941/pubmed)]

## Dopamina:

1. van Diepen S, Katz JN, Albert NM, et al; American Heart Association Council on Clinical Cardiology; Council on Cardiovascular and Stroke Nursing; Council on Quality of Care and Outcomes Research; Mission: Lifeline. Contemporary management of cardiogenic shock: a scientific statement from the American Heart Association. *Circulation*. 2017;136(16):e232-e268. doi:10.1161/CIR.0000000000000525 [PubMed [28923988](https://www.uptodate.com/contents/dopamine-drug-information/abstract-text/28923988/pubmed)]

## Noradrenalina:

1. De Backer D, Biston P, Devriendt J, et al. Comparison of dopamine and norepinephrine in the treatment of shock. *N Engl J Med*. 2010;362(9):779-789. doi:10.1056/NEJMoa0907118 [PubMed [20200382](https://www.uptodate.com/contents/norepinephrine-noradrenaline-drug-information/abstract-text/20200382/pubmed)]
2. Hollenberg SM, Ahrens TS, Annane D, et al. Practice parameters for hemodynamic support of sepsis in adult patients: 2004 update. *Crit Care Med.* 2004;32(9):1928-1948. doi:10.1097/01.ccm.0000139761.05492.d6 [PubMed [15343024](https://www.uptodate.com/contents/norepinephrine-noradrenaline-drug-information/abstract-text/15343024/pubmed)]
3. Hollenberg SM. Vasoactive drugs in circulatory shock. *Am J Respir Crit Care Med*. 2011;183(7):847-855. doi:10.1164/rccm.201006-0972CI [PubMed [21097695](https://www.uptodate.com/contents/norepinephrine-noradrenaline-drug-information/abstract-text/21097695/pubmed)]
4. Manaker S. Use of vasopressors and inotropes. Post TW, ed. UpToDate. Waltham, MA: UpToDate Inc. [http://www.uptodate.com](http://www.uptodate.com/). Accessed October 29, 2020.
5. Martin C, Saux P, Eon B, Aknin P, Gouin F. Septic shock: a goal-directed therapy using volume loading, dobutamine and/or norepinephrine. *Acta Anaesthesiol Scand*. 1990;34(5):413-417. doi:10.1111/j.1399-6576.1990.tb03114.x [PubMed [2389659](https://www.uptodate.com/contents/norepinephrine-noradrenaline-drug-information/abstract-text/2389659/pubmed)]
6. Russell JA, Walley KR, Singer J, et al; VASST Investigators. Vasopressin versus norepinephrine infusion in patients with septic shock. *N Engl J Med*. 2008;358(9):877-887. doi:10.1056/NEJMoa067373 [PubMed [18305265](https://www.uptodate.com/contents/norepinephrine-noradrenaline-drug-information/abstract-text/18305265/pubmed)]

# Nitratos:

## Nitroglicerina:

1. Whelton PK, Carey RM, Aronow WS, et al. 2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA guideline for the prevention, detection, evaluation, and management of high blood pressure in adults: executive summary: a report of the American College of Cardiology/American Heart Association Task Force on Clinical Practice Guidelines. Hypertension. 2018;71(6):1269-1324. doi:10.1161/HYP.0000000000000066 [PubMed 29133354]
2. Elliott WJ, Varon J. Drugs used for the treatment of hypertensive emergencies. Post TW, ed. UpToDate. Waltham, MA: UpToDate Inc. [http://www.uptodate.com](http://www.uptodate.com/). Accessed January 24, 2022b.
3. Marik PE, Rivera R. Hypertensive emergencies: an update. Curr Opin Crit Care. 2011;17(6):569-580. doi:10.1097/MCC.0b013e32834cd31d [PubMed 21986463]

## Nitroprussiato de Sódio:

1. Whelton PK, Carey RM, Aronow WS, et al. 2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA guideline for the prevention, detection, evaluation, and management of high blood pressure in adults: a report of the American College of Cardiology/American Heart Association Task Force on clinical practice guidelines. Hypertension. 2018;71(6):e13-e115. doi:10.1161/HYP.0000000000000065 [PubMed 29133356]
2. Elliot WJ, Varon J. Drugs used for the treatment of hypertensive emergencies. Post TW, ed. UpToDate. Waltham, MA: UpToDate Inc. [http://www.uptodate.com](http://www.uptodate.com/). Accessed February 23, 2022b.
3. Marik PE, Varon J. Hypertensive crises: challenges and management. Chest. 2007;131(6):1949-1962. doi:10.1378/chest.06-2490 [PubMed 17565029]
4. Peixoto AJ. Acute severe hypertension. N Engl J Med. 2019;381(19):1843-1852. doi:10.1056/NEJMcp1901117 [PubMed 31693807]
"""


