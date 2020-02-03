import osmnx as ox
import random

ox.config(log_console = True, data_folder = 'data')
graph = ox.load_graphml('northeuroperails.graphml')
edges = graph.edges
nodes = graph.nodes
flatten = lambda l: [item for sublist in l for item in sublist]
keys = lambda l: set(flatten([n.keys() for n in l.values()]))

random_nodes = random.sample(nodes, 10)
node_keys = keys(nodes) 

edge_keys = keys(edges) 
random_edges = random.sample(edges, 10)

print(node_keys)
'''{'highway', 'y', 'ref', 'osmid', 'x'}'''

print(edge_keys)
'''{'highway', 'service', 'width', 'maxspeed', 'landuse', 'name', 'oneway', 'ref', 'lanes', 'access', 'geometry', 'length', 'osmid', 'bridge', 'tunnel'}'''

for i in range(10):
    print(nodes[random_nodes[i]])
'''
    {'y': 55.2743161, 'x': 38.7319848, 'osmid': 2205752808}
    {'y': 52.2139809, 'x': 20.902197, 'osmid': 3037779457}
    {'y': 66.9634694, 'x': 30.3722644, 'osmid': 2401684595}
    {'y': 53.5086192, 'x': 9.9153028, 'osmid': 1913423341}
    {'y': 59.8749356, 'x': 30.4141804, 'osmid': 1487123270}
    {'y': 52.6323322, 'x': 13.2118428, 'osmid': 930616575}
    {'y': 56.0878707, 'x': 40.2343981, 'osmid': 1483045617}
    {'y': 55.1418079, 'x': 27.2075295, 'osmid': 5969252976}
    {'y': 54.5430073, 'x': 18.4998883, 'osmid': 5487731791}
    {'y': 54.3895476, 'x': 18.5912528, 'osmid': 4696338092}
'''

for i in range(10):
    print(edges[random_edges[i]])
'''
{'osmid': 728279779, 'oneway': False, 'length': 50.577}
{'osmid': 174117143, 'service': 'spur', 'oneway': False, 'length': 329.685, 'geometry': <shapely.geometry.linestring.LineString object at 0x199ddb370>}
{'osmid': [10149024, 10149025, 10149346, 10149345, 9966738, 9966739, 441464372, 47365655, 9966748, 9966749], 'ref': '6185', 'maxspeed': '140', 'oneway': False, 'length': 1210.288, 'bridge': 'yes', 'name': 'SFS Oebisfelde–Spandau', 'geometry': <shapely.geometry.linestring.LineString object at 0x1763b2c40>}
{'osmid': 282557276, 'oneway': False, 'length': 987.414, 'geometry': <shapely.geometry.linestring.LineString object at 0x1462c8f10>}
{'osmid': 22686719, 'oneway': False, 'length': 756.283, 'geometry': <shapely.geometry.linestring.LineString object at 0x16b679580>}
{'osmid': [125967065, 22774363, 95207116], 'oneway': False, 'length': 4885.062, 'bridge': 'yes', 'geometry': <shapely.geometry.linestring.LineString object at 0x148626d30>}
{'osmid': 418163298, 'ref': '201', 'maxspeed': '110', 'oneway': False, 'length': 116.112}
{'osmid': 663504490, 'oneway': False, 'length': 133.13600000000002, 'geometry': <shapely.geometry.linestring.LineString object at 0x1ab73a670>}
{'osmid': 286964425, 'name': 'Gjøvikbanen', 'oneway': False, 'length': 13.796}
{'osmid': 146769507, 'service': 'spur', 'oneway': False, 'length': 141.202, 'geometry': <shapely.geometry.linestring.LineString object at 0x1777efdc0>}
'''
