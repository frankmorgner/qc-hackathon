from IPython.display import HTML

import webbrowser

def qiskit_xp():
    return HTML('''<img src="images/qiskit_xp.png" width="1000 px">''')

def qiskit():
    return HTML('''<img src="images/qiskit_banner.png" width="500 px">''')

def ibmqx_logo():
    return HTML('''<img src="images/IBM-cloud.jpg">''')

def lab():
    return HTML('''<img src="images/lab.jpg" width="1000 px">''')

def ibmqx():
    # generate an URL
    return webbrowser.open("https://quantumexperience.ng.bluemix.net/qx/editor", new=0)

def ibmq_qcc():
    return HTML('''<img src="images/ibmq_qcc.jpg" width="1000 px">''')

def git():
    return webbrowser.open("https://github.com/qiskit", new=0)

def quantum():
    return HTML('<img src="https://66.media.tumblr.com/763756ea907e30b639da239618bbe2d3/tumblr_mlotjw0e2C1r4xjo2o1_500.gif" width="500 px" align="center">')
    
def model():
    return HTML('<img src="images/model.jpg" width="1000 px" align="center">')

def community():
    return HTML('<img src="images/community.jpg" width="1000 px" align="center">')

def entanglement():
    return HTML('<img src="images/entanglement.jpg" width="1000 px" align="center">')

def aqua():
    return HTML('<img src="images/aqua.jpg" width="1000 px" align="center">')

def papers():
    return HTML('<img src="images/papers.jpg" width="1000 px" align="center">')

def execution():
    return HTML('''
    <video src="images/executions-week.mp4" width="1000 px" autoplay>
    ''')

def thanks():
    return HTML('<img src="images/thanks.gif" width="1000 px" align="center">')

def system():
    return HTML('<img src="images/system.jpg" width="1000 px" align="center">')

def software():
    return HTML('<img src="images/software_stack.png" width="800 px" align="center">')

def framework():
    return HTML('<img src="images/qiskit-framework.png" width="800 px" align="center">')

def framework_detailed():
    return HTML('<img src="images/qiskit-framework_detailed.png" width="1000 px" align="center">')

def go():
    return HTML('<img src="images/panda.gif" width="800 px" align="center">')

#print("Hello BDR .... ")
display(HTML('<div><br><h1 align="center">The IBM Quantum Experience</h1><br></div>'))