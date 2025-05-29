
# 🎮 Tetris em Python com Pygame

Este é um projeto de recriação do clássico jogo **Tetris**, desenvolvido em Python utilizando a biblioteca **Pygame**. O jogo conta com interface gráfica, controle de pontuação e **sistema de highscore salvo em arquivo JSON**.

## 🧩 Funcionalidades

- ✔️ Movimento e rotação de peças (tetrominós)
- ✔️ Detecção de linhas completas e pontuação
- ✔️ Sistema de **highscore** (maior pontuação salva localmente)
- ✔️ Animações básicas e UI simples
- ✔️ Controle via teclado (setas)

## 🖥️ Tecnologias utilizadas

- **Python 3.10+**
- **Pygame**
- **JSON** (para salvar scores)
- **Programação Orientada a Objetos (POO)**

## 📂 Estrutura do Projeto

```
📁 seu-repositorio/
├── main.py           # Loop principal do jogo
├── tetris.py         # Lógica do jogo e pontuação
├── tetromino.py      # Peças e movimentação
├── settings.py       # Constantes e configurações
├── score.json        # Arquivo onde os scores são salvos
├── assets/
│   └── font/
│       └── fonte.ttf # Fonte utilizada no jogo
```

## 🎮 Controles

- ◀️ `Seta Esquerda` – mover para a esquerda  
- ▶️ `Seta Direita` – mover para a direita  
- 🔽 `Seta Baixo` – acelerar descida  
- 🔼 `Seta Cima` – rotacionar peça  

## 📈 Pontuação

A pontuação aumenta conforme o número de linhas eliminadas:
- 1 linha: +100 pontos  
- 2 linhas: +300 pontos  
- 3 linhas: +700 pontos  
- 4 linhas: +1500 pontos  

O **highscore** é salvo automaticamente e mostrado na tela.

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/tetris-python.git
cd tetris-python
```

2. Instale as dependências:
```bash
pip install pygame
```

3. Execute o jogo:
```bash
python main.py
```

⚠️ **Certifique-se de que a pasta `assets/font/` contenha a fonte `fonte.ttf`.**

## 💡 Créditos

Desenvolvido como projeto de estudo com fins educacionais.
