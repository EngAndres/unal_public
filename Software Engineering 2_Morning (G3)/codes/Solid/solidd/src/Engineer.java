/*
 * This file has a class to represent an engineer in the simulation.
 * 
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co>
 */

/**
 * This class represents the behavior of a engineer as a human profession
 * into the simulation.
 */
public class Engineer extends Human {
    
    private String speciality;
   
    public Engineer(String name, int age, int speciality){
        super(name, age);
        this.defineSpeciality(speciality);
    }

    private void defineSpeciality(int speciality){
        if(speciality == 1)
            this.speciality = "Civil";
        else if(speciality == 2)
            this.speciality = "Electrical";
        else if(speciality == 3)
            this.speciality = "Chemical";
        else
            this.speciality = "Computer";
    }

    @Override
    public void whoIAm(){
        System.out.println("My name is " + this.name + ", I am " + this.age +
                            " years old, and I am a " + this.speciality +
                            " engineer.");
    }
}
