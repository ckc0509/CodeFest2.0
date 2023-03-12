import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Orchard {
    int[] prices_perkg, days, perkg_fruits, per_bourn, profit, planted, bourn_fruit, total_fruits, total_kg, greed;
    public Orchard() {
        prices_perkg = new int[] { 150, 250, 100, 50, 1600 };
        days = new int[] { 10, 6, 15, 5, 15 };
        perkg_fruits = new int[] { 5, 7, 8, 10, 15 };
        per_bourn = new int[] { 400, 280, 2200, 1500, 75 };
        planted = new int[] { 1, 1, 1, 1, 1 };
        profit = new int[5];
        bourn_fruit = new int[5];
        total_fruits = new int[5];
        total_kg = new int[5];
        greed = new int[5];
    }

    public static void main(String[] args) throws java.lang.Exception {
		FileWriter fw = new FileWriter("TOF_smallOutput.txt");
		Scanner sc = new Scanner(new File("TOF_small.txt"));
        int N = Integer.parseInt(sc.nextLine());
		for(int i=1;i<=N;++i)
		{
			String[] str = sc.nextLine().split("\t");
			int n = Integer.parseInt(str[0]);
			int gd = Integer.parseInt(str[1]);
			long profit = new Orchard().maximumProfit(n,gd);
			fw.write("Case #" + i + ": " + Long.toString(profit) + "\n");
		}
		fw.close();
        //System.out.println(orc.maximumProfit(22,29));

    }

    public long maximumProfit(int n, int gd) {
        for (int i = 0; i < 5; i++)
            bourn_fruit[i] = gd / days[i];
        for (int i = 0; i < 5; i++)
            greed[i] = ((bourn_fruit[i] * per_bourn[i]) / (perkg_fruits[i])) * prices_perkg[i];

        int[] temp = Arrays.copyOf(greed, 5);
        Arrays.sort(temp);
        int pyt[] = new int[5];
		
        int pr = 1;
		//System.out.println(Arrays.toString(greed));
        for (int i = 4; i >= 0; i--) {
            int req = temp[i];
            for (int j = 0; j < 5; j++) {
                if (greed[j] == req) {
                    pyt[j] = pr;
					greed[j] = 0;
                    pr++;
                    break;
                }
            }
        }
		//System.out.println(Arrays.toString(pyt));
        StringBuilder ss = new StringBuilder();
        for (int i = 0; i < 5; i++)
            ss.append(pyt[i]);
		//System.out.println(ss);
        int mx1 = (int) Math.floor(n * 0.4);
        int mx2 = (int) Math.floor(n * 0.4);
        int mx3 = (int) Math.floor(n * 0.4);
        int mx4 = (int) Math.floor(n * 0.4);
        n -= 5;
        int first = ss.indexOf("1");
        int second = ss.indexOf("2");
        int third = ss.indexOf("3");
        int fourth = ss.indexOf("4");
        int fifth = ss.indexOf("5");

        while (n > 0) {
            if (mx1 > 1) {
                planted[first]++;
                n--;
                mx1--;
            } else if (mx2 > 1) {
                planted[second]++;
                n--;
                mx2--;
            } else if (mx3 > 1) {
                planted[third]++;
                n--;
                mx3--;
            } else if (mx4 > 1) {
                planted[fourth]++;
                n--;
                mx4--;
            } else {
                planted[fifth]++;
                n--;
            }
        }
        long ans = 0;
        for (int i = 0; i < 5; i++)
            ans += ((bourn_fruit[i] * per_bourn[i] * planted[i]) / perkg_fruits[i]) * prices_perkg[i];
        return ans;
    }
}