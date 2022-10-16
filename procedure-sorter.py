#Variables
procedures = []
main_procedure = []
additional_procedure = []
surgery = None
i = 1
is_hard_main = False
is_soft_main = False


hard_main = [
    #General
    'ectomy',
    'bypass',
    'ressection',
    'graft',
    'raphy',
    #Acronyms
    'CABG'
]

soft_main = [
    #General
    'repair',
    'ostomy',
    'anastomosis',
    'plication',
    'closure',
    #Acronyms
    'BSO',
    'I&D'
]

hard_add = [
    'otomy',
    'oscopy',
    'exploratory'    
]

#Get procedures
while surgery != 'End':
    surgery = input(f'Input procedure {i!s}:').capitalize() 
    i+=1
    if surgery != 'End':
        procedures.append(surgery)

#Sort procedures
for ops in procedures:
    for criteria in hard_main:
        if criteria in ops:
            is_hard_main = True
            main_procedure.append(ops)
    for criteria in soft_main:
        if criteria in ops:
            is_soft_main = True
            main_procedure.append(ops)
    
#Define main
if len(main_procedure) > 0:
    print('Main procedure is:', main_procedure[0])
    if len(main_procedure) > 1:
        print('Other important procedures are:', main_procedure[1:])
#To be added
#elif len(main_procedure) > 1:
#    if is_soft_main == True and is_hard_main == False
else:
    print(procedures)

# For refinement have all procedures table and specify which should be #0