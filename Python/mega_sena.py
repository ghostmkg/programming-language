import random

def gerar_jogo_megasena(quantidade_numeros=6):
    """
    Gera um jogo aleatório da Mega-Sena.
    
    Args:
        quantidade_numeros (int): Quantidade de números no jogo (padrão: 6)
        
    Returns:
        list: Lista com os números sorteados em ordem crescente
    """
    if quantidade_numeros < 6 or quantidade_numeros > 15:
        raise ValueError("A Mega-Sena permite jogos de 6 a 15 números.")
    
    numeros = random.sample(range(1, 61), quantidade_numeros)
    return sorted(numeros)

def formatar_jogo(numeros):
    """Formata os números do jogo para exibição."""
    return " - ".join([f"{num:02d}" for num in numeros])

def calcular_preco(quantidade_numeros):
    """Calcula o preço aproximado do jogo baseado na quantidade de números."""
    precos = {
        6: 5.00,
        7: 35.00,
        8: 140.00,
        9: 420.00,
        10: 1050.00,
        11: 2310.00,
        12: 4620.00,
        13: 8580.00,
        14: 15015.00,
        15: 25025.00
    }
    return precos.get(quantidade_numeros, 0)

def main():
    print("=" * 50)
    print("GERADOR DE JOGOS DA MEGA-SENA")
    print("=" * 50)
    print()
    
    while True:
        try:
            qtd = input("Quantos números deseja jogar? (6 a 15, ou Enter para 6): ").strip()
            
            if qtd == "":
                qtd_numeros = 6
            else:
                qtd_numeros = int(qtd)
            
            if qtd_numeros < 6 or qtd_numeros > 15:
                print("❌ Quantidade inválida! Escolha entre 6 e 15 números.\n")
                continue
            
            break
        except ValueError:
            print("❌ Por favor, digite um número válido.\n")
    
    print()
    qtd_jogos = 1
    
    try:
        resp = input("Quantos jogos deseja gerar? (padrão: 1): ").strip()
        if resp:
            qtd_jogos = int(resp)
    except ValueError:
        qtd_jogos = 1
    
    print("\n" + "=" * 50)
    print(f"SEUS JOGOS DA MEGA-SENA ({qtd_numeros} números)")
    print("=" * 50)
    print()
    
    for i in range(qtd_jogos):
        jogo = gerar_jogo_megasena(qtd_numeros)
        print(f"Jogo {i+1:02d}: {formatar_jogo(jogo)}")
    
    preco_total = calcular_preco(qtd_numeros) * qtd_jogos
    print()
    print("=" * 50)
    print(f"Valor aproximado: R$ {preco_total:.2f}")
    print("=" * 50)
    print()
    print("🍀 Boa sorte! 🍀")

if __name__ == "__main__":
    main()