/*
 * This class is the entry point to execute the application.
 * 
 * Author: Carlos Andres Sierra <casierrav@unal.edu.co>
 */

import java.util.List;
import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        List<Human> population = new ArrayList<>();

        population.add(new Human("Don Ramon", 40));
        population.add(new Doctor("Strange", 35, "Mystical Arts"));
        population.add(new Engineer("Tony Stark", 40, 2));
        population.add(new Engineer("Linus Torvals", 60, 10));
        population.add(new Doctor("Chapatin", 60, " cardiology"));

        for(Human h: population){
            h.whoIAm();
        }
    }
}
