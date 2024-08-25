import java.util.Scanner;
public class arra {
    public static void main(String[] args) {
        Scanner kb=new Scanner(System.in);
        String name[]=new String[5];
        for(int i=0;i<=4;i++){
            System.out.println("ระบุคะเเนน"+(i+1)+"-->");
            name[i]=kb.next();
    }
        for(int i=0;i<=4;i++){
            System.out.println("คะเเนนคนที่"+(i+1)+":"+name[i]);
        }
    }
}

