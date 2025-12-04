# -*- coding: utf-8 -*-
import sys
import time
import os

# O desenho do coração original mantido
__HEART__ = '''

          @@@@@@@@@@@                @@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@@@@@@@@@@@@
                   @@@@@@@@@@@@@@@@@@@@
                       @@@@@@@@@@@@
                            @@

'''

class Color:
    # Cores para deixar o terminal bonito
    RED = '\x1b[0;31;40m'
    BOLD_YELLOW = '\x1b[1;33;40m'
    CYAN = '\x1b[1;36;40m' # Adicionei uma cor nova (Ciano/Azul claro)
    NORMAL = '\x1b[0m'

def limpar_tela():
    # Comando para limpar a tela dependendo do sistema (Windows ou Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar_lento(texto, atraso=0.04):
    """
    Função que imprime o texto letra por letra para criar animação.
    """
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print() # Pula uma linha no final

class Valentine:
    def __init__(self, name):
        self.loved_one = name

    def romanticize(self):
        # Lógica original para preencher o coração com o nome
        you_in_my_heart = __HEART__
        
        # Cria uma lista cíclica com as letras do nome
        name_list = list(self.loved_one)
        len_name = len(name_list)
        count = 0

        # Substitui cada @ por uma letra do nome
        while '@' in you_in_my_heart:
            you_in_my_heart = you_in_my_heart.replace('@', name_list[count % len_name], 1)
            count += 1

        return you_in_my_heart

    def show_love(self):
        limpar_tela()
        
        # 1. Introdução com efeito de digitação
        print(Color.NORMAL)
        digitar_lento(f"olá, meu amor...", 0.1)
        time.sleep(1)
        digitar_lento("hoje fui fazer um exame que mostra meu coracao como esta.", 0.08)
        time.sleep(1)
        digitar_lento("vou mostrar ele pra vccccc.", 0.08)
        time.sleep(1)
        
        # 2. Mostrar o coração colorido
        cora_preenchido = self.romanticize()
        print(Color.RED + cora_preenchido + Color.NORMAL)
        time.sleep(0.5)

        # 3. Mensagem Final
        mensagem_final = f"conseguiu perceber o {Color.RED}nome{Color.NORMAL} que esta dentro dele?????"
        digitar_lento(mensagem_final, 0.05)
        mensagem_final = f"exatamente, esta escrito {Color.RED}{self.loved_one}{Color.NORMAL} pq vc eh a pessoa mais importante do mundo pra mim!"
        digitar_lento(mensagem_final, 0.05)
        mensagem_final = f"eu te amo muito, {Color.RED}minha princesa{Color.NORMAL} obrigado por ser tao incrivel!"
        digitar_lento(mensagem_final, 0.05)
        
        # 4. Poema ou frases extras (Podes editar aqui!)
        print("\n" + Color.RED + "algumas coisas que eu queria te dizer..." + Color.NORMAL + "\n" )
        frases = [
            "você é o meu código favorito.",
            "sem bugs, apenas amor (isso foi horrivel kkkk).",
            "mas falando sério agora...",
            "você me faz MUITO feliz.",
            "desde que você chegou, tudo ficou melhor.",
            "o seu sorriso é a minha coisa favorita no mundo.",
            "prometo te fazer feliz todos os dias.",
            "obrigado por ser exatamente quem você é.",
            "sei que passo longe de ser perfeito.",
            "mas eu te amo muito, hoje e sempre.",
            "e não vejo a hora de te ver de novo.",
            "<3"
        ]
        
        for frase in frases:
            time.sleep(1)
            digitar_lento(" -> " + frase)

def main():
    # Tenta pegar o nome via argumento, senão pergunta
    try:
        if len(sys.argv) > 1:
            name = sys.argv[1]
        else:
            # Pergunta o nome se não for fornecido
            limpar_tela()
            name = input("Digite o nome da sua namorada: ")
            if not name: name = "Meu Amor" # Nome padrão
    except:
        name = 'Love'

    my_beloved = Valentine(name)
    my_beloved.show_love()

if __name__ == '__main__':
    main()