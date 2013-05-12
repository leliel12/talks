#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pilas

pilas.iniciar()

mono = pilas.actores.Mono()
mono.x, mono.y = 100, 100 #
mono.aprender(pilas.habilidades.Arrastrable) #

bananas = pilas.actores.Banana() * 10

bombas = pilas.actores.Bomba() * 5

def mono_come_banana(mono, banana):
    mono.sonreir()
    banana.eliminar()

def bomba_mata_mono(mono, bomba):
    bomba.explotar()
    mono.gritar()
    mono.eliminar()

pilas.escena_actual().colisiones.agregar(mono, bananas, mono_come_banana)
pilas.escena_actual().colisiones.agregar(mono, bombas, bomba_mata_mono)

pilas.ejecutar()
