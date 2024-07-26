package iPhone;
import Apps.Browser;
import Apps.MusicPlayer;
import Apps.Phone;

public class iPhoneModel implements Browser, MusicPlayer, Phone{
	
	private int abas = 1;
	private boolean player = false;
	private String musica;
	private boolean emChamada = false;
	
	//BROWSER METHODS
	public void exibirPagina() {
		System.out.println("EXIBINDO PAGINA VIA IPHONE");
	}
	public void adicionarNovaAba(){
		this.abas += 1;
		System.out.println("NOVA ABA ABERTA");
	}
	public void numeroAbas() {
		//System.out.println("Abas abertas: " + this.abas);
		System.out.println(String.format("ABAS ABERTAS: %d", this.abas));
	}
	public void atualizarPagina(){
		System.out.println("PAGINA ATUALIZADA");
	}
	
	//MUSICPLAYER METHODS
	public void tocar() {
		//Verificando se o player está desligado. Se estiver, liga
		if(this.emChamada)
			System.out.println("NAO E POSSIVEL LIGAR O PLAYER. ATUALMENTE EM CHAMADA");
		
		if(!this.player && !emChamada) {
			this.player = true;
			
			System.out.println("PLAYER LIGADO");
			
			try {
				System.out.println(String.format("TOCANDO '%s'", this.musica.toUpperCase()));
				}catch(NullPointerException e) {
					System.out.println("NENHUMA MUSICA SELECIONADA");
				}
		}
	
	}
	public void pausar(){
		//Verifica se o player está ligado. Se estiver, desliga.
		if(this.player)
			this.player = false;
		System.out.println("PLAYER PAUSADO");
	}

	
	public void selecionarMusica(String musica) {
		System.out.println(String.format("MUSICA SELECIONADA: '%s'", musica.toUpperCase()));
		this.musica = musica;
	}	
	
	//PHONE METHODS	
	public void ligar(String numero) {
		if(!this.emChamada) {
			System.out.println("LIGANDO PARA " + numero);
		this.emChamada = true;
		this.player = false;
	}	else
			System.out.println("JA POSSUI UMA CHAMADA ATIVA");
	}
	public void atender() {
		if(!emChamada) {
			System.out.println("ATENDENDO LIGACAO");
			this.player = false;
			this.emChamada = true;
		}else
			System.out.println("NAO E POSSIVEL ATENDER LIGACAO. ATUALMENTE EM CHAMADA");
	}
	public void desligar() {
		this.emChamada = false;
		System.out.println("LIGACAO ENCERRADA");
	}
	public void iniciarCorreioVoz() {
		System.out.println("INICIANDO CORREIO DE VOZ");
	}

}
