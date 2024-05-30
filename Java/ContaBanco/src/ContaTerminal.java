import java.util.Scanner;   //Recurso para ler entrada de dados pelo usuário
import java.util.Locale;    //Utilizado para permitir o separador de milhar padrão EUA, o " . "

/**Simulação simples de um terminal bancário na abertura de uma nova conta.
 * Projeto proposto pelo Bootcamp da DIO em parceiria com a Santander
 * @author Kevin Johnny
 * @since Maio, 2024
*/

public class ContaTerminal{

    public static void main(String [] args){
        Scanner ler = new Scanner(System.in).useLocale(Locale.US);
        int numeroConta;
        String agencia;
        String nomeCliente;
        double saldo;

        System.out.println("Boas vindas ao nosso banco!");
        System.out.println("Por favor, informe seu nome: ");
        nomeCliente = ler.nextLine();

        System.out.println("Número da conta: ");
        numeroConta = ler.nextInt();

        System.out.println("Informe sua agência: ");
        agencia = ler.next();

        System.out.println("Deposite um valor para validar sua conta: ");
        saldo = ler.nextDouble();
        System.out.println("Valor de " + saldo + " depositado com sucesso!");

        System.out.println("Olá " + nomeCliente + 
        ", obrigado por criar uma conta em nossso banco, sua agencia é " + agencia + 
        ", conta " + numeroConta + " e seu saldo " + saldo + " já está disponível");

    }

}