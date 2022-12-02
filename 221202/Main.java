
class Test {
    int help(int a, int b) {  // a, b 는 매개변수
        return a + b;
    }

}

class Updater{
    void update(Counter counter){
        counter.count++;
    }
}


class Counter{
    int count = 0;

}
public class Main{
    public static void main(String[] args) {
        Counter myCounter = new Counter();
        System.out.println(myCounter.count);
        Updater myUpdater = new Updater();
        myUpdater.update(myCounter);
        System.out.println(myCounter.count);
    }

}