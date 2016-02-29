package arrays;

public class Evenfibonacci {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum = 0;
		int [] ab = new int [30];
		ab[0] = 1;
		ab[1] = 2;
		for (int i = 2; i < ab.length; i++)
		{
			ab[i] = ab[i-1] + ab[i-2];
		}
		for ( int i = 0; i < ab.length; i++)
		{
			if (ab[i] < 4000000)
			{
			System.out.printf("%d%n", ab[i]);
			}
			if (ab[i] % 2 == 0)
			{
				sum = sum + ab[i];
			}
		}
		System.out.println("sum = " + sum);
	}
}