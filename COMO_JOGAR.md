# 🕵️ Xylo's Hideout - Guia de Mecânicas e Arquitetura do Jogo

Este documento detalha o funcionamento interno, as regras e a estrutura mecânica da versão atual do **Xylo's Hideout - Escape Room v4.0**.

---

## 🎮 1. Visão Geral do Jogo
**Gênero:** Escape Room Cooperativo / Point & Click  
**Câmera:** Visualização Fixa 2.5D (com inspeções de itens 3D)  
**Rede:** Multiplayer P2P Integrado (PeerJS) sem necessidade de servidor centralizador.

O jogo simula a sala secreta do laboratório/esconderijo de *Xylo*. O objetivo é explorar cooperativamente os cantos do cenário em busca de pistas escondidas que culminam em quebra-cabeças.

---

## 🧠 2. Mecânicas Centralizadas

### 🖱️ Sistema Point and Click (Hotspots Invisíveis)
O cenário principal (`hideout_background.png`) é uma grande pintura (matte-painting) estática de proporção 1920x1080.
A interatividade acontece através de **Hotspots** — uma teia invisível de polígonos gráficos desenhados por cima das cordenadas exatas da imagem. Ao passar o mouse e clicar nessas coordenadas, os eventos centrais do jogo são engatilhados.

**Pontos de Interesse Interativos Atuais:**
- `Pergaminho:` Fica sobre a mesa. Revela textos.
- `Lupa:` Item equipável na mesa.
- `Lanterna:` Item deixado no chão ou estante.
- `Fenda na Parede:` Usada para inspecionar falhas na estrutura.
- `Olho / Placa:` Possíveis trancas e dicas crípticas localizadas no cenário.

### 🎒 Inventário Modular
Ao contrário de jogos clássicos onde tudo é jogado num baú só, o inventário é inteligente e separa o tipo de descoberta do jogador em categorias lógicas:
1. **🛠️ Ferramentas:** Itens como *Lupa* e *Lanterna*. Quando equipados, eles podem de fato alterar o ponteiro do seu mouse para uma `lens-cursor` ou criar um facho de luz dinâmico na tela para "escanear" coisas invisíveis.
2. **📜 Pistas:** Itens como *Pergaminhos* contendo enigmas de texto que vão para o seu bloco de notas invisível.
3. **💎 Loot:** Recompensas, chaves ou conquistas como Moedas Sol/Onyx (`coin.png`).

### 🔍 Inspeção Translúcida e Textos Ocultos (Canvas 3D)
Graças à injeção da biblioteca **Three.js**, quando você abre um objeto para inspecioná-lo de perto, uma tela 3D invisível sobrepõe o cenário do seu navegador (`webgl-canvas`). Isso permite rotacionar pergaminhos em 3D.
Além disso, um *Canvas de Texto Oculto* é gerado paralelamente (`text-canvas-secret`). Somente quando a ferramenta correta (como a Lupa de Latão) for pareada, o texto que está nesta tela revelará o que nele está escrito.

---

## 📡 3. Multiplayer e Conexão (PeerJS)

### Como as salas são formadas?
O sistema abandona o uso de banco de dados pesados e resolve usar **WebRTC**.
1. **Lobby Inicial:** O jogador escolhe o nome e seleciona a identidade visual da sessão atual.
2. **P2P:** O anfitrião gera a conexão da mesa e um link de "convite interno" baseado na Hash do servidor do PeerJS.
3. **Diário de Mesa (Logs):** À direita da tela, um terminal de Chat atua primariamente como uma central de registros. Se o Mestre encontra uma pista, uma tag de evento é transmitida globalmente para as instâncias dos outros amigos notificando: *"Fulano encontrou uma Lupa na mesa"*.

---

## 🛠️ 4. Deploy e Manutenção
- O jogo inteiro é construído através de módulos javascript (*Vite Bundler*) para rodar o mais rápido possível e de forma ultra-comprimida.
- **Atenção nas Imagens:** O Vite carrega e compila todas as texturas e ícones do `/public/` original para a **Raiz** do diretório do Netlify. É crucial que o código (como feito na nossa correção via powershell) referencie as imagens usando `/nome.png` e não `./public/nome.png`.

*Dica de Mestre: Para jogar o build isolado em casa na rede local ou máquina, lance sempre um servidor com `Live Server` do VSCode ou `Python http.server`.*
