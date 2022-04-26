#!/usr/bin/python
import primer3
import sys
import pandas as pd

file1 = open(sys.argv[1],"r")
seq = ""
number = ""
dic_seq = {}
for line in file1:
    if line.startswith(">"):
        if line != "":
            dic_seq[number] = seq
        number = line
        seq = ""
    else:
        seq = seq + line.strip("\n")
dic_seq[number] = seq
globals_arg = {
    'PRIMER_PRODUCT_SIZE_RANGE': [400, 700],
    'PRIMER_FIRST_BASE_INDEX': 1,
    'PRIMER_TASK': 'generic',
    'PRIMER_NUM_RETURN': 5,
    'PRIMER_SECONDARY_STRUCTURE_ALIGNMENT': 1,
    'PRIMER_PICK_LEFT_PRIMER': 1,
    'PRIMER_PICK_INTERNAL_OLIGO': 0,
    'PRIMER_PICK_RIGHT_PRIMER': 1,
    'PRIMER_PICK_ANYWAY': 1,
    'PRIMER_TM_FORMULA': 1,
    'PRIMER_MIN_TM': 53.0,
    'PRIMER_OPT_TM': 60.0,
    'PRIMER_MAX_TM': 64.0,
    'PRIMER_PAIR_MAX_DIFF_TM': 5.0,
    'PRIMER_WT_TM_LT': 0,
    'PRIMER_WT_TM_GT': 0,
    'PRIMER_PAIR_WT_DIFF_TM': 0.0,

    'PRIMER_MIN_SIZE': 18,
    'PRIMER_OPT_SIZE': 21,
    'PRIMER_MAX_SIZE': 25,
    'PRIMER_WT_SIZE_LT': 0,
    'PRIMER_WT_SIZE_GT': 0,

    'PRIMER_MIN_GC': 40.0,
    'PRIMER_MAX_GC': 60.0,
    'PRIMER_WT_GC_PERCENT_LT': 0.0,
    'PRIMER_WT_GC_PERCENT_GT': 0.0,

    'PRIMER_THERMODYNAMIC_OLIGO_ALIGNMENT': 1,

    'PRIMER_MAX_SELF_ANY': 8.00,
    'PRIMER_WT_SELF_ANY': 0.0,
    'PRIMER_MAX_SELF_ANY_TH': 45.00,
    'PRIMER_WT_SELF_ANY_TH': 123.2,

    'PRIMER_MAX_SELF_END': 3.00,
    'PRIMER_WT_SELF_END': 0.0,
    'PRIMER_MAX_SELF_END_TH': 35.00,
    'PRIMER_WT_SELF_END_TH': 302.4,

    'PRIMER_PAIR_MAX_COMPL_ANY': 8.00,
    'PRIMER_PAIR_WT_COMPL_ANY': 0.0,
    'PRIMER_PAIR_MAX_COMPL_ANY_TH': 45.00,
    'PRIMER_PAIR_WT_COMPL_ANY_TH': 123.2,

    'PRIMER_PAIR_MAX_COMPL_END': 3.00,
    'PRIMER_PAIR_WT_COMPL_END': 0.0,
    'PRIMER_PAIR_MAX_COMPL_END_TH': 35.00,
    'PRIMER_PAIR_WT_COMPL_END_TH': 302.4,

    'PRIMER_MAX_HAIRPIN_TH': 24.00,
    'PRIMER_WT_HAIRPIN_TH': 672,

    'PRIMER_MAX_END_STABILITY': 9.0,
    'PRIMER_WT_END_STABILITY': 1,

    'PRIMER_LOWERCASE_MASKING': 0,
    'PRIMER_MAX_POLY_X': 4,
    'PRIMER_MAX_NS_ACCEPTED': 0,
    'PRIMER_WT_NUM_NS': 0.0,
    'PRIMER_MAX_END_GC': 5,
    'PRIMER_GC_CLAMP': 0,
    'PRIMER_LIBERAL_BASE': 1,
    'PRIMER_LIB_AMBIGUITY_CODES_CONSENSUS': 0,
}
primer_df = pd.DataFrame()

'''seq_arg = {
        'SEQUENCE_ID': 'MN175989',
        'SEQUENCE_TEMPLATE': seq,
        'SEQUENCE_INCLUDED_REGION': [i,100],
    }
primer3_result = primer3.bindings.designPrimers(seq_arg,globals_arg)
for key in primer3_result.keys():
    print((key)+":"+str(primer3_result[key]))'''
for key in dic_seq.keys():
    seq = dic_seq[key]
    print(key)
    if seq == "":
        continue
    else:
        seq_arg = {
            'SEQUENCE_ID': 'hm',
            'SEQUENCE_TEMPLATE': seq,
            'SEQUENCE_PRIMER_PAIR_OK_REGION_LIST': [0,250,450,249]
        }
        primer3_result = primer3.bindings.designPrimers(seq_arg,globals_arg)
        list1 = [primer3_result]
        data = pd.DataFrame(list1)
        data.insert(0,'POS',key.strip("\n"))
        primer_df = primer_df.append(data)
'''print(list(primer_df))
pd1 = primer_df[['PRIMER_LEFT_EXPLAIN','PRIMER_RIGHT_EXPLAIN','PRIMER_LEFT_0_PENALTY', 'PRIMER_RIGHT_0_PENALTY','PRIMER_LEFT_0_SEQUENCE', 'PRIMER_RIGHT_0_SEQUENCE', 'PRIMER_LEFT_0', 'PRIMER_RIGHT_0','PRIMER_LEFT_0_TM', 'PRIMER_RIGHT_0_TM', 'PRIMER_LEFT_0_GC_PERCENT', 'PRIMER_RIGHT_0_GC_PERCENT','PRIMER_LEFT_0_SELF_ANY_TH', 'PRIMER_RIGHT_0_SELF_ANY_TH', 'PRIMER_LEFT_0_SELF_END_TH', 'PRIMER_RIGHT_0_SELF_END_TH', 'PRIMER_LEFT_0_HAIRPIN_TH','PRIMER_RIGHT_0_HAIRPIN_TH', 'PRIMER_PAIR_0_PRODUCT_SIZE']]'''
primer_df.to_csv(sys.argv[2])
