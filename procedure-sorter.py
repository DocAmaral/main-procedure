procedures = []
main_procedure = []
additional_procedure = []
surgery = None

hard_main = [
    #General
    'ectomy',
    'bypass',
    'anastomosis',
    #Anacronyms
    'CABG',
    'BSO'
    
]

soft_main = [
    #General
    'colostomy',
    'bypass',
    'anastomosis',
    #Anacronyms
    'BSO',
    'I&D'
    
]

hard_add = [
    'laparoscopy',
    'toracoscopy'

]

#Get procedures
while surgery != 'end':
    surgery = input('Input procedure: ')
    if surgery != 'end':
        procedures.append(surgery)

#Sort procedures
for ops in procedures:
    for criteria in hard_main:
        if criteria in ops:
            main_procedure.append(ops)
    

if len(main_procedure) > 0:
    print(main_procedure)
else:
    print(procedures)
