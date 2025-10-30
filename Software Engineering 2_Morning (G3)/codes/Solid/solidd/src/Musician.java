public class Musician extends Human implements IArtist {

    public Musician(String name, int age) {
        super(name, age);
    }

    @Override
    public String makeArt() {
        return "I make: chararara!";
    }

    @Override
    public int askMoney() {
        return 20;
    } 

    @Override
    public void whoIAm(){
        System.out.println("My name is " + this.name + 
        ", don't ask my age. " + this.makeArt() + 
        ". For my art you will pay me " + this.askMoney() + "$.");
    }
}
