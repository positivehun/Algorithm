
class Animal{
    String name;

    void setName(String name){
        this.name = name;
    }
    void sleep(){
        System.out.println(this.name + "zzzanimal");

    }
}

class Dog extends Animal{
    String nextname;

    void setNextname(String nextname){
        this.nextname = nextname;
    }
    void sleep(){
        System.out.println(this.name + "zzzdog");

    }

}

class Bigdog extends Dog{
    Bigdog(String name){
        this.setName(name);
    }

    void sleep(){
        System.out.println(this.name + "zzzabigdog");

    }


}
public class ExtendSample {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Bigdog bigdog = new Bigdog("haroo");
        Animal animal = new Animal();
        dog.setName("hanui");
        dog.setNextname("harang");
        System.out.println(dog.name);
        System.out.println(dog.nextname);
        dog.sleep();
        bigdog.sleep();

    }

}
