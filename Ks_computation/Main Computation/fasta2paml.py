import sys
def remove_stops(seq):
    stops = {"TAG", "TAA", "TGA"}
    codons = [seq[i:i+3] for i in range(0, len(seq), 3) if len(seq[i:i+3]) == 3]
    return "".join([c for c in codons if c.upper() not in stops])
try:
    with open(sys.argv[1], 'r') as f:
        lines = [l.strip() for l in f if l.strip()]
    seqs, curr = [], ""
    for l in lines:
        if l.startswith(">"):
            if curr: seqs.append(curr)
            curr = ""
        else: curr += l
    if curr: seqs.append(curr)
    s1, s2 = remove_stops(seqs[0]), remove_stops(seqs[1])
    L = min(len(s1), len(s2))
    with open(sys.argv[2], 'w') as f:
        f.write(f" 2 {L}\nGeneA     {s1[:L]}\nGeneB     {s2[:L]}\n")
except: sys.exit(1)
