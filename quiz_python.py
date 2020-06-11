# coding: UTF-8

#variável para seleção de nível de dificuldade do jogo. 
dificuldades_validas = ["facil", "medio", "dificil"]

# variável para controle da dificuldade nas funções.
dificuldade = 'controle'

#variáveis das frases dos 3 níveis de dificuldade e suas respostas. 

frase_facil = '''E melhor ter varias ___1___ especificas do que poucas, longas e complexas. O comando indicado para este processo e o ___2___. Para este projeto, se uma funcao tem mais de 18 ___3___ ela deve ser ___4___ em outras.'''

respostas_facil = ['funcoes', 'def', 'linhas', 'dividida']

frase_medio = '''O ___1___ indica a posicao de um item em uma ___2___. Na linguagem ___3___,
essa estrutura pode conter tanto ___4___ quanto numeros.''' 

respostas_medio = ['indice', 'lista', 'python', 'strings']

frase_dificil =  '''Para criar uma ___1___ usamos def. Entre as possibilidades de uso deste recurso esta o uso do ___2___, que realiza uma atividade enquanto determinada condicao for verdadeira. E necessario fornecer condicoes para interromper o ___3___ criado, para que ele nao seja ___4___. '''

respostas_dificil = ['funcao', 'while', 'loop', 'infinito']

#variável com a pergunta que questiona sobre o teor da lacuna.
pergunta_lacuna = '\nQual a palavra que preenche corretamente a lacuna '

#variável para resposta correta. 
resposta_correta = '\nResposta correta!\n'

# variável com string para resposta incorreta. 
resposta_incorreta = '\nResposta incorreta, tente novamente.'

#variável com a frase que pede ao jogador para selecionar o nível. 
selecao = "Digite um dos niveis de dificuldade (facil, medio ou dificil): "

#variável para seleção inválida de nível 
selecao_invalida = "Opcao invalida. Digite facil, medio ou dificil: "

# função boas-vindas, diz olá ao jogador. 
#def boas_vindas():
#    
  
#função para seleção do nível de dificuldade do jogo. Imprime a frase adequada segundo o nível de dificuldade. 
def pergunta_dificuldade():
    print "\nOla, bem-vindo ao meu jogo!\n"
    dificuldades_validas = ['facil', 'medio', 'dificil']
    dificuldade = raw_input(selecao).lower()
    while dificuldade not in dificuldades_validas:
        dificuldade = raw_input(selecao_invalida).lower()
    print '\nVoce selecionou o nivel ' + dificuldade + '. ''\n\nVamos la!\n'
    dificuldade = 'frase_' + dificuldade
    if dificuldade == 'frase_facil':
        print "A frase e: " + frase_facil
        return frase_facil, respostas_facil
    if dificuldade == 'frase_medio':
        print "A frase e: " + frase_medio
        return frase_medio, respostas_medio
    if dificuldade == 'frase_dificil':
        print "A frase e: " + frase_dificil
        return frase_dificil, respostas_dificil
# a funcao da como retorno a frase a ser usada e a lista de respostas correspondente para serem os inputs da funcao seguinte. 

frase_escolhida, lista_respostas_escolhida = pergunta_dificuldade()

# o nivel selecionado na funcao anterior e usado para o jogo - a frase_escolhida indica a frase que será usada e listas_respostas_escolhida
#indica a lista com as respectivas respostas.

def jogar (frase_escolhida, lista_respostas_escolhida):
    #como temos 4 lacunas o numero de respostas e 4
    numero_respostas = 4
    #temos 4 lacuna, então o total de respostas sera 4.
    numero_respostas_corretas = 0
    # loop indica que é preciso 4 respostas corretas para terminar o jogo. 
    while numero_respostas_corretas < numero_respostas:		

        resposta_usuario = raw_input(pergunta_lacuna + str(numero_respostas_corretas + 1) + "? ")
        #se a resposta inserida esta correta o jogo passa para a proxima lacuna. 
        if resposta_usuario == lista_respostas_escolhida[numero_respostas_corretas]:
            print resposta_correta
            #se a resposta estiver correta o jogo imprime a frase substituindo a lacuna pela resposta
            frase_escolhida = frase_escolhida.replace("___" + str(numero_respostas_corretas + 1) +"___", resposta_usuario)
            print frase_escolhida
            numero_respostas_corretas = numero_respostas_corretas + 1
        else:
            # mensagem exibida em caso de resposta incorreta. 
            print resposta_incorreta
    # se o numero de respostas corretas for igual ao total, o jogo acaba.    
    if numero_respostas_corretas == numero_respostas:
        #mensagens finais do jogo
        print "\nParabens, voce acertou! =)\nGame over." 

#função que chama as outras funções para começar o jogo. 		
def boas_vindas():
    frase_escolhida, lista_respostas_escolhida = pergunta_dificuldade()
    jogar(frase_escolhida, lista_respostas_escolhida)

boas_vindas()

