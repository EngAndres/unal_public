/*
 * This file has an engineer class. This is part of current platform.
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co>
 */

 /**
  * This class represents the behavior of an 
  * engineer in the simulation.
  */
public class ChemicalEngineer extends Human implements IEngineer {

    public ChemicalEngineer(String name, int age){
        super(name, age);
    }

    @Override
    public String whoIAm(){
        return "I am a chemical engineer.\n";
    }

    public String toString(){
        return super.toString() + "\n" + this.whoIAm();
    }
}