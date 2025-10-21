/*
 * This file contains a class called Human, a main mother class
 * in the app.
 * 
 * Author: Carlos Andrés Sierra <casierrav@unal.edu.co>
 */

 /**
  * This class represents the behavior of any Human in the
  * simulation.
  */
public class Human {
    
    protected String name = "";
    protected int age = -1;

    public Human(String name, int age){
        this.name = name;
        this.age = age;
    }

    /**
     * This method prints the basic information of a human. s
     */
    public void whoIAm(){
        System.out.println("My name is " + this.name + ", I am " + this.age +
                            " years old, and I am unemployed.");
    }
}
