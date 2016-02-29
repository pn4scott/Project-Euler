package arrays;

public class Multiplesof3and5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] ab = new int [1000];
		int sum = 0;
		for (int i = 1; i<ab.length; i++ )
		{
			if ((i % 3 == 0) || (i % 5 == 0))
			{
				System.out.printf(" %d%n", i);
				sum = sum + i;
			}
		}
		System.out.printf("sum = %d", sum);
	}
}