# 🎮 Tetris em Python com Pygame

Este é um projeto de recriação do clássico jogo **Tetris**, desenvolvido em Python utilizando a biblioteca **Pygame**. O jogo conta com interface gráfica, controle de pontuação, persistência em arquivo JSON e sistema de logs via mixin (`MixinLogRoute`) para rastrear chamadas de rota, método e função.

## 🧩 Funcionalidades

* ✔️ Movimento e rotação de peças (tetrominós)
* ✔️ Queda automática das peças com aceleração (`down`)
* ✔️ Detecção de linhas completas e pontuação
* ✔️ Sistema de **highscore** (maior pontuação salva localmente em `score.json`)
* ✔️ Logs formatados usando **MixinLogRoute** (`mixinlog.py`)
* ✔️ Animações básicas e UI simples
* ✔️ Controle via teclado (setas)

## 🖥️ Tecnologias utilizadas

* **Python 3.10+**
* **Pygame**
* **JSON** (para salvar scores)
* **Programação Orientada a Objetos (POO)**

## ⚙️ Estrutura de arquivos

```
seu-repositorio/
├── main.py           # Loop principal do jogo (inicia App e Tetris)
├── tetris.py         # Lógica de jogo, controle de fluxo e pontuação
├── tetromino.py      # Classe Tetromino: movimento, rotação e colisão
├── mixinlog.py       # MixinLogRoute: herança e polimorfismo para logs
├── settings.py       # Constantes e configurações
├── score.json        # Arquivo onde os scores são salvos
└── assets/
    └── font/
        └── playgumregular.ttf  # Fonte utilizada no jogo
```

## 🎮 Controles

* ◀️ **Seta Esquerda** – mover para a esquerda
* ▶️ **Seta Direita** – mover para a direita
* 🔽 **Seta Baixo** – acelerar descida
* 🔼 **Seta Cima** – rotacionar peça

## 📈 Pontuação

A pontuação aumenta conforme o número de linhas eliminadas:

* 1 linha: +100 pontos
* 2 linhas: +300 pontos
* 3 linhas: +700 pontos
* 4 linhas: +1500 pontos

O **highscore** é salvo automaticamente em `score.json` e exibido na tela.

## 📝 Logs com MixinLogRoute

Toda vez que uma ação-chave ocorre (movimento, rotação, controle), um objeto de `MixinLogRoute` é instanciado e seu método `mostrar_log()` imprime um bloco de log com:

* **Rota**: identificador do método onde ocorreu
* **Método**: nome da chamada (ex. `move_left`, `rotate_90`, `keydown_left`)
* **Função**: descrição da ação

Isso demonstra **herança** (de `MixinLog`), **polimorfismo** (várias classes usam o mesmo método) e o padrão **mixin** para extensão de funcionalidade.

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

⚠️ **Certifique-se de que a pasta **\`\`**.**

---

Desenvolvido como projeto de estudo com fins educacionais.
