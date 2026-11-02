# Marcos — Sites & dashboards

Portfólio pessoal em português, responsivo e sem dependências externas. Reúne uma demonstração comercial independente e um projeto de código existente.

## Projetos apresentados
- **Zyon Pet Store:** conceito independente, sem vínculo ou aprovação da empresa. Agendamento e painel são simulados, com dados fictícios e sem pedidos reais.
- **IconBro:** fork comunitário não oficial do Iconify, com suporte experimental ao Android 14. Consulte os créditos, requisitos e limitações no repositório original listado na página.

## Funcionalidades
- Tema claro e escuro (sem persistência).
- Filtros de projetos.
- Dashboard demonstrativo com seleção de período e dados fictícios.
- Gerador de resumo de projeto com cópia e alternativa manual. Não envia nem armazena dados.
- Navegação por teclado e respeito à preferência de movimento reduzido.

## Visualizar
Baixe os arquivos do repositório e abra `index.html` em um navegador. Não é necessário instalar ferramentas nem configurar chaves.

## Personalizar
Edite os textos e links em `index.html`, as cores em `style.css` e as interações em `script.js`. O contato via WhatsApp não foi configurado: nenhum telefone foi inventado ou exposto. Os dados do painel ficam no objeto `datasets` em `script.js`.

## Limites
Este é um site estático, sem autenticação, banco, backend, pagamentos ou formulário de envio. As demonstrações não representam contratos ou resultados comerciais comprovados. Não há ferramentas de análise ou cookies.

## Testes
`test_portfolio.py` valida os principais fluxos em Chromium, layout mobile e desktop, ausência de rolagem horizontal e erros de JavaScript. Requer Python e Playwright com Chromium instalados.

## Publicação opcional
O site está pronto para hospedagem estática gratuita. Para GitHub Pages, selecione a branch `main` e a pasta raiz nas configurações Pages do repositório. A publicação não é ativada automaticamente por este projeto.
