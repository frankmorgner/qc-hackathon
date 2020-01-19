import itertools, math

def print_sv(statevector, mode='row'):
    num_qubits = int(math.log(len(statevector),2))
    a = [[0,1]]*num_qubits
    labels = [''.join([str(n) for n in x]) for x in list(itertools.product(*a))]
    kets = [str(statevector[i]) + '|' + l + '\u27E9' for i,l in enumerate(labels) if statevector[i]!=0j]
    if mode=='row':
        return ' + '.join(kets)
    if mode=='col':
        return kets