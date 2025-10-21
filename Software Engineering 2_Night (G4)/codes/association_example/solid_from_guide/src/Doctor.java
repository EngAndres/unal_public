/*
 * This file has a class called doctor.
 * Author: Carlos Andres Sierra (cavirguezs@unal.edu.co)
 */

/**
 * This class represents the behavior of a doctor in the simulation.
 */
public class Doctor extends Human{
    
    public String speciality;

    public Doctor(String name, int age, String speciality){
        super(name, age);
        this.speciality = speciality;
    }

    /**
     * This method return the current status of the doctor.  
     * @return status code
     */
    public String message(){
        return "\nMy speciality is " + this.speciality + ". And, you are sick.\n";
    }

    public String toString(){
        return super.toString() + this.message();
    }
}
