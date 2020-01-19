import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def matrixform(Q):
    """
    Transforms a given QUBO Q-form into a numeric matrix

    :return:
    matrix - numpy.array
    labels - numpy.array
    """
    keys = np.array(list(Q.keys()))
    vals = np.array(list(Q.values()))

    unq_keys, key_idx = np.unique(keys, return_inverse=True)
    key_idx = key_idx.reshape(-1, 2)

    n = len(unq_keys)

    adj = np.zeros((n, n), dtype=vals.dtype)
    adj[key_idx[:, 0], key_idx[:, 1]] = vals
    
    return adj, unq_keys

def plot_matrixform(Q, colormap='seismic'):
    m, labels = matrixform(Q)
    v_min = np.min(m)
    v_max = np.max(m)
    v_abs = max(abs(v_min), abs(v_max))
    if v_min < 0 < v_max:
        plt.matshow(m, cmap=colormap, vmin=-v_abs, vmax=v_abs)
    else:
        plt.matshow(m, cmap=colormap)
        
    return None

def inclusion2exclusion(df):
    for idx,row in df.iterrows():
        ex_list = list()
        if row['inclusion'] != []:
            for i in row['inclusion']:
                item_fam = df[df['name']==i]['family'].values[0]
                ex_list += [itm for itm in df[df['family']==item_fam]['name'] if itm!=i]
            df.at[idx,'exclusion'] = ex_list
            
    return df

def result_dicts(results, df):
    res = iter(results)
    result_dicts = list()
    for _ in results:
        sample = next(res)
        items = [node for node in sample if sample[node] > 0]
        result_dicts.append(df[df['name'].isin(items)])

    return result_dicts

def str2list(s):
    assert isinstance(s, str)
    if s == '[]':
        return []
    else:
        return [x.strip().strip("'") for x in s[1:-1].split(',')]

def show_bqm_graph(bqm):
    G = bqm.to_networkx_graph()
    elabels = nx.get_edge_attributes(G,'bias')
    nlabels =  nx.get_node_attributes(G,'bias')

    # positions for all nodes
    pos = nx.spring_layout(G)  
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    # edges
    nx.draw_networkx_edges(G, pos, width=3, edge_color='lightgray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()
    