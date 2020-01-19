from qiskit import execute, Aer

def get_statevector_for_circuit(qc, backend='statevector_simulator'):
    be = Aer.get_backend(backend)
    job = execute(qc, be)
    result = job.result()
    
    return result.get_statevector(qc, decimals=3)
    
    