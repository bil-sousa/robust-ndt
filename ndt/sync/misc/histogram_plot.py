"""
Script to create paper histogram plots
of the network characteristics
Created by Cláudio Modesto
LASSE
"""

import networkx as nx
from matplotlib import pyplot as plt

crosshaul = nx.read_gml("../../../physical_twin/topologies/5G_crosshaul_51.gml")
germany = nx.read_gml("../../../physical_twin/topologies/germany_50.gml")
passion = nx.read_gml("../../../physical_twin/topologies/HPASSION_128.gml")
random = nx.read_gml("../../../physical_twin/topologies/synth_topology_700.gml")

crosshaul_capacity = nx.get_edge_attributes(crosshaul, "capacity")
crosshaul_delay = nx.get_edge_attributes(crosshaul, "delay")

germany_capacity = nx.get_edge_attributes(germany, "capacity")
germany_delay = nx.get_edge_attributes(germany, "delay")

passion_capacity = nx.get_edge_attributes(passion, "capacity")
passion_delay = nx.get_edge_attributes(passion, "delay")

random_capacity = nx.get_edge_attributes(random, "capacity")
random_delay = nx.get_edge_attributes(random, "delay")

plt.subplot(4, 1, 1)
plt.hist(crosshaul_capacity.values(), color='#4C72B0', edgecolor='white', alpha=0.8)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("5G-Crosshaul")
plt.subplot(4, 1, 2)
plt.hist(germany_capacity.values(), color='#4C72B0', edgecolor='white', alpha=0.8)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Germany")
plt.subplot(4, 1, 3)
plt.hist(passion_capacity.values(), color='#4C72B0', edgecolor='white', alpha=0.8)
plt.tight_layout()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("PASSION")
plt.subplot(4, 1, 4)
plt.hist(random_capacity.values(), color='#4C72B0', edgecolor='white', alpha=0.8)
plt.gcf().supylabel("Occurrences", fontsize=15)
plt.tight_layout()
plt.xlabel("Capacity (Mbits/s)", fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Synthetic-700")
plt.savefig("figures/hist_capacities.pdf", bbox_inches="tight")
plt.close()

plt.subplot(4, 1, 1)
plt.hist(crosshaul_delay.values(), color='#069736', edgecolor='white', alpha=0.8)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("5G-Crosshaul")
plt.subplot(4, 1, 2)
plt.hist(germany_delay.values(), color='#069736', edgecolor='white', alpha=0.8)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Germany")
plt.subplot(4, 1, 3)
plt.hist(passion_delay.values(), color="#069736", edgecolor='white', alpha=0.8)
plt.tight_layout()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("PASSION")
plt.subplot(4, 1, 4)
plt.hist(random_delay.values(), color="#069736", edgecolor='white', alpha=0.8)
plt.gcf().supylabel("Occurrences", fontsize=15)
plt.tight_layout()
plt.xlabel("Propagation delay (ms)", fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Synthetic-700")
plt.savefig("figures/hist_delay.pdf", bbox_inches="tight")
plt.close()
