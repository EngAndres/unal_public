/*
 * This file has a class to define all humans n the application.
 * 
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co>
 */

 /**
  * This class represents the behavior o a humba in the simulation. 
  */
public class Human implements IHuman {
    
    protected String name;
    protected int age;

    public Human(String name, int age){
        this.name = name;
        this.setAge(age);
    }

    @Override
    public void setAge(int newAge){
        if(newAge < 0){
            System.out.println("Age cannot be negative.");
        }
        else{
            this.age = newAge;
        }
    }

    public String toString(){
        return "My name is " + this.name + ", and my age is " + this.age + "."; 
    }
}