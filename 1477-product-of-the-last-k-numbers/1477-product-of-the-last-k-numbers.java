import java.util.*;
class ProductOfNumbers {

    List<Integer> arr;
    public ProductOfNumbers() {
        this.arr = new ArrayList<>();
    }
    
    public void add(int num) {
        arr.add(num);
    }
    
    public int getProduct(int k) {
        int result = 1;
        int start = arr.size() - k ;
        for(; k > 0; k--)
        {
            // System.out.println(start+" "+k);
            result *= this.arr.get(start);
            start += 1;
        }
        // System.out.println("Thsats sll");
        return result;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */