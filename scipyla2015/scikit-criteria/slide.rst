.. =============================================================================
.. ICONS
.. =============================================================================




.. =============================================================================
.. CONTENT
.. =============================================================================

Multicriterio y Escalas Ordinales
---------------------------------

.. class:: center

    **Sus becas fueron asignadas con esto**


.. class:: center

    Ing. Cabral, Juan B.


.. class:: center

    Universidad Gastón Dachary

    SciPyLa 2015

    05/2015 - Posadas - Argentina


About Me
--------

- Software engineer.
- Data scientist.
- Grad Student In Machine Learning for Astrophisics


.. class:: center

    **Disclaimer:** Wikipedia powered slides!


Decision-making
---------------

-   The cognitive process resulting in the selection of a belief or a course of
    action among several alternative possibilities. Every decision-making
    process produces a final choice that may or may not prompt action.
-   Is the study of identifying and choosing alternatives based on the values
    and preferences of the decision maker.

.. hint::

    DM is one of the central activities of management and is a huge part of
    any process of implementation; also is a subject of active research from
    Edit human performance with regard to decisions has been the subject of
    active research from **Psychological**, **Cognitive** and **Normative**
    perspectives.

    Also can be regarded as a problem-solving activity terminated by a
    solution deemed to be satisfactory. It is, therefore, a reasoning or
    emotional process which can be rational or irrational


Decision-making (Cont.)
-----------------------

.. class:: center

    Rational choice theory encompasses the notion that people try to maximize
    benefits while minimizing costs.


-   A major part of decision-making involves the analysis of a finite set of
    alternatives described in terms of evaluative criteria.
-   These criteria may be benefit or cost in nature. (*Maximization* an
    *Minimization* problems).
-   The problem might be to rank these alternatives in terms of how attractive
    they are to the decision-maker(s) when all the criteria are considered
    simultaneously.

.. important::

    .. class:: center

        Solving such problems is the focus of multi-criteria decision analysis
        (**MCDA**), also known as multi-criteria decision-making (**MCDM**).


Rational & Irrational Decision-making
-------------------------------------

-   In economics, it is thought that if humans are rational and free to make
    their  own decisions, then they would behave according to rational choice
    theory.
-   The people make decisions by determining the likelihood of a potential
    outcome, the value of the outcome, multiplying the two, and then
    choosing the more positive of the two outcomes.
-   In reality some factors that affect decision-making abilities and cause
    people to make irrational decisions (availability bias)


Information Overload
--------------------

.. important::

    IO is a gap between the volume of information and the tools we need to
    assimilate it. If the gap grows your decision is worse.

**Factors**

    #. Personal Information Factors.
    #. Information Characteristics.
    #. Tasks and Process.
    #. Organizational Design.
    #. Information Technology.

-   Hall, Ariss & Todorov (2007) described an
    illusion of knowledge: **too much knowledge it actually interferes with**
    **their ability to make rational decisions.**


Multiple-criteria decision analysis
-----------------------------------

.. class:: center

    Whether in our daily lives or in professional settings, there are typically
    multiple conflicting criteria that need to be evaluated in
    making decisions.

    we usually weigh multiple criteria implicitly and we may be comfortable
    with the consequences of such decisions that are made based on only
    intuition.

    when stakes are high, it is important to properly structure the problem
    and explicitly evaluate multiple criteria.

.. important::

    MCDM or MCDA is concerned with structuring and **solving** decision and
    planning problems involving multiple criteria.

    **"Solving"** can be:

    -   Best alternative, small set of best alternatives or grouping
        alternatives.
    -   An extreme interpretation could be to find all "efficient" or
        "nondominated" alternatives.

    A nondominated solution has the property that it is not possible to move
    away from it to any other solution without sacrificing in at least one
    criterion.


MCDA - Typologies
-----------------

-   **Multiple-criteria evaluation problems:** These problems consist of a
    finite number of alternatives, explicitly known in the beginning of the
    solution process. Each alternative is represented by its performance in
    multiple criteria. The problem may be defined as finding the best
    alternative for a decision maker (DM), or finding a set of good
    alternatives.
-   **Multiple-criteria design problems (multiple objective mathematical**
    **programming problems):** In these problems, the alternatives are not
    explicitly known. An alternative (solution) can be found by solving a
    mathematical model. The number of alternatives is either infinite and
    not countable (when some variables are continuous) or typically very
    large if countable (when all variables are discrete).

Also:

-   There are methods that require the DM’s preference information at the start
    of the process, transforming the problem into essentially a single criterion problem.
    (**prior articulation of preferences**).
-   Some methods require preference information from the DM throughout the solution process.
    (**progressive articulation of preferences**).
-   MC design problems typically require the solution of a series of
    mathematical programming models in order to reveal implicitly defined solutions.
    (**posterior articulation of preferences"**).

Representations and definitions
-------------------------------

The MCDM problem can be represented in the criterion space or the decision
space. Alternatively, if different criteria are combined by a weighted linear
function, it is also possible to represent the problem in the weight space.

.. figure:: imgs/space_def.png
    :align: center
    :scale: 50 %

where **q** is the vector of **k** criterion functions
(objective functions) and **Q** is the feasible set, **Q ⊆ R^k**.

If Q is defined explicitly or implicity (by a set of alternatives),
the resulting problem is called a Multiple Criteria Evaluation or Design
problem.

X is the feasible set and x is the decision variable vector of size n.

Te quotation mark indicate the maximization is not well-defined.


Representations and definitions (cont.)
---------------------------------------

.. image:: imgs/space_dem.png
    :align: center
    :scale: 30 %

**Definitions:**

.. image:: imgs/4def.png
    :align: center
    :scale: 50 %

-   **Ideal point:** (in criterion space) represents the best (the maximum for
    maximization problems and the minimum for minimization problems) of each
    objective function, and typically corresponds to an infeasible solution.
-   **Nadir point:** (in criterion space) represents the worst (the minimum
    for maximization problems and the maximum for minimization problems) of
    each objective function among the points in the nondominated set, and is
    typically a dominated point.


Decision-Makin Paradox
----------------------

-   Hay muchos metodos MCDA (normativos y descriptivos); y cada uno clama ser
    el mejos. Sin embargo muchos de estos metodos retornan diferentes resultados
    para los mismos problemas con exactamente los mismos datos.
-   Encontrar un el mejor metodo es un problema de MCDA en si mismo.
-   Naturalmente es necesario conocer el mejor metodo a-priori.


Decision-Makin Paradox (cont.)
------------------------------

-   A traves de un estudio [Triantaphyllou1989]_ [Triantaphyllou,2000]_
    Se realizo un experimento de selección de metodos utilizando 4 metodos.
    WSM, WPM y dos variantes de AHP. Cuando se usaba un metodo *X*
    (perteneciente a los anteriores, indicaba que *Y* era el mejor. Cuando se
    utilizaba *Y* el resultado decia que *Z* era mejor.
-   Para enunciar el problema se utilizaron 2 criterios:
    #.  Todo metodo debe ser tan precido en problemas multidimensionales como
        uni-dimensionales (se comparo resultados con WSUM) es lo llamaso
        ranking reversal tipo 5.
    #.  Resultados de Analisis de ranking reversals tipo 2.


Ranking Reversal
----------------

-   Esencialmente son: Test Cases
-   La idea es modificar las alternativas de tal forma que "suponemos" que las
    mejores alternativas no cambian.


Ranking Reversal (cont.)
------------------------

Si tenemos tres Alternativas ``A > B > C``

Tipos:

    -   **Tipo 1:** Agregamos una alternativa D igual o parecida a B o C y
        validamos que la mejor alternativa no cambie.
    -   **Tipo 2:** Reemplazamos B por D siendo D > B. Esperamos que A
        siga siendo la mejor.
    -   **Tipo 3:** Descomponemos el problema es problemas de 2 alternativas
        por ves, y verificamos que ninguno de ellos no se contradiga con el
        problema mayor.
    -   **Tipo 4:** Igual al tipo 3 pero solo comparamos entre ellos ignorando
        el general.
    -   **Tipo 5:** Comparaciones unidimensionales vs multidimensionales.


Ranking Reversal (cont.)
------------------------

-   Puede que una falla en un ranking reversal sea un resultado deseado.
-   Se da en situaciones racionales.
-   Conjetura: Intuyo que pasa en Machine Learning.

Ejemplo:

    - Un comprador M1 que le gusta el lujo, Un comprador M2 que no tiene
      dinero.
    - Un auto A1 lujoso y caro y un auto A2 barato y con poco confort.
    - ``M1 = A1 > A2`` y ``M2 = A2 > A1``



¿Preguntas?
-----------

    - Charla:
    - Contactos:
        - `jbcabral.com <http://jbcabral.com>`_
        - Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>




