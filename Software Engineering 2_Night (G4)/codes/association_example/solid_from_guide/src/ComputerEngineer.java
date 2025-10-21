/*
 * This file has an engineer class. This is part of current platform.
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co>
 */

 /**
  * This class represents the behavior of an 
  * engineer in the simulation.
  */
public class ComputerEngineer extends Human implements IEngineer {
    
    private String discipline;

    public ComputerEngineer(String name, int age, String discipline){
        super(name, age);
        this.discipline = discipline;
    }

    /**
     * This method returns just a notification.
     * @return string confirming identity
     */
    @Override
    public String whoIAm(){
        return "I am a computer engineer, with focus in " + this.discipline + ".\n";
    }

    @Override
    public String toString(){
        return super.toString() + "\n" + this.whoIAm();
    }
}
