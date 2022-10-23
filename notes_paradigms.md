# Software development processes

## SDLC
 *SDLC* ,or the Software Development Life Cycle, is a model describing the process of bringing a peice of software to market and maintaining it. The basic steps or as they are know phases each encompass different tasks  needed to be completed as the software goes from idea to frution through an iterative process. 
  <!--- https://www.tutorialspoint.com/sdlc/index.htm --->
<image src="DevelopmentDesign/img/SDLC_ISO_IEC_12207.png"><span style="font-size:10px"> Illustration of the generalize SDLC, from the IEEE Guide—Adoption of ISO/IEC TR 24748-1:2010
Systems and Software Engineering—Life Cycle Management—Part 1: Guide for Life Cycle Management</span>
 
 The early models where depicted as circles stemming from the waterflow model. <image src="DevelopmentDesign/img/Waterfall_system_model.jpg"><span style="font-size:10px"> Illustration waterfall model from https://commons.wikimedia.org/wiki/File:Waterfall_system_model.jpg </span>
 
 The modern views tend emphisize to focus on the iterative nature of development. <rewrite> One of these the spiral model where each iteration is succeded by a larger spiral. Personally I like to envison the spiral as a helix as it is not nessesary that a followin iteration take more time or is even completed before you start the next.
 <image src="DevelopmentDesign/img/helix_legend-01.png" >Concept by Lars Eklund, UPPMAX, Uppsala University, art Jonas Söderberg, NBIS/UPPMAX, Uppsala University image is released under CC-BY licence<span style="font-size:10px"> </span>

  The helix depiction of the SDLC emphasise the idea that as cost spiral in each iteration is cumulative and eventually the cost of the next phase is higher than the value of continuing at which point the software starts to trickle out of existence. 


Depending on the chosen method or metodology these steps are genarlly named sligthly diffrent dependent on model but i general the step fullfill the standard SDLC. 

## Spiral model
 The spiral model was developed in 1986 by Barry Boehm in his paper A Spiral Model of Software Development and Enhanchment
 The focus of the spiral model is to identify risk 
<image src="DevelopmentDesign/img/Spiral_model_(Boehm,_1988).png"><span style="font-size:10px"> Illustration of the spiral model as presentes by Boehm 1988, from https://commons.wikimedia.org/wiki/File:Spiral_model_(Boehm,_1988).png </span>


##PHASES OF THE SDLC

## First phase *Risk assessment and Planning*
In the first phase one needs to determine what Trauth et.al call Percetption of need, Feasabillity and Analysis

 Most models cover some form of risk assesment, involved in the requiremnts gathering process. In the Spiral model the concept of risk assessment is essential while in models like RUP it has a lesser role. 

## Second phase  *Design*

## Third phase *Development*
 Appart the algorithm part, testing, and optimisation that is covered elsewhere in the material we will not focus on development.

## Fourth phase *Deployment*/*Testing*

## Fifth phase *Maintenance*/*Deployment and Maintenance*

## RUP
   Rational Unified Process is a software development metod based on iterative obejctoriented development. The idea is that you tailor the development method to fit the project, this howerver is not without cost as adapting and formulating templates take time. It is important to note that development models of this type are not in contrast to Agile development but some consessions to the iterative flow may have to be made as the image depicts RUP follows the phases of design as SDLC (with the addition of a 0th step Buiseness modeling), Each phase in RUP is a complete itreation of the design steps Inception, Elaboration,Construction and Transition
   <image src="DevelopmentDesign/img/Unified_Process_Model_for_Iterative_Development.png">
   <font>image contributated from  Wikimedia Commons and was originaly made Jakob Farian Krarup and released to the public domain under cc 0

### Inception
### Elaboration
### Construction
### Transition
# Paradigms of design

## Structural programming, Structured design
   ### imperative programming
   ### procedural programming
## Declarative programming

## Object Orientation
 An object is the representation of a thing or concept, that encapsulates both data and the actions perfomed on it. A key concept of an object is that it interactact with the world through message passing of its parameters. 
 * The concept of Information Hiding 
 * The concept of Encapsulation
 * The concept of message passing

 Once a set of objects have been identified it is common to abstract these through the process of classification, a process where we abstact a given object into its concepts, as we build out our classes some concepts that have no connection to the objects of our design. Thes classes are commonly known as utility classes. Once the classification and message passing have been designed our classes are gennerally instanciated as objects again which are the interacting entities of our software. 

## Functional programming


# Tools and methodologies  
The tools and methodologies are too numerous to describe in any complete way,<rewrite> and they are always evolving as developers find issues with the models and methodologies they are currently using and trying to adress them there for many models evolve to adress the "lates and greates" method but as on be can guess this means other consessions have to be made. 
<explain system>
The best way to aproach wich methodology one should use is to look at the development requirements of the system that you wish to create and choose the one that lets you do the least amount of work for the highest value. 

In this course we will present a few methodologies which are in no way or form the best or only methods out there but is a start.


## UML
The Unified modelling language was first standardized in November 1997 as [UML-98]. It has its origin in Rumbaugh OMT and Jacobsens efforts with the OOSE (object oriented software enginering). it is by that nature very good att describing the Rational Unified Process (RUP), se below, created by Rumbaugh, Booch and Jacobsen in the late 90s. Today the UML standard is maintanined by the omg standard development organisation https://www.omg.org/spec/UML/2.5/PDF) 

plantuml.org a way of using UML graphs and charts in markdown, and to specify the relationship between objects using text/pseudo code. 

Plantuml vizulaiser is available both as chrome extension and as firefox extension. To see the diagrams the extension has to be loaded.
The traditional method is to use som sort of moddeling software, a complete modeling software allows for atleast forward enginering from models to code. There are ofcourse great comersial versions but also some decent free ones.
draw.io
https://www.eclipse.org/papyrus/

```plantuml
@startuml
!theme superhero
title:"USECASE Diagrams"
skinparam actorStyle awesome
Lecturer -d->(Present slides on UML)
Participant-d->(learn UML from SLIDES)
@enduml
```
```plantuml
@startuml
 !theme _none_
 class01 <|-- class02
 class03 *-- class04
 class05 o-- class06

 class01- class03 : knows >
 class class01 {
    -var01 : Integer
    Time : Date
    #method01()
    +get_var01()
    {method}Without paranteces or Qualifiers
 }
@enduml
```
//legacy style uml
```plantuml
@startuml
!theme amiga 
(*)--> activity1
if "stuff?" then 
-->[true] "action2"
-r->(*)
else 
--> [false](*)
@enduml
``` 
//new style
```plantuml
@startuml
!theme amiga
start
:activity 1;
-> data;
if (stuff?) then (true) 
   :action 2;
else(false)
endif
stop
@enduml
```
Unified modeling language is defined and managed by the OMG(obeject management group)(omg.org), which is a standrard developments organisation with 27 countries and more than 230 organisations which produces standards for buissnes development and the software industry. UML is devided into Diagram types these types are supplemental, behavioural and structural - modeling. The Supplemental modeling is Use Cases, Deployments and Information flows. The Behavioural models include state machines, activities and interactions and are based on actions and common behaviour. Structural modeling models Values, Classifiers and Packages and describe the common structure of the software. Structural modeling is vital to discover proper abstraction of classes and interaction models help you find the methods needed to run an object oriented design. Activities and statemachines are great for describing the flow of a program and to supplement pseudo code when vizualing processes or algorithms.

## RUP Rational Unified Process
A method primarily for generating larger object oriented systems. Partially it can be used even for smaller projects but some of the steps and diagrams would be skipped. The design of the system is a use case driven design where the analyst tries to identify all typical interactions that can be done with the systems. This then works as a requirements analysis for the rest of the design step.





## The AGILE manifesto
https://agilemanifesto.org/

## AGILE Development as a respons to what they called document driven development

## SCRUM and how it fits with AGILE development

## Pair Programming 
 A tool for rapid development is the so called Pair Programming where two developers code on the same code simultatiously one as the "Driver" and one as the "Navigator" 