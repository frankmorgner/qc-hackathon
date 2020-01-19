import matplotlib.pyplot as plt
import itertools

def plot_landscape(qubo, n_qubits):
    # just implemented for 4 qubits!!!
    assert n_qubits==4
    
    # generate all possible qubit samples
    qbits = [seq for seq in itertools.product([0,1], repeat=n_qubits)]
    # calculate the energies for each sample 
    energies = [qubo(x,y,z,w) for x,y,z,w in qbits]
    labels = ["".join([str(i) for i in sub]) for sub in qbits]
    
    # vizualize energie landscape
    fig = plt.figure(figsize=(8,5))
    plt.plot(labels, energies)
    plt.xlabel('sample')
    plt.ylabel('energy')
    plt.xticks(rotation=45)
    plt.show()
