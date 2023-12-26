public class Triangle {
    public static void main (String[] args) {
       System.out.println(classifyTriangle(3, 4, 5));  // Output: Right-angled
       System.out.println(classifyTriangle(5, 5, 5));  // Output: Equilateral
       System.out.println(classifyTriangle(4, 4, 6));  // Output: Isosceles
       System.out.println(classifyTriangle(7, 8, 10)); // Output: Right-angled
       System.out.println(classifyTriangle(1, 2, 3));  // Output: Not a valid triangle
    }

    public static String classifyTriangle(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0){
            return "Not a valid triangle";
        }

        if (a == b && b == c) {
            return "Equilateral";
        } else if ((a * a + b * b == c * c) || (a * a + c * c == b * b) || (b * b + c * c == a * a)) {
            return "Right-angled";
        } else if (a != b && b != c && a != c) {
            return "Scalene";
        } else {
            return "Isosceles";
        }
    }
}