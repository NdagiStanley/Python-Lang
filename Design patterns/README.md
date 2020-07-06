# Designing Software

> Objective: Learn how to apply design patterns to break problems into simple components and create (Python) programs that are easy to write, read and maintain

WHY?

To ensure that my work is CONSISTENT, RELIABLE and UNDERSTANDABLE

## Design Patterns

Let's start in 1994. A book: [Design Patterns: Elements of Reusable Object-Oriented Software][wikipedia] by "the Gang of Four" is published.

They were awarded the 2005 **Programming Languages Achievement Award** due to the impact their work had (continues to have) on _programming practice_ and _programming language design_.

### Gist

Design techniques that would lead to good OOP design

### Statements

- Program to an 'interface', not an 'implementation'
- Favor 'object composition' over 'class inheritance'
  - white-box reuse (class inheritance) _internals of parent class are visible_
  - black-box reuse (object composition)
- Inheritance breaks encapsulation
- delegation' is an extreme form of object composition that can always be used to replace inheritance
- Parameterization - use of 'parameterized types'

  Allows any type to be defined without specifying all the other types it uses—the unspecified types are supplied as 'parameters' at the point of use

- _Dynamic, highly parameterized software_ is harder to **understand and build** than more static software

- Aggregation VS Acquantaince

Maximum maintainability in a design? have loosly-coupled objects.

## Object Modelling

- Object-modeling technique (OMT)
- Unified Modeling Language (UML)

## Separation of Concerns

Edsger W. Dijkstra in his 1974 paper "On the role of scientific thought" said that SoC is being **one- and multiple-track minded simultaneously**. It's so far the only available technique for effective ordering of one's thoughts.

in _Elements of Functional Programming_ by Chris Reade; SoC:

A programmer is doing the following at the same time:

1. describe what is to be computed;
1. organise the computation sequencing into small steps;
1. organise memory management during the computation.

Examples:

- IP stack sepearted into layers
- HTML, CSS, JS
- Software build automation
- Levels of analysis in AI ([David Marr's levels of analysis][analysis])

  A researcher is foccusing on:
  - what some aspect of intelligence needs to compute (Computational level)
  - what algorithm it employs (Algorithmic)
  - how that algorithm is implemented in hardware (Implementation/ Physical level)

- Interface/ Implementation distinction in S/w and H/w engineering
- Subject-oriented programming?
- Aspect-oriented programming

  Aspects like `security`, `logging` are seperate concerns but are elevated to primary concerns to be addressed at initial stages of S/W writing

- [Normalised Systems][ns]?
- Partial classes?

[Reference][SOC_origin]

## Software Design Patterns

A general, reusable solution to a commonly occurring problem within a given context in software design

Software Engineering levels (Cognitive levels):

1. [Programming paradigm][pp]

    - Impertaive: Procedural, OOP
    - Declarative: Functional, Logic, Mathematical

2. Design pattern
3. Algorithm

### Classification

1. Creational patterns (Object creation)
2. Structural patterns (Object relationships)
3. Behavioral patterns (Object interactions and responsibility)
4. Concurrency patterns

[Reference][sdp]

### Et al

> Reader be warned: there's been criticism to the concept of s/w design patterns and design patterns specifically

Like this statement said by [Paul Graham][paul_graham] (best known for Y-Combinator):

```When I see patterns in my programs, I consider it a sign of trouble. The shape of a program should reflect only the problem it needs to solve. Any other regularity in the code is a sign, to me at least, that I'm using abstractions that aren't powerful enough-- often that I'm generating by hand the expansions of some macro that I need to write.```

[wikipedia]: https://en.wikipedia.org/wiki/Design_Patterns
[SOC_origin]: https://en.wikipedia.org/wiki/Separation_of_concerns#Origin
[analysis]: https://en.wikipedia.org/wiki/David_Marr_(neuroscientist)#Levels_of_analysis
[ns]: https://web.archive.org/web/20161120171432/https://en.wikipedia.org/wiki/Normalized_Systems
[pp]: https://en.wikipedia.org/wiki/Programming_paradigm
[sdp]: https://en.wikipedia.org/wiki/Software_design_pattern
[paul_graham]: https://en.wikipedia.org/wiki/Paul_Graham_(programmer)
