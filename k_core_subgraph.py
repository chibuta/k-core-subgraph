#The network is built using the python networx library
import sys
import networkx as nt

def build_network(ppi_file):
    # Open the network file
    with open(ppi_file, "r") as ppi:
        # Empty network graph
        network = nt.Graph()

        # Each protein in the network
        for interaction in ppi:
            # Strip and split edge
            nodes = interaction.rstrip("\n").split("\t")
            # Add nodes to the graph
            network.add_edge(nodes[0], nodes[1])
    return network

def find_kcores(ppi_file):

    k_cores = {}          #dictionary to hold proteins and the highest k-core they belong to
    highest_kcore =0    #keep track of the hightest recored k-core

    network = build_network(ppi_file)         #Build a network
    protein_cores = nt.core_number(network)      #get max k-cores from the network for each protein

    #group proteins based on the highest k-core in the network where each protein belong
    for protein, k_core in protein_cores.items():

        if highest_kcore < k_core: #keep track of the highest k-core
            highest_kcore = k_core

        #group the proteins in a dictionary based on highest k_core they belong to
        if k_core in k_cores:
            k_cores[k_core].append(protein)
        else:
            k_cores[k_core]=[protein]

    return highest_kcore,k_cores

ppi_file = 'yeast_PPI.txt'  #path to a network file

highest_kcore,k_cores = find_kcores(ppi_file) #get all possible cores and highest k-cores

#print highest k-core from the graph and return the proteins in that graph
print("The highest k-core is a {0}-core and there are {1} proteins in that {0}-core. \n"
      "The proteins are: {2}".format(highest_kcore,len(k_cores[highest_kcore]),k_cores[highest_kcore]))


