#!/usr/bin/env python
# -*- coding: utf-8 -*-

#===============================================================================
# CREATION
#===============================================================================

from yatel import dom, db

# postgres, oracle, mysql, and many more
nw = db.YatelNetwork("memory", mode="w")

elems = [
    dom.Haplotype(0, name="Cordoba", clima="calor", edad=200, frio=True), # left
    dom.Haplotype(1, name="Cordoba", poblacion=12), # right
    dom.Haplotype(2, name="Cordoba"), # bottom

    dom.Edge(6599, (0, 1)),
    dom.Edge(8924, (1, 2)),
    dom.Edge(9871, (2, 0)),

    dom.Fact(0, name="Andalucia", lang="sp", timezone="utc-3"),
    dom.Fact(1, lang="sp"),
    dom.Fact(1, timezone="utc-6"),
    dom.Fact(2, name="Andalucia", lang="sp", timezone="utc")
]

nw.add_elements(elems)
nw.confirm_changes()


#===============================================================================
# QUERY 1
#===============================================================================

print nw.describe()
# {
#   'haplotype_attributes': {
#       'hap_id': <type 'int'>,
#       'name': <type 'str'>
#   },
#  'fact_attributes': {
#       'idioma': <type 'str'>,
#       'timezone': <type 'str'>,
#       'hap_id': <type 'int'>,
#       'name': <type 'str'>},
#   'mode': 'r',
#   'edge_attributes': {u'max_nodes': 2, u'weight': <type 'float'>},
#   'size': {u'facts': 4, u'haplotypes': 3, u'edges': 3}
# }

for hap in nw.haplotypes():
    print hap
# <Haplotype (0) at 0x2cb8710>
# <Haplotype (1) at 0x2cb8810>
# <Haplotype (2) at 0x2cb8850>

for edge in nw.edges():
    print edge
# <Edge ([6599.0 [0, 1]]  ) at 0x2cb64d0>
# <Edge ([8924.0 [1, 2]]  ) at 0x2cb6dd0>
# <Edge ([9871.0 [2, 0]]  ) at 0x2cb6fd0>

for fact in nw.facts():
    print fact
# <Fact (of Haplotype '0') at 0x2cb6f50>
# <Fact (of Haplotype '1') at 0x2cb6ed0>
# <Fact (of Haplotype '1') at 0x2cb6c50>
# <Fact (of Haplotype '2') at 0x2cb6e90>

#===============================================================================
# QUERY 2
#===============================================================================

hap = nw.haplotype_by_id(2)

for edge in nw.edges_by_haplotype(hap):
    print edge
# <Edge ([9871.0 [2, 0]]  ) at 0x1cf6910>,
# <Edge ([8924.0 [1, 2]]  ) at 0x1cf6810>

for fact in nw.facts_by_haplotype(hap):
    print dict(fact)
# {u'timezone': u'utc', u'lang': u'sp', 'hap_id': 2, u'name': u'Andalucia'}

for hap in nw.haplotypes_by_enviroment(lang="sp"):
    print hap
# <Haplotype (0) at 0x254bfd0>
# <Haplotype (1) at 0x254bc10>
# <Haplotype (2) at 0x254bfd0>

for hap in nw.haplotypes_by_enviroment(timezone="utc-6"):
    print hap
# <Haplotype (1) at 0x14a8210>

for hap in nw.haplotypes_by_enviroment(name="Andalucia"):
    print hap
# <Haplotype (0) at 0x254bb50>
# <Haplotype (2) at 0x254bfd0>

#===============================================================================
# QUERY 3
#===============================================================================

for edge in nw.edges_by_enviroment(name="Andalucia"):
    print edge
# <Edge ([9871.0 [2, 0]]  ) at 0x23e3ad0>

for env in nw.enviroments():
    print env
# <Enviroment {u'lang': u'sp', u'timezone': u'utc-3', u'name': u'Andalucia'} at 0x1f6b490>
# <Enviroment {u'lang': u'sp', u'timezone': None, u'name': None} at 0x1f6b810>
# <Enviroment {u'lang': None, u'timezone': u'utc-6', u'name': None} at 0x1f6b490>
# <Enviroment {u'lang': u'sp', u'timezone': u'utc', u'name': u'Andalucia'} at 0x1f6b810>

for env in nw.enviroments(["lang", "name"]):
    print env
# <Enviroment {u'lang': u'sp', u'name': u'Andalucia'} at 0x1aa4950>
# <Enviroment {u'lang': u'sp', u'name': None} at 0x1aa45d0>
# <Enviroment {u'lang': None, u'name': None} at 0x1aa4950>

from yatel import stats

print stats.average(nw)
# 8464.66666667
print stats.std(nw, name="Andalucia")
import ipdb; ipdb.set_trace()
# 0


#===============================================================================
# DATA MINNING
#===============================================================================

from scipy.spatial.distance import euclidean
from yatel.cluster import kmeans

cbs, distortion = kmeans.kmeans(nw, nw.enviroments(), 2)

for env in nw.enviroments():
    coords = kmeans.hap_in_env_coords(nw, env)
    min_euc = None
    closest_centroid = None
    for cb in cbs:
        euc = euclidean(cb, coords)
        if min_euc is None or euc < min_euc:
            min_euc = euc
            closest_centroid = cb
    print "{} || {} || {}".format(dict(env), closest_centroid, euc)
# {u'lang': u'sp', u'timezone': u'utc-3', u'name': u'Andalucia'} || [0 0 0] || 1.41421356237
# {u'lang': u'sp', u'timezone': None, u'name': None} || [0 1 0] || 0.0
# {u'lang': None, u'timezone': u'utc-6', u'name': None} || [0 1 0] || 0.0
# {u'lang': u'sp', u'timezone': u'utc', u'name': u'Andalucia'} || [0 0 0] || 1.41421356237

