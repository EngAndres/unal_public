/*
 * This file has an exxtension for the logic of a human who is a musician.
 * 
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co>
 */

/**
 * This class represents the behavior of a Musician in the simulation.
 */
public class Musician extends Human {
    
    public Musician(String name, int age){
        super(name, age);
    }

    /**
     * This method plays music  based on user preferences.
     * @return music
     */
    private String playMusic(){
        return "\nViva la música!\nChararararaan!\n";
    }

    @Override
    public String toString(){
        return super.toString() + this.playMusic();
    }
}