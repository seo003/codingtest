package swJava;

import java.util.Scanner;

public class p7272 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		scanner.nextLine(); //nextInt 다음 nextLine하면 오류남 -> 엔터를 입력받음............그래서 추가해야댐(\n 제거)
		for (int i=0; i<T; i++) {
			String compares = scanner.nextLine();
			String[] compare = compares.split(" ");
			String left = compare[0];
			String right = compare[1];
			
			if (left.length() != right.length()) {
				System.out.printf("#%d DIFF\n", i+1);
				continue;
			}
			String result = "";
			String noCircle = "CEFGHIJKLMNSTUVWXYZ";
			String oneCircle = "ADOPQR";
			for (int j=0; j<left.length(); j++) {
				if (noCircle.indexOf(left.charAt(j)) != -1 && noCircle.indexOf(right.charAt(j)) != -1) {
                    result = "SAME";
				} else if (oneCircle.indexOf(left.charAt(j)) != -1 && oneCircle.indexOf(right.charAt(j)) != -1) {
                    result = "SAME";
				} else if (left.charAt(j) == 'B' && right.charAt(j) == 'B') {
					result = "SAME";
				} else if (left.charAt(j) == 'B' && right.charAt(j) != 'B') {
					result = "DIFF";
					break;
				} else if (left.charAt(j) != 'B' && right.charAt(j) == 'B') {
					result = "DIFF";
					break;
				}else {
					result = "DIFF";
					break;
				}
				
			}
			System.out.printf("#%d %s\n", i+1, result);
		}
	}
}
