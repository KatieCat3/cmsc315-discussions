# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.


## Readme
- created a parent class named parent class with the class variable category set to person and instance variables name and age.
- created the display_info() method to return the person's name, age, and category.
- created a child class named childclass that inherited from parent class.
- added the variable role which was set to student and the instance variables student_id and major.
- overrode the display_info() method and created the study() method. 
- created objects for Taylor Swift and Selena Gomez to demonstrate class and instance namespaces.
- added graduation_year = 2028 to the Taylor Swift object and used __dict__ to display the object and class namespaces.
- created an Ariana Grande object with a course list to demonstrate shallow and deep copying.
- added Advanced Programming Languages to the original course list for the shallow copy to show a change and the deep copy to remain unchanged.
- created a Britney Spears parent class object and a Taylor Swift child class object in main().
- added the change_major() method to change Taylor Swift's major from cloud computing to computer science. 