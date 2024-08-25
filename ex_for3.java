import java.util.Scanner;

public class ex_for3 {
    public static void main(String[] args) {
       Scanner a=new Scanner(System.in);
       System.out.println("กรุณากรอกจำนวนคน"); 
       int x=a.nextInt();
        int score[]=new int[x+1];
        for(int i=1;i<=x;i++){
            System.out.print("ระบุคะเเนนครั้้งที่"+(i)+"-->");
            score[i]=a.nextInt();}
            for(int i=1;i<=x;i++){
                System.out.println("คะเเนนคนที่"+(i)+"คือ"+score[i]);
        }
    }
}
