public class Engine {

    private String type;
    private int potency;

    public Engine(String type, int potency){
        this.type = type;
        this.potency = potency;
    }

    public String info(){
        return "The engine is a " + this.type + " of " + 
                this.potency + " HP.";
    }
    
}
