import java.util.Scanner;

public class array1 {
    public static void main(String[] args) {
        Scanner scn =new Scanner(System.in);
        int a =scn.nextInt(); 
        System.out.println("คะเเนนชุดที่ 1 ลำดับที่ 1 คือ");      
        int b =scn.nextInt(); 
        System.out.println("คะเเนนชุดที่ 1 ลำดับที่ 2 คือ");      
        int c =scn.nextInt(); 
        System.out.println("คะเเนนชุดที่ 2 ลำดับที่ 1 คือ");      
        int d =scn.nextInt(); 
        System.out.println("คะเเนนชุดที่ 2 ลำดับที่ 2 คือ");      
        int e =scn.nextInt(); 
        System.out.println("คะเเนนชุดที่ 3 ลำดับที่ 1 คือ");      
        int f =scn.nextInt(); 
        System.out.println("คะเเนนชุดที่ 3 ลำดับที่ 2 คือ"); 
        int[][]number=new int[3][2];
            number[0][0]=a;
            number[0][1]=b;
            number[1][0]=c;
            number[1][1]=d;
            number[2][0]=e;
            number[2][1]=f;
    System.out.println("คะเเนนชุดที1 ลำดับที่ 1 คือ"+number[0][0]);
    System.out.println("คะเเนนชุดที1 ลำดับที่ 2 คือ"+number[0][1]);
    System.out.println("คะเเนนชุดที2 ลำดับที่ 1 คือ"+number[1][0]);
    System.out.println("คะเเนนชุดที2 ลำดับที่ 2 คือ"+number[1][1]);
    System.out.println("คะเเนนชุดที3 ลำดับที่ 1 คือ"+number[2][0]);
    System.out.println("คะเเนนชุดที3 ลำดับที่ 2 คือ"+number[2][1]);    
    }
}
