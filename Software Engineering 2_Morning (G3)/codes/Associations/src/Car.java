/*
 * This class has a class Car as the main element into 
 * the tunning app.
 * 
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co>
 */

/**
 * This class represents the definition of a tunned car.
 */
public class Car {
    
    public String brand;
    public Engine engine;

    public Car(String brand, Engine engine){
        this.brand = brand;
        this.engine = engine;
    }

    public String toString(){
        String output = "I am a car of brand " + this.brand + ".";
        output += this.engine.info();
        return output;
    }
}
