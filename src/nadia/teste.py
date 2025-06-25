from nadia.nadia_pt_fo import check_proof

proof = '''
1. ~(A & B) pre
2. ~A | ~B demorgan1 1
'''
print(check_proof(proof))

