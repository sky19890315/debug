package Factory;

/**
 * Created by sunkeyi on 2017/9/30.
 */
public class Circle implements Shape {

    @Override
    public void draw() {
        System.out.println("Inside Factory.Circle::draw() method.");
    }
}
