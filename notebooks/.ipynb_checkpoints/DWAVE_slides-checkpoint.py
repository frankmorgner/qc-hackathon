from IPython.display import HTML

import webbrowser

def qpu():
    return HTML('''<img src="images/dwave_qpu.jpeg" width="500 px">''')

def machine():
    return HTML('''<img src="images/dwave_machine.jpg" width="500 px">''')

def dwave_logo():
    return HTML('''<img src="images/dwave_logo.png">''')

def lab():
    return HTML('''<img src="images/DWave_lab.jpg" width="800 px">''')

def ibmqx():
    # generate an URL
    return webbrowser.open("https://quantumexperience.ng.bluemix.net/qx/editor", new=0)

def chimera():
    return HTML('''<img src="images/dwave_chimera.png" width="400 px">''')

def pegasus():
    return HTML('''<img src="images/dwave_pegasus.jpg" width="1000 px">''')

def annealing():
    return HTML('<img src="images/annealing.png" width="1000 px" align="center">')
    
def spectrum():
    return HTML('<img src="images/eigenspectrum.png" width="500 px" align="center">')

def tunneling():
    return HTML('<img src="images/tunneling.jpeg" width="500 px" align="center">')

def leap():
    return HTML('<img src="images/dwave_leap.png" width="600 px" align="center">')

def community():
    return HTML('<img src="images/dwave_ucs.jpg" width="1000 px" align="center">')

def papers():
    return HTML('<img src="images/papers.jpg" width="1000 px" align="center">')

def advantage():
    return HTML('<img src="images/dwave_advantage.jpg" width="800 px" align="center">')

def thanks():
    return HTML('<img src="images/thanks.gif" width="1000 px" align="center">')

def landscape():
    return HTML('<img src="images/landscape.jpg" width="1000 px" align="center">')

def software():
    return HTML('<img src="images/dwave_sw_stack.png" width="800 px" align="center">')

def framework():
    return HTML('<img src="images/dwave_leap_framework.png" width="800 px" align="center">')

def framework_detailed():
    return HTML('<img src="images/ocean_stack.png" width="1000 px" align="center">')

def go():
    return HTML('<img src="images/panda.gif" width="800 px" align="center">')

#print("Hello BDR .... ")
display(HTML('<img src="images/dwave_logo.png" width="500 px" align="center">'))