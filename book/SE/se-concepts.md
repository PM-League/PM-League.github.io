# SEBoK 2.9

Notes from Guide to the Systems Engineering Body of Knowledge (SEBok), version 2.9

## Part 3: Systems Engineering and Management (SE&M)

### Systems Engineering and Management

Systems Engineering and Management (SE&M) articles provide system lifecycle best practices for defining and executing interdisciplinary processes to ensure that customer needs are satisfied with a technical performance, schedule, and cost compliant solution.

### SE&M Knowledge Areas

The SE&M articles are organized into the following Knowledge Areas (KAs).

* Systems Engineering STEM Overview
* Model-Based Systems Engineering (MBSE)
* Systems Life Cycle Approaches
* System Life Cycle Models
* Systems Engineering Management
* Business and Mission Analysis
* Stakeholder Needs Definition
* System Architecture Definition
* Detailed Design Definition
* System Analysis
* System Realization
* System Implementation
* System Integration
* System Verification
* System Transition
* System Validation
* System Operation
* System Maintenance
* System Specialty Engineering
* Logistics
* Service Life Management
* Systems Engineering Standards

### Systems Engineering & Management Overview

The **role** of Systems Engineering (SE) is to define system, constraints, allocations, behavior and structure characteristics to satisfy customer needs.

The **system** is defined in terms of

* hierarchical structural elements, and
* their behavior interactions.

The **interactions** include the exchange of data, energy, force, or mass which modifies the state of the cooperating elements resulting in emergent, discrete, or continuous **behaviors**.

The **behaviors** are at sequential levels of aggregation (bottoms-up) or decomposition (top-down) to satisfy requirements, constraints, and allocations.

SE collaborates within an integrated product **team** with electrical, mechanical, software, and specialty engineering to define the subsystem and component detailed design implementations to develop a holistic technical solution.

### Model-Based Systems Engineering (MBSE)

Model-based Systems Engineering (MBSE)

* is a paradigm that uses formalized representations of systems, known as models, to support and facilitate the performance of SE tasks throughout a system’s life cycle.
* is frequently contrasted with legacy document-based approaches where systems engineering captures system design information via multiple independent documents in various non-standardized formats.
* consolidates of system information in system design models, which provide primary SE artifacts.

These system models, which are generally expressed in a standardized modelling language such as Systems Modeling Language (SysML®) express key system information in a concise, consistent, correct, and coherent format.

When implemented properly, MBSE models permit the standardized consolidation and integration of system knowledge across engineering disciplines and subsystems and streamline key systems engineering tasks while also minimizing developmental risk.

#### System Models

##### Definition of a model

Models

* are representations that are used to capture, analyze, and/or communicate information about a system or concept.
* can vary in scope, purpose, and type, and can be utilized both individually as stand-alone entities as well as in concert with each other as part of an integrated set.

##### Model Properties

A model can be described and classified with respect to the following properties:

* Scope
* Domain
* Formality
* Abstraction
* Physical/conceptual
* Descriptive/analytical
* Fidelity
* Completeness
* Integration
* Quality

##### Criteria for Effective MBSE Models

While a successful MBSE workflow can involve the use of several different interconnected or standalone models of various scopes and types based on user needs, the main system model in an MBSE projects generally should have
the following characteristics:

1. A scope which matches the scope of the project (i.e., it should encompass the entire SoI);
2. Representative of a holistic perspective from all relevant domains.
3. Strict compliance with a previously established standardized modeling language, whether that be an existing language such as SysML® or a custom formalism.
4. Fully abstracted, to only include relevant information appropriate for the SoI and its desired use-case(s).
5. Conceptual in nature, to permit the capture of intangible information (e.g., system requirements)
6. Containing a description of the system functional and structural architecture at minimum and supplemented by
   integrated analytical/quantitative property descriptions as needed.
7. Demonstrating sufficient fidelity to capture relevant system elements and behavior.
8. Fully complete given its scope.
9. Integrated with any necessary auxiliary models.
10. Sufficiently high-quality as to meet the needs of those designing, developing, or otherwise working on the system.
    In terms of content, effective system models are expected to capture key system information regarding requirements, system functionality/behavior, structure/form, properties, and interconnections between system components.

##### Digital Twins

When MBSE models of physical systems are built with sufficient completeness and fidelity, it is possible for them to function as "digital twins" of the systems they represent.

Digital twins provide a means of accurately representing a system’s form and function throughout the system’s lifecycle, all within a digital environment.

Creating such digital twins allow

* testing, analysis, and optimization of systems in a virtual environment at
  * no risk to the actual system of interest, and
  * a greatly reduced cost/burden.
* representing the behavior of systems under conditions which would be impractical or impossible to induce under experimental conditions, thereby making it possible to obtain information not obtainable via study of the original physical system.

## Knowledge Area: Systems Lifecycle Approaches

### Systems Lifecycle Approaches

Key principles:

* life cycle,
* life cycle model, and
* life cycle processes.

A generic SE paradigm is described; this forms a starting point for discussions of more detailed life cycle knowledge.

#### Topics

This KA contains the following topics:

* Generic Life Cycle Model
* Applying Life Cycle Processes
* Life Cycle Processes and Enterprise Need

#### Life Cycle Terminology

The term "life cycle" is used to describe

* the complete life of an instance of a system-of-interest (SoI), and
* the managed combination of multiple such instances to provide capabilities which deliver stakeholder satisfaction.

A life cycle model:

* identifies the major stages that a specific SoI goes through, from its inception to its retirement.
* is generally implemented in development projects and are strongly aligned with management planning and decision making.

#### Generic Systems Engineering Paradigm

Overall goals of any SE effort:

* understanding of stakeholder value,
* selection of a specific need to be addressed,
* transformation of that need into a system (the product or service that provides for the need), and
* use of that product or service to provide the stakeholder value.

SoI's identified in the formation of a System Breakdown Structure (SBS).
SoI 1 is broken down into its basic elements, which in this case are systems as well (SoI 2 and SoI 3).
These two systems are composed of system elements that are not refined any further.

### Generic Life Cycle Model

Each SoI has an associated LC model.

The generic LC model below applies to a single SoI.

SE must generally be synchronized across a number of tailored instances of such LC models to fully satisfy stakeholder needs.

| ![Figure SBS](../images/sebok-SBS.svg) |
| :----------------------------------: |
|      System Breakdown Structure      |

| ![Figure SOI_LC](../images/sebok-SOI_LC.svg) |
| :----------------------------------------: |
|              SoI LC/Processes              |

#### A Generic System Life Cycle Model

There is no single "one-size-fits-all" system LC model that can provide specific guidance for all project situations.

The model is defined as a set of stages, within which technical and management
activities are performed.

The stages are terminated by decision gates, where the key stakeholders decide whether

* to proceed into the next stage,
* to remain in the current stage, or
* to terminate or re-scope related projects.

Stages:

1. Definition
   * Concept Definition
   * System Definition
2. System Realization
3. System Production, Support, and Utilization (PSU)
   * System Production
   * System Support
   * System Utilization
4. System Retirement

### Applying Life Cycle Processes

The Generic Life Cycle Model describes a set of life cycle stages and their relationships.

In defining this we described some of the technical and management activities critical to the success of each stage.

While this association of activity to stage is important, we must also recognize the through life relationships between these activities to ensure we take a systems approach.

SE technical and management activities are defined in a set of life cycle processes.

These group together closely related activities and allow us to describe the relationships between them.

In this topic, we discuss a number of views on the nature of the inter-relationships between process activities within a life cycle model.

In general, the technical and management activities are applied in accordance with the principles of concurrency, iteration and recursion described in the generic systems engineering paradigm.

These principles overlap to some extent and can be seen as related views of the same fundamental need to ensure we can take a holistic systems approach, while allowing for some structuring and sequence of our activities.

The views presented below should be seen as examples of the ways in which different SE authors present these overlapping ideas.

#### Life Cycle Process Terminology

##### Process

* Is a series of actions or steps taken in order to achieve a particular end, and
* Can be performed by humans or machines transforming inputs into outputs.
* Are interpreted in several ways, including
  * technical,
  * LC,
  * business, or
  * manufacturing flow processes.

##### Requirement

* Are something that are needed/wanted but may not be compulsory in all circumstances,
* May refer to product/process characteristics/constraints.
* Different understandings of requirements are dependent upon
  * process state,
  * level of abstraction,
  * and type (e.g. functional, performance, constraint).
* May have multiple interpretations over time.
* Exist at multiple levels of enterprise/systems with multiple levels of abstraction, ranging from
  * highest level of the enterprise capability/customer need to
  * lowest level of the system design.
* Need to be defined at the appropriate level of detail for the level of the entity to which they apply.

##### Architecture

* Organizational structure of a system, whereby the system can be defined in different contexts.
* Is the art or practice of designing the structures.
* Can apply for a system product, enterprise, or service.
* Closely related to framework, as they are ways of representing architectures.

#### Life Cycle Process Concurrency

In the Generic LC Model, the execution of process activities is not compartmentalized to particular LC stages.

| ![Figure RUP](../images/sebok-RUP.svg) |
| :----------------------------------: |
|               RUP Hump               |

The lines on this diagram represent the amount of activity for each process over the generic life cycle.
The peaks (or humps) of activity represent the periods when a process activity becomes the main focus of a stage.
The activity before and after these peaks may represent through life issues raised by a process focus, e.g. how likely maintenance
constraints will be represented in the system requirements.
These considerations help maintain a more holistic perspective in each stage, or they can represent forward planning to ensure the resources needed to complete future activities have been included in estimates and plans, e.g. all resources needed for verification are in place or available.
Ensuring this hump diagram principle is implemented in a way which is achievable, affordable and appropriate to the situation is a critical driver for all life cycle models.

#### Life Cycle Process Iteration

The concept of iteration applies to LC stages within a LC model, and also applies to processes.

| ![Figure LC_process_iteration](../images/sebok-LC_process_iteration.svg) |
| :--------------------------------------------------------------------: |
|           Concept and System Definition processes iterations           |

Figure 3 below gives an example of the iteration between the other life cycle processes.
The iterations in this example relate to the overlaps in process outcomes shown in Figure 1.
They either allow consideration of cross process issues to influence the system definition (e.g. considering likely integration or verification approaches might make us think about failure modes or add data collection or monitoring elements into the system) or they allow risk management and through life planning activities to identify the need for future activities.

| ![Figure LC_process_iteration_2](../images/sebok-LC_process_iteration_2.svg) |
| :------------------------------------------------------------------------: |
| Concept and System Definition processes iterations --- System realization |

#### Life Cycle Process Recursion

The comprehensive definition of a SoI is generally achieved using decomposition layers and system elements.

Figure 4 presents a fundamental schema of a SBS.
The comprehensive definition of a SoI is generally achieved using decomposition layers and system elements.
In each decomposition layer and for each system, the System Definition processes are applied recursively because the notion of "system" is in itself recursive; the notions of SoI, system, and system element are based on the same
concepts (see Part 2).

| ![Figure LC_process_iteration_recursion](../images/sebok-LC_process_iteration_recursion.svg) |
| :----------------------------------------------------------------------------------------: |
|              Concept and System Definition processes iterations --- Recursion              |

#### Systems Approach to Solution Synthesis

##### Top-Down Approach: From Problem to Solution

In a **top-down** approach, concept definition activities

* are focused primarily on understanding
  * the problem,
  * the operational needs/requirements within the problem space, and
  * the conditions that constrain the solution and bound the solution space.
* determine
  * the mission context,
  * the mission analysis, and
  * te needs to be fulfilled in that context by a new or modified system (i.e. the SoI), and
* address stakeholder needs and requirements.
* consider functional, behavioral, temporal, and physical aspects of one or more solutions based on the results of concept definition.

System analysis:

* considers the advantages and disadvantages of the proposed system solutions both in terms of
  * how they satisfy the needs established in concept definition, as well as
  * the relative cost, time scales and other development issues.
* requires further refinement of the concept definition to ensure all legacy relationships and stakeholders relevant to a particular solution architecture have been considered in the stakeholder requirements.

The outcomes of this iteration between *Concept Definition* and *System Definition* define

* a required system solution and
* its associated problem context, which are used for
  * *System Realization*,
  * *System Deployment and Use*, and
  * *Product and Service Life Management* of one or more solution implementations.

In this approach, problem understanding and solution selection activities are

* completed in the front-end portion of system development and design and then
* maintained and refined as necessary throughout the LC of any resulting solution systems.

Depending upon the LC model, **top-down** activities can be

* sequential,
* iterative,
* recursive, or
* evolutionary.

##### Bottom-Up Approach: Evolution of the Solution

In some situations, the concept definition activities

* determine the need to evolve existing capabilities or
* add new capabilities to an existing system.

During the concept definition, the alternatives to address the needs are evaluated.

Engineers are then led to reconsider the system definition in order to modify or adapt some structural, functional, behavioral, or temporal properties during the product or service life cycle for a changing context of use or for the purpose of improving existing solutions.

Reverse engineering is often necessary to

* enable system engineers to (re)characterize the properties of the
  system-of-interest (SoI) or its elements.
* ensure that system engineers understand the SoI before beginning modification.

A **bottom-up** approach is necessary for

* analysis purposes, or
* (re)using existing elements in the design architecture.

Changes in the context of use or a need for improvement can prompt this.
In contrast, a **top-down** approach is generally used to define an initial design solution corresponding to a problem or a set of needs.

##### Solution Synthesis

In most real problems, a combination of **bottom-up** and **top-down** approaches provides the right mixture of innovative solution thinking driven by need, and constrained and pragmatic thinking driven by what already exists.

This is often referred to as a "middle-out" approach.

As well as being the most pragmatic approach, synthesis has the potential to

* keep the life cycle focused on whole system issues, and
* allow the exploration of the focused levels of detail needed to describe realizable solutions.

## Knowledge Area: System Life Cycle Models

### Categories of Life Cycle Model

Categories of potential LC process models:

* Pre-specified and sequential processes
* Evolutionary and concurrent processes
* Interpersonal and emergent processes

The emergence of integrated, interactive hardware-software systems made pre-specified processes potentially harmful, as the most effective human-system interfaces tended to emerge with its use.
This led to the introduction of more lean approaches to concurrent hardware-software-human factors approaches such as:

* concurrent vee models, and
* Incremental Commitment Spiral Model.

## System Lifecycle Process Drivers and Choices

LC processes:

* impacted by many organizational factors,
* impact all other aspects of system design and development.

### Fixed-Requirements and Evolutionary Development Processes

Aside from the traditional, pre-specified, sequential, single-step development process (identified as Fixed Requirements), there are several models of evolutionary development processes; however, there is no one-size-fits-all approach that is best for all situations.

For rapid-fielding situations, an easiest-first, prototyping approach may be most appropriate.
For enduring systems, an easiest-first approach may produce an unscalable system, in which the architecture is incapable of achieving high levels of performance, safety, or security.

In general, system evolution now requires

* much higher sustained levels of SE effort,
* earlier and continuous integration and testing,
* proactive approaches to address sources of system change,
* greater levels of concurrent engineering, and
* achievement reviews based on evidence of feasibility versus plans and system descriptions.

Evolutionary development processes or methods have been in use since the 1960s (and perhaps earlier).

They allow a project to provide an initial capability followed by successive deliveries to reach the desired SoI.

This practice is particularly valuable in cases in which

* rapid exploration and implementation of part of the system is desired,
* requirements are unclear from the beginning, or are rapidly changing,
* funding is constrained,
* the customer wishes to hold the SoI open to the possibility of inserting new technology when it becomes mature, and
* experimentation is required to develop successive versions.

In evolutionary development a capability of the product is developed in an increment of time.
Each cycle of the increment subsumes the system elements of the previous increment and adds new capabilities to the evolving product to create an expanded version of the product in development.
This evolutionary development process, that uses increments, can provide a number of advantages, including:

* continuous integration, verification, and validation of the evolving product,
* frequent demonstrations of progress,
* early detection of defects,
* early warning of process problems, and
* systematic incorporation of the inevitable rework that may occur.

### Primary Models of Incremental and Evolutionary Development

| ![Figure models_incremental_delivery](../images/sebok-models_incremental_delivery.svg) |
| :----------------------------------------------------------------------------------: |
|              Primary models of incremental and evolutionary development              |

| Type          | Subtype       | Pros                                                                                           | Cons                                                                                    | Examples                                                                    |
| ------------- | ------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Pre-specified | Single-step   | Efficient<br />Easy to verify                                                                  | Difficulties with rapid change<br />Emerging requirements                               | Simple manufactured products                                                |
|               | Multi-step    | Early initial capability<br />Scalability when stable human-intensive systems                 | Emergent requirements or rapid change<br />Architecture breakers                        | Vehicle platform plus value-adding pre-planned product improvements (PPPIs) |
| Evolutionary  | Sequential    | Adaptability to change<br />Smaller human-intensive systems                                    | Easiest-first<br />Late<br />Costly fixes<br />SE time gaps<br />Slow for large systems | Small: Agile<br />Larger: Rapid fielding                                    |
|               | Opportunistic | Mature technology upgrades                                                                     | Emergent requirements or rapid change<br />SySE time gaps                               | Stable development<br />Maturing technology                                 |
|               | Concurrent    | Emergent requirements or rapid change<br />Stable development increments<br />SysE continuity | Overkill on small or highly stable systems                                              | Rapid, emergent development<br />Systems of systems                         |

### Incremental and Evolutionary Development Decision Table

| Type          | Subtype       | Stable, pre-specific<br /> requirements? | Ok to wait for full system<br />to be developed? | Need to wait for<br />next-increment priorities? | Need to wait for<br />next-increment enablers? |
| ------------- | ------------- | ---------------------------------------- | ------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------- |
| Pre-specified | Single-step   | True                                     | True                                             |                                                  |                                                |
|               | Multi-step    | True                                     | False                                            |                                                  |                                                |
| Evolutionary  | Sequential    | False                                    | False                                            | True                                             |                                                |
|               | Opportunistic | False                                    | False                                            | False                                            | True                                           |
|               | Concurrent    | False                                    | False                                            | False                                            | False                                          |

### System Life Cycle Process Models: Vee

| ![Figure vee](../images/sebok-vee.svg) |
| :------------------------------------: |
| Left Side of the Sequential Vee Model  |

| ![Figure stages](../images/sebok-stages.svg) |
| :------------------------------------------: |
|  Stages, Purposes, and Major Decision Gates  |