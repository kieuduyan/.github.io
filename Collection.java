
package collection;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;
import java.util.Iterator;
public class Collection {
    public static void main(String[] args) {
        Set<Double> BiensetDouble = new TreeSet<Double>();
        BiensetDouble.add(10.8d);
        BiensetDouble.add(1.2d);
        BiensetDouble.add(1d);
        BiensetDouble.add(0.99d);
        Iterator<Double> BienIterator = null;
        System.out.println("Cá phần tử trong BiensetDouble");
        BienIterator = BiensetDouble.iterator();
        while(BienIterator.hasNext()) {
            System.out.println(BienIterator.next());   
            
        }
        
    }
    
}
