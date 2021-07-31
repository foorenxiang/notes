# Design Patterns Selector

## Creational Patterns

### Abstract Factory

Provides interface to create families of related objects without specifying their concrete classes

### Builder

Separate construction of a complex object from its representation so the same construction process can create different representations

### Factory method

Define an interface for creating an object.  
Subclasses use that interface to decide which class to instantiate.  
Let's a class defer instantiation to subclasses

### Prototype

Specify the kinds of objects to create using a prototypical instances  
Create new objects by copying the prototypes

### Singleton

Ensure a class only has one instance and provide a global point of access to it

## Structural Patterns

### Adapter

Convert the interface of a class into another interface clients expect  
Adapt incompatible class interfaces to allow them to work together

### Bridge

Decouple an abstraction from its implementation so that the two can vary independently

### Composite

Compose objects into tree structures to represent part-whole hierarchies  
Lets clients treat individual objects and compositions of objects uniformly

### Decorator

Attach additional responsibilities to an object dynamically.  
Provides a flexible alternative to sub-classing for extending functionality  

### Facade

Provide a unified interface for a set of interfaces.  
Defines a high level interface that makes the subsystem easier to use  

### Flyweight

Use sharing, to support large numbers of fine grained objects efficiently

### Proxy

Provide a placeholder for another object control access to it

## Behavioural Patterns

### Chain of Responsibility

Avoid coupling the sender of a request to its receiver.  
Achieved by giving more than one receiver object a chance to handle the request  
Chain the receiving objects and pass the request along the chain until an object handles it.

### Command

Encapsulate a request as an object.  
This allows the clients sending the request to be parameterized with different requests, queue or log requests and support undoable operations.  

### Interpreter

Given a language, define its grammer representation along with an interpreter that uses that grammer representation to interpret sentences in the language

### Iterator

Provide a way to access elements of an aggregate object sequentially without exposing its underlying representation

### Mediator

Define an object that encapsulates how a set of objects interact.  
Promotes loose coupling by preventing objects from referencing each other explicitly.  
Their interactions can be varied independently

### Memento

Without violating encapsulation, capture and externalize an object's internal state.  
Allows the object to be restored to this state later

### Observer 

Define a one-to-many dependency between objects.  
So when one object changes state, all its dependents are notified and updated automatically. (Pub Sub)

### State

Allows an object to alter its behaviour when its internal state changes.  
The object will appear to change its class

### Strategy

Define a family of algorithms, encapsulate each one, and make them interchangeable.  
Lets the algorithm vary independently from clients that use it.

### Template Method

Define the skeleton of an algorithm in operation, deferring some steps to its subclasses.  
Lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

### Visitor

Represent an operation to be performed on the elements of an object structure.  
A new operation can be defined without the classes of the elements on which it operates.
