public class App {
    public static void main(String[] args) {
        Engine engine = new Engine("v10", 1050);
        Car fw24 = new Car("Williams", engine);
        System.out.println(fw24);
    }
}
