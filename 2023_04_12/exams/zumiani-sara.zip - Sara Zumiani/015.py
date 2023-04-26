import random

def generate_MAC():
    out = ''
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for _ in range(5):
        out += random.choice(nums)
        out += random.choice(nums)
        out += ':'
        
    out += random.choice(nums)
    out += random.choice(nums)
    
    return out