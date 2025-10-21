/* This file has a class to represent a doctor as a human
 * profession in the simulation.
 * 
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co> 
 */ 

/**
 * This class represents the behavior of a human doctor
 * into the simulation.
 */
public class Doctor extends Human {
    
    private String speciality;

    public Doctor(String name, int age, String speciality){
        super(name, age);
        this.speciality = speciality;
    }

    @Override
    public void whoIAm(){
        System.out.println("My name is " + this.name + ", I am " + this.age +
                            " years old, and I am a medical doctor with emphasis in " +
                            this.speciality);
    }
}
