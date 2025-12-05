from itertools import product
symbols=['A','B','C','D','E','-']
enc_target='10011100110111100'
dec_target='0011011100011100'

max_len=6

codewords=[ ''.join(p) for L in range(1,6) for p in product('01', repeat=L) ]

def is_prefix_free(mapping):
    codes=list(mapping.values())
    for a in codes:
        for b in codes:
            if a!=b and (a.startswith(b) or b.startswith(a)):
                return False
    return True

# segmentations

def all_segmentations(s, parts):
    n=len(s)
    res=[]
    def back(i,k,cur):
        if k==parts:
            if i==n: res.append(cur.copy())
            return
        for l in range(1,6):
            if i+l<=n:
                cur.append(s[i:i+l])
                back(i+l,k+1,cur)
                cur.pop()
    back(0,0,[])
    return res

segs1=all_segmentations(enc_target,6)
segs2=all_segmentations(dec_target,5)
print('seg1 candidates',len(segs1),'seg2 candidates',len(segs2))
for s1 in segs1:
    map1={sym:code for sym,code in zip(list('CAD-BE'),s1)}
    ok=True
    codes1=list(map1.values())
    for a in codes1:
        for b in codes1:
            if a!=b and (a.startswith(b) or b.startswith(a)):
                ok=False; break
        if not ok: break
    if not ok: continue
    for s2 in segs2:
        map2={sym:code for sym,code in zip(list('E-DAD'),s2)}
        combined=map1.copy()
        consistent=True
        for k,v in map2.items():
            if k in combined and combined[k]!=v:
                consistent=False; break
            combined[k]=v
        if not consistent: continue
        if set(combined.keys())!=set(symbols):
            continue
        if not is_prefix_free(combined):
            continue
        print('Found mapping:')
        for k in symbols:
            print(k,combined[k])
        print('enc check', ''.join(combined[c] for c in 'CAD-BE'))
        print('dec check', ''.join(combined[c] for c in 'E-DAD'))
        raise SystemExit
print('No mapping found')
