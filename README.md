# Cronograma Acadêmico DEV - SENAI 2026/1 👨‍💻🎓

Este projeto consiste em uma modernização radical (Redesign Full-Stack) do cronograma de aulas de Desenvolvimento de Sistemas do SENAI. Partimos de uma simples grade em PDF e tabelas rudimentares em HTML para um **Sistema SaaS Fluído (Dashboard)** incrivelmente rápido e responsivo.

## ✨ Features Implementadas
- **Hero Section Cinemática:** Fundo de vídeo animado com título possuindo fade-ins assíncronos em cascata e tipografia com cores estilo Degradê Premium (Neon Blue).
- **Glassmorphism:** Uso maciço de desfoque (`backdrop-filter`) em cartões para dar a sensação de janelas translúcidas modernistas flutuando sobre a página.
- **Bento-Box Timeline:** Em vez de "só um bloco imenso", as aulas dos meses foram desmembradas num visual que simula o feed do aplicativo iOS da Apple. Linhas conectivas (*hover tracks*) que reagem ao percurso do mouse.
- **Toggle View:** Botão interativo construído com classes injetadas para que o aluno alterne instantaneamente entre "Aulas Compactas" e "Calendário Completo (incluindo fins de semana sem aula)".
- **Responsividade (Mobile & Tablets):** Adaptação elástica da arquitetura (Flex e Grid columns) que não enrosca independente da resolução. Desconstruímos o scroll interno restrito para liberar a página 100% no touch-screen em *Androids e iPhones*.

## 🏗 Arquitetura do Repositório (Organização)
```text
/
├── assets/
│   ├── css/
│   │   └── style.css          # Design System e Media Queries Enterprise
│   ├── img/
│   │   └── SENAI_logo...png   # Identity Visual
│   └── media/
│       └── video...mp4        # Video Background Header
├── docs/                      # Original PDFs e Wireframes
├── tools/
│   └── build_timeline.py      # Automação/Raspagem de Grade de Aulas
├── index.html                 # Página Matriz Single-Page Application (SPA)
└── README.md                  # Algoritmo de Documentação Oficial
```

## 🛠️ Tecnologias Principais
- **HTML5**: Estrutura Semântica
- **Vanilla CSS3 Moderno**: Efeitos Neons, Glassmorphism, UI fluida.
- **Python 3**: Usado como Motor de Template (`tools/build_timeline.py`) para injetar a tabela de forma automática prevenida de erros humanos.

## 🚀 Como Visualizar
Este projeto **não necessita de Frameworks pesados ou Servidores complexos** para rodar localmente. Você pode:
1. Abrir a pasta raiz do projeto.
2. Dar dois cliques em `index.html`.
3. Ou, para emular uma Cloud Server e evitar os alertas nativos do Google Chrome sobre CORS na versão Desktop, abra a pasta raiz em seu Visual Studio Code e inicie com a extensão nativa **Live Server**.

## 📅 Manutenção
Se precisar de novas disciplinas ou mudar algum dia:
1. Abra `/tools/build_timeline.py`.
2. Modifique os arrays de curso.
3. No terminal execute na raiz: `python tools/build_timeline.py`.
4. O `index.html` será enxertado magicamente com a grade corrigida!
