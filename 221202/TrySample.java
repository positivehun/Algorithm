class NullTest{
    String value;
    void setValue(String value){
        this.value = value;
    }
    public void test(int a){ //throws NullPointerException{
        if(a==1){
            throw new NullPointerException("1 is null");
        }
        else{
            System.out.println("not 1");
        }
    }

}


public class TrySample {
    public static void main(String[] args) {
        NullTest nullTest = new NullTest();
        try{
            //System.out.println(nullException.A());
            //throw (new NullPointerException());
            nullTest.test(1);

        }catch(NullPointerException e){
            System.out.println("null exception");
        }catch(ArithmeticException ex){
            System.out.println("Arith exception");
        }
    }
}


