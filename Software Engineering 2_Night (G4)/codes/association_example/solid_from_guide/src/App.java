import java.util.List;
import java.util.ArrayList;

public class App {

    public static void main(String[] args) throws Exception {
        List<Human> population = new ArrayList<Human>();

        population.add(new ComputerEngineer("Pepito", 50, "FrontEnd"));
        population.add(new Doctor("Pepita", 20, "Pediatric"));
        population.add(new Musician("Juanita", 30)); 
        population.add(new ComputerEngineer("Sutanita", 34, "BackEnd"));

        // Liskov Substitution
        for(Human h: population){
            System.out.println(h);
        }
    }

}
