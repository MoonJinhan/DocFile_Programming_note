
public class Casting {
	public static void main(String[] args) {
		
		 	double a = 1.1;
	        double b = 1;
	        
	        //�Ǽ��� �ƴϴ��� ������ ���� �ʴ´�.(�ڵ�)
	        double b2 = (double) 1;
	        //������ b�� ���� ����� ��Ÿ������ �������� �Ѵٰ� �����ϸ� �ȴ�.
	        System.out.println(b);
	        //����� 1.0 �Ǽ��� ����� �ȴ�. �� �������� �ȴ�.
	        
	        // int c = 1.1; ����. ���� �ڵ����� �Ǽ��� ������ �ٲ�ٸ�
	        //0.1�� �Ҿ���� ���� �ִ�. �׷��� �̸� �����ϱ� ���ؼ� ����.
	        //�̸� "�ս�"�̶�� �θ���.
	        
	        System.out.println(b2);
	        //
	        int e = (int) 1.1;
	        //��Ƽ��(����)�ε� ������ ����� ��Ÿ���ڴٴ�. �� �� ������ �ۼ�.
	        System.out.println(e);
	         
	        // 1 to String 
	        String f = Integer.toString(1);
	        System.out.println(f.getClass());
	 
	 
	}

}
