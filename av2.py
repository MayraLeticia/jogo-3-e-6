from random import randint

rodadas = 1
pontos = 0
contador = []

#apresentação
print("Jogo 3 ou 6")
print("Obtenha a maior pontuação possível!")

print("Regras:\n. O jogador pode rolar o dado quantas vezes quiser dentro de uma mesma rodada.\nSe ao rolar o dado der o valor “3”, você perde todos os pontos obtidos na rodada atual e a rodada atual acaba.\nSe ao rolar o dados sair o valor “6”, o jogador tem sua pontuação dobrada.\nO jogo acontece em 4 rodadas.")

print("Divirta-se")

#primeira rodada
if rodadas == 1:
    resposta = int(input("Deseja começar o jogo?\n1 - Sim\n2 - Não\n_"))

    if resposta == 1:
        print("Rodada {}!".format(rodadas))
        print("Rolando os dados...")
        dado = randint(1,6)

        if dado == 3:
            pontos = 0
            print("Os dados deram {}! Que pena...".format(dado))
            print("Seus pontos foram zerados.")

            rodadas = rodadas + 1
            contador.append(pontos)
            pontos = 0
            print("A rodada acabou.")
            print("________________________________________")

            print("Rodada {}!".format(rodadas))
        elif dado == 6:
            if pontos == 0:
                pontos = pontos * 2
                print("Os dados deram {}!".format(dado))
                print("Seus pontos foram dobrados! Seus pontos são {}. Haha!".format(pontos))
            else:
                pontos = pontos * 2
                print("Os dados deram {}! Parabéns!!".format(dado))
                print("Seus pontos foram dobrados! Seus pontos são {}.".format(pontos))
        else:
            pontos = pontos + dado
            print("Os dados deram {}!".format(dado))
            print("Seus pontos são {}.".format(pontos))

        while rodadas < 4:
            resposta = int(input("O que deseja?\n1 - Rolar o dado.\n2 - Manter meus pontos e acabar a rodada.\n_"))

            if resposta == 1:
                print("Rolando os dados...")
                dado = randint(1,6)

                if dado == 3:
                    pontos = 0
                    print("Os dados deram {}! Que pena...".format(dado))
                    print("Seus pontos foram zerados.")

                    rodadas = rodadas + 1
                    contador.append(pontos)
                    pontos = 0
                    print("A rodada acabou.")
                    print("________________________________________")

                    print("Rodada {}!".format(rodadas))
                elif dado == 6:
                    if pontos == 0:
                        pontos = pontos * 2
                        print("Os dados deram {}!".format(dado))
                        print("Seus pontos foram dobrados! Seus pontos são {}. Haha!".format(pontos))
                    else:
                        pontos = pontos * 2
                        print("Os dados deram {}! Parabéns!!".format(dado))
                        print("Seus pontos foram dobrados! Seus pontos são {}.".format(pontos))
                else:
                    pontos = pontos + dado
                    print("Os dados deram {}!".format(dado))
                    print("Seus pontos são {}.".format(pontos))
            elif resposta == 2:
                rodadas = rodadas + 1
                contador.append(pontos)
                pontos = 0
                print("A rodada acabou.")
                print("________________________________________")

                print("Rodada {}!".format(rodadas))
            else:
                print("Entrada inválida. Tente de novo, selecionando 1 OU 2.")
                print("________________________________________")

        if rodadas == 4:
            resposta = int(input("O que deseja?\n1 - Rolar o dado.\n2 - Manter meus pontos e acabar a partida.\n_"))

            if resposta == 1:
                print("Rolando os dados...")
                dado = randint(1,6)

                if dado == 3:
                    pontos = 0
                    print("Os dados deram {}! Que pena...".format(dado))
                    print("Seus pontos foram zerados.")

                    rodadas = rodadas + 1
                    contador.append(pontos)
                    pontos = 0
                    print("A rodada acabou.")
                    print("________________________________________")
                elif dado == 6:
                    if pontos == 0:
                        pontos = pontos * 2
                        print("Os dados deram {}!".format(dado))
                        print("Seus pontos foram dobrados! Seus pontos são {}. Haha!".format(pontos))
                    else:
                        pontos = pontos * 2
                        print("Os dados deram {}! Parabéns!!".format(dado))
                        print("Seus pontos foram dobrados! Seus pontos são {}.".format(pontos))
                else:
                    pontos = pontos + dado
                    print("Os dados deram {}!".format(dado))
                    print("Seus pontos são {}.".format(pontos))
                while rodadas < 4:
                    resposta = int(input("O que deseja?\n1 - Rolar o dado.\n2 - Manter meus pontos e acabar a rodada.\n_"))

                    if resposta == 1:
                        print("Rolando os dados...")
                        dado = randint(1,6)

                        if dado == 3:
                            pontos = 0
                            print("Os dados deram {}! Que pena...".format(dado))
                            print("Seus pontos foram zerados.")

                            rodadas = rodadas + 1
                            contador.append(pontos)
                            pontos = 0
                            print("A rodada acabou.")
                            print("________________________________________")

                            print("Rodada {}!".format(rodadas))
                        elif dado == 6:
                            if pontos == 0:
                                pontos = pontos * 2
                                print("Os dados deram {}!".format(dado))
                                print("Seus pontos foram dobrados! Seus pontos são {}. Haha!".format(pontos))
                            else:
                                pontos = pontos * 2
                                print("Os dados deram {}! Parabéns!!".format(dado))
                                print("Seus pontos foram dobrados! Seus pontos são {}.".format(pontos))
                        else:
                            pontos = pontos + dado
                            print("Os dados deram {}!".format(dado))
                            print("Seus pontos são {}.".format(pontos))
                    elif resposta == 2:
                        rodadas = rodadas + 1
                        contador.append(pontos)
                        pontos = 0
                        print("A rodada acabou.")
                        print("________________________________________")

                        print("Rodada {}!".format(rodadas))
                    else:
                        print("Entrada inválida. Tente de novo, selecionando 1 OU 2.")
                        print("________________________________________")
            elif resposta == 2:
                rodadas = rodadas + 1
                contador.append(pontos)
                pontos = 0
                print("A rodada acabou.")
                print("________________________________________")
            else:
                print("Entrada inválida. Tente de novo, selecionando 1 OU 2.")
                print("________________________________________")
        if sum(contador) == 0:
            print("Fim de jogo!")
            print("Você conseguiu {} pontos... Que pena...".format(sum(contador)))

            print("________________________________________")
        else:
            print("Fim de jogo!")
            print("Você conseguiu {} pontos! Parabéns!".format(sum(contador)))

            print("________________________________________")
    elif resposta == 2:
        print("Ok, então até a proxima!")
        print("________________________________________")
    else:
        print("Entrada inválida. Tente de novo, selecionando 1 OU 2.")
        print("________________________________________")

