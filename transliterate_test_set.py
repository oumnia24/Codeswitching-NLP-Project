import requests
import torchmetrics
import csv

# transliterated = requests.get('https://transliterate.qcri.org/en2ar/nbest/Ahmed')

# print(transliterated.json()["results"]['0'][::1])

ref_to_hyp = {}
hyp = ""
ref = ""
with open('wp3/exp-20220509/E2E-conformer/ArzEn/sys.a/ArzEn_dev/score_cer/result.txt') as f:
    for line in f:
        if line[:3] == "REF":
            ref = line[4:].strip()
        if line[:3] == "HYP":
            hyp = line[4:].strip()
            ref_to_hyp[ref] = hyp

#Word and character error rates on original data:
char_error_rates = []
word_error_rates = []
char_metric = torchmetrics.CharErrorRate()
word_metric = torchmetrics.WordErrorRate()
i = 1

for ref, hyp in ref_to_hyp.items():
    ref = ref.lower().replace('<space>', ' ')
    hyp = hyp.lower().replace('<space>', ' ')
    char_error_rate = char_metric(hyp, ref)
    char_error_rates.append(char_error_rate)
    word_error_rate = word_metric(hyp, ref)
    word_error_rates.append(word_error_rate)
    i += 1
    if i == 5:
        break

print("Character error rates without transliteration:", char_error_rates)
print("Word error rates without transliteration:", word_error_rates)

#Get character error rates, arabic to english transliteration:
transliterated_hypotheses_ar2en = []
transliterated_references_ar2en = []
char_error_rates_ar2en = []
word_error_rates_ar2en = []
i = 1

transliterate_link_ar2en = 'https://transliterate.qcri.org/ar2en/'
for ref, hyp in ref_to_hyp.items():
    ref = ref.lower().replace('<space>', ' ')
    hyp = hyp.lower().replace('<space>', ' ')

    transliterate_ref_ar2en = requests.get(transliterate_link_ar2en + ref)
    transliterate_hyp_ar2en = requests.get(transliterate_link_ar2en + hyp)
    transliterate_ref_ar2en = '' + transliterate_ref_ar2en.json()['results'].lower()
    transliterate_hyp_ar2en = '' + transliterate_hyp_ar2en.json()['results'].lower()
    # print("Ref Arabic to english", transliterate_ref_ar2en)
    # print("Hyp Arabic to english", transliterate_hyp_ar2en)
    transliterated_hypotheses_ar2en.append(transliterate_hyp_ar2en)
    transliterated_references_ar2en.append(transliterate_ref_ar2en)
    char_error_rate = char_metric(transliterate_hyp_ar2en, transliterate_ref_ar2en)
    char_error_rates_ar2en.append(char_error_rate)
    word_error_rate = word_metric(transliterate_hyp_ar2en, transliterate_ref_ar2en)
    word_error_rates_ar2en.append(word_error_rate)
    i += 1
    if i == 5:
        break

print("Character error rates with Arabic to English transliteration:", char_error_rates_ar2en)
print("Word error rates with Arabic to English transliteration:", word_error_rates_ar2en)

#Get character error rates, english to arabic transliteration:
i = 1
transliterate_link_en2ar = 'https://transliterate.qcri.org/en2ar/'
transliterated_hypotheses_en2ar = []
transliterated_references_en2ar = []
char_error_rates_en2ar = []
word_error_rates_en2ar = []

for ref, hyp in ref_to_hyp.items():
    ref = ref.lower().replace('<space>', ' ')
    hyp = hyp.lower().replace('<space>', ' ')
    transliterate_ref_en2ar = requests.get(transliterate_link_en2ar + ref)
    transliterate_hyp_en2ar = requests.get(transliterate_link_en2ar + hyp)
    transliterate_ref_en2ar = '' + transliterate_ref_en2ar.json()['results'].lower()
    transliterate_hyp_en2ar = '' + transliterate_hyp_en2ar.json()['results'].lower()
    transliterated_hypotheses_en2ar.append(transliterate_hyp_en2ar)
    transliterated_references_en2ar.append(transliterate_ref_en2ar)
    char_error_rate = char_metric(transliterate_hyp_en2ar, transliterate_ref_en2ar)
    char_error_rates_en2ar.append(char_error_rate)
    word_error_rate = word_metric(transliterate_hyp_en2ar, transliterate_ref_en2ar)
    word_error_rates_en2ar.append(word_error_rate)
    i += 1
    if i == 5:
        break


print("Character error rates with English to Arabic transliteration:",char_error_rates_en2ar)
print("Word error rates with English to Arabic transliteration:", word_error_rates_en2ar)



#remove stars



