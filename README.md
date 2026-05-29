# O Enigma de Xylo

Jogo investigativo cooperativo em estilo escape room, com exploração point-and-click, inspeção de pistas em 2D, inventário categorizado e suporte a mesa multiplayer com Mestre como fonte da verdade.

## Visão Geral

`O Enigma de Xylo` coloca os jogadores em um esconderijo repleto de mecanismos, cartas, objetos ocultos e passagens secretas. A experiência mistura exploração de cenário, leitura de pistas, combinação de itens e resolução de puzzles interligados até revelar novas áreas e artefatos do mundo de Axioma.

O projeto foi evoluído de forma incremental e hoje representa uma versão jogável e praticamente final do jogo, com foco em UX de investigação, clareza de inventário e progressão cooperativa.

## Premissa

Os jogadores exploram o esconderijo de Xylo em busca de segredos ligados a Edgar, Nimue, à Forja Real e a sociedades ocultas que operam nas rotas de Axioma. Ao longo da partida, pistas documentais, objetos mágicos e mecanismos escondidos revelam novas camadas da narrativa e destravam salas adicionais.

## Principais Mecânicas

- Hotspots invisíveis sobre o cenário principal e salas secundárias.
- Inspeção de pistas em 2D com canvas.
- Ferramentas equipáveis com cursores e comportamentos próprios.
- Inventário separado por categoria.
- Puzzles contextuais com modais leves.
- Recompensas com feedback visual e microanimações.
- Fluxo multiplayer com sincronização de estado da mesa.

## Inventário

O inventário é dividido em três grupos principais:

- **Ferramentas**: itens equipáveis e usáveis, como Lupa, Lanterna, Chave de Fenda e itens especiais ativáveis.
- **Pistas**: cartas, retratos, documentos e evidências de investigação.
- **Loot**: recompensas, componentes, moedas, chaves e artefatos coletáveis.

Essa separação ajuda a manter a leitura do progresso clara sem misturar narrativa, utilidade e recompensa.

## Multiplayer e Papel do Mestre

O jogo suporta uma mesa cooperativa em que o **Mestre/Host** atua como fonte da verdade para o estado compartilhado.

Estado sincronizado da mesa:

- sala/cena atual;
- inventário relevante;
- hotspots já coletados;
- flags de progresso;
- puzzles resolvidos;
- presença de jogadores conectados.

Quando um novo jogador entra ou reconecta, ele recebe um snapshot atualizado da mesa para cair no mesmo estado do restante do grupo.

## Puzzles Implementados

Entre os principais sistemas e puzzles já implementados:

- **Carta_Edgar** com inspeção 2D, Lupa revelando substituições e Lanterna revelando `islandmap`.
- **Carta da Forja Real** em inspeção 2D legível.
- **Carta do Corvo** com revelação progressiva sob a Lanterna e obtenção da Moeda do Corvo.
- **Olho de Nimue / Olho de Ônix** com ativação e recompensa associada.
- **Montagem da Lanterna** com peças, popup de montagem e compatibilidade com puzzles posteriores.
- **Puzzle dos Livros** com tentativas, histórico visual e desbloqueio do Quarto Escondido.
- **Puzzle do Baú/Cadeados** com trancas conectadas e recompensa automática.
- **Mini puzzle da lamparina** no Quarto Escondido com engrenagem e liberação do núcleo.
- **Combinações de itens** para montagem de artefatos derivados.

## Salas e Cenas Existentes

- **Sala Principal**
  - cenário base da investigação;
  - maioria dos hotspots iniciais;
  - acesso aos itens e puzzles centrais.

- **Quarto Escondido**
  - liberado após o puzzle dos livros;
  - possui hotspots próprios, itens, documentos e puzzles adicionais;
  - mantém navegação de ida e volta sem resetar progresso.

## Como Rodar Localmente

### Opção 1: PowerShell

Use o script local do projeto:

```powershell
.\serve.ps1
```

### Opção 2: Python

```powershell
python -m http.server 8080
```

Depois, abra no navegador:

```text
http://localhost:8080/
```

## Estrutura Geral dos Arquivos

Estrutura resumida do projeto:

```text
Segredo/
|- index.html
|- assets/
|  \- unminified.js
|- README.md
|- COMO_JOGAR.md
|- serve.ps1
|- check_syntax.py
|- *.png / *.svg (assets visuais e placeholders)
```

### Arquivos principais

- `index.html`: shell principal da aplicação.
- `assets/unminified.js`: lógica central do jogo, UI, multiplayer, puzzles e inventário.
- `serve.ps1`: utilitário local para subir servidor simples.
- `check_syntax.py`: checagem rápida de balanceamento/sintaxe útil durante manutenção.
- `COMO_JOGAR.md`: documento complementar de mecânicas e arquitetura.

## Observações Importantes

- A base atual foi mantida com mudanças pontuais e incrementais, evitando refatorações amplas.
- O projeto possui placeholders visuais e alguns assets temporários que podem ser trocados depois sem exigir reestruturação grande.
- O foco desta versão final é estabilidade jogável, clareza de UX e preservação dos fluxos já validados.

## Assets, Placeholders e Créditos

- Diversos ícones e imagens de itens usam placeholders ou versões provisórias para permitir iteração rápida de conteúdo.
- Alguns arquivos de arte podem ser substituídos posteriormente por versões finais sem alterar ids internos dos itens.
- Sempre que possível, os nomes internos de itens foram preservados para evitar regressões em puzzles e sincronização.

## Estado Atual da Versão

Esta branch representa a versão final atual de trabalho do projeto, com:

- fluxo principal jogável;
- puzzles principais integrados;
- Quarto Escondido desbloqueável;
- multiplayer funcional com sincronização de mesa;
- documentação atualizada para manutenção e entrega.
