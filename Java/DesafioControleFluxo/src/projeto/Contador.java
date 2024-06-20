package projeto;

import java.util.Scanner;

public class Contador {

	public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		
		System.out.print("Digite o primeiro valor: ");
		
		int primeiroValor = ler.nextInt();
		
		System.out.print("Digite o segundo valor: ");
		
		int segundoValor = ler.nextInt();		
		
		try {
			contar(primeiroValor, segundoValor);
		}catch(Exception e) {
			System.out.println("Invalido! O primeiro valor deve ser MENOR que o segundo!");
		}
		
	}
	
	static void contar(int a, int b) throws ParametrosInvalidosException{
		
		if (a > b)
			throw new ParametrosInvalidosException();
		
		int contagem = b-a;
		
		for(int i=0; i<contagem; i++) {
			System.out.println("Imprimindo o número " + (i+1));
		}
	}

}
