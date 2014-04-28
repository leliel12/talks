#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from yatel import dom, db

# Pensemos en una red exploratoria totalmente rara

# Super heroes
haps = [dom.Haplotype("Batman", name="Bruce Wayne", debut=1939),
        dom.Haplotype("Alfred", name="Alfred Pennyworth", debut=1943),
        dom.Haplotype("Superman", name="Clark Joseph Kent", debut=1938),
        dom.Haplotype("Lex Luthor", name="Alexander Joseph Luthor")]

# Creamos arcos entre amigos = 1 enemigos = 2
edges = [dom.Edge(1, "Batman", "Superman"),
         dom.Edge(1, "Batman", "Alfred"),
         dom.Edge(2, "Superman", "Lex Luthor")]

# Agregamos hechos
facts = [dom.Fact("Batman", job="Billonaire", family="Murdered"),
         dom.Fact("Batman", job="Super Hero", city="Gotham"),
         dom.Fact("Batman", job="Vigilante", created_by="Bob Kane"),
         dom.Fact("Alfred", job="Buttler", created_by="Bob Kane"),
         dom.Fact("Lex Luthor", job="Billonaire"),
         dom.Fact("Lex Luthor", job="Criminal Mastermind"),
         dom.Fact("Lex Luthor", job="US President"),
         dom.Fact("Superman", job="Super Hero"),
         dom.Fact("Superman", created_by="Jerry Siegel"),
         dom.Fact("Superman", created_by="Joe Shuster"),
         dom.Fact("Superman", job="Reporter"),
         dom.Fact("Lex Luthor", created_by="Jerry Siegel"),
         dom.Fact("Lex Luthor", created_by="Joe Shuster")]

# Validamos que la red sea consistente
dom.validate(haps, facts, edges)

# Persistimos la red en nuestra base de datos
db_exist = os.path.exists("superheroes.db")
conn = db.YatelConnection("sqlite", "superheroes.db")

if db_exist:
    # si la base de datos ya existe
    # asumimos que es una base de datos de yatel
    conn.init_yatel_database()
else:
    conn.init_with_values(haps, facts, edges)

list(conn.enviroment(job="Super Hero"))
#OUT# [<Haplotype 'Batman' at 0x1cb1e90>, <Haplotype 'Superman' at 0x1cb1f90>]

list(conn.enviroment(job="Billonaire"))
#OUT# [<Haplotype 'Batman' at 0x1caae50>, <Haplotype 'Lex Luthor' at 0x1cb1c90>]

list(conn.enviroment(created_by="Bob Kane"))
#OUT# [<Haplotype 'Batman' at 0x1cb80d0>, <Haplotype 'Alfred' at 0x1cb8150>]

list(conn.filter_edges(0,1))
#OUT# [<Edge '(u'Batman', u'Superman') 1.0' at 0x305ee90>,
#OUT#  <Edge '(u'Batman', u'Alfred') 1.0' at 0x305ee50>]

from yatel.conversors import yjf2yatel
with open("bk.yjf", "w") as fp:
    yjf2yatel.dump(conn.iter_haplotypes(), conn.iter_facts(),
                   conn.iter_edges(), conn.iter_versions(),
                   fp) # escribe en el stream fp


with open("bk.yjf") as fp:
    haps, facts, edges, versions = yjf2yatel.load(fp) # lee la red del stream fp
    print haps
