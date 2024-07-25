package iPhone;


public class MyiPhone {

	public static void main(String[] args) {
		iPhoneModel iPhone = new iPhoneModel();
		
		//BROWSER METHODS
		
		iPhone.adicionarNovaAba();
		iPhone.numeroAbas();
		iPhone.exibirPagina();
		iPhone.atualizarPagina();
		
		//MUSICPLAYER METHODS
		iPhone.tocar();
		iPhone.pausar();
		iPhone.selecionarMusica("a music");
		iPhone.tocar();
		
		//PHONE METHODS	
		

		iPhone.ligar("+55(00) 99999-9999");
		iPhone.atender();
		iPhone.tocar();
		iPhone.desligar();
		iPhone.atender();
		iPhone.tocar();
		iPhone.desligar();
		iPhone.tocar();
		
	}

}
