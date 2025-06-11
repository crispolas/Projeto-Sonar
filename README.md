# Demonstração Prática do SonarCloud com uma API FastAPI

**Projeto da disciplina de Engenharia de Software**

**Grupo:**
* [Nome1]
* [Nome2]
* [Nome3]
* [Nome4]
* [Nome5]
* [Nome6]

---

## 1. Introdução à Ferramenta: SonarQube e SonarCloud

O SonarQube é uma plataforma open-source que analisa o código-fonte para encontrar problemas de qualidade, como bugs, vulnerabilidades, códigos duplicados, mal formatados ou de difícil manutenção. Ele é instalado localmente ou em um servidor da empresa.

No nosso caso, utilizamos o SonarCloud, que é a versão em nuvem do SonarQube. Ele possui a mesma função principal, mas elimina a necessidade de instalação local, configuração de servidores ou uso de Docker. Isso facilita muito o processo de integração com repositórios e CI/CD, oq torna o processo muito mais fácil.

### Principais Recursos e Vantagens

* **Análise Automática**: Integrado com plataformas como GitHub, GitLab e Bitbucket, o SonarCloud analisa automaticamente cada *pull request* e *branch*.
* **Detecção Abrangente**: Identifica desde bugs simples até vulnerabilidades de segurança complexas, inclusive code smells.
* **Qualidade do Código (Quality Gate)**: Permite configurar critérios de qualidade que precisam ser atendidos para que um código possa ser mesclado.
* **Interface Intuitiva**: Apresenta os resultados em um dashboard claro e objetivo.

### Limitações

* **Análise Estática**: Não detecta vulnerabilidades que só se manifestam em tempo de execução.
* **Projetos Privados**: A versão gratuita é limitada a projetos públicos. Para repositórios privados, é necessário um plano pago.

---

## 2. Demonstração Prática e Configuração

O projeto usado para a demonstração foi uma **API simples e funcional de TaskBoard**, que permite criar, listar, atualizar e excluir itens. Ele foi desenvolvido com:

* **Python** 3.11+
* **FastAPI**
* **SQLite** (Banco de Dados)
* **SQLAlchemy** (ORM)
* **Pytest** (Testes)

### Estrutura de Diretórios

```
/
|
├── .github/
│   └── workflows/
│       └── build.yml          # Define o workflow de CI/CD para análise do SonarCloud
|
├── app/                       # Contém todo o código-fonte da aplicação FastAPI
│   ├── routers/               # Define as rotas (endpoints) da API
│   ├── crud.py                # Contém as funções de Create, Read, Update, Delete
│   ├── database.py            # Configuração da conexão com o banco de dados
│   ├── main.py                # Ponto de entrada da aplicação FastAPI
│   ├── models.py              # Modelos de dados da SQLAlchemy (tabelas do banco)
│   └── schemas.py             # Schemas Pydantic para validação de dados
|
├── test/                      # Contém os testes automatizados da aplicação
│   └── test.py                # Scripts de teste com Pytest para validar a API
|
├── .gitignore                 # Especifica arquivos a serem ignorados pelo Git
├── README.md                  # Este arquivo de documentação
├── requirements.txt           # Lista de dependências Python do projeto
└── sonar-project.properties   # Arquivo de configuração para o scanner do SonarCloud
```

### Análise dos Resultados

Após a configuração do pipeline de CI/CD, cada `push` para o repositório disparou uma nova análise no SonarCloud. O dashboard resultante da última análise nos forneceu insights cruciais sobre a qualidade do nosso código:

![Dashboard do SonarCloud](https://i.imgur.com/link-da-imagem.png)

A análise do dashboard revelou os seguintes pontos:

1.  **Quality Gate: `Failed`**: O resultado mais importante foi a **falha** no "Portão de Qualidade". Em um ambiente profissional, isso impediria o merge do código, protegendo a branch principal de código que não atende aos padrões de qualidade da equipe.

2.  **Causa da Falha: Cobertura de Testes**: A análise apontou que a falha ocorreu devido a **`0.0% de Cobertura de Testes`** no código novo, enquanto o critério mínimo exigido era de 80%. Isso significa que nosso script de teste (`test/test.py`) não está efetivamente testando a lógica de negócio implementada na pasta `app/`, representando um risco, pois bugs podem passar despercebidos.

3.  **Pontos Positivos:**: Um resultado muito positivo foi que, apesar da baixa cobertura, a ferramenta **não detectou nenhum `Issue`**. Isso indica que o código está bem escrito, sem bugs óbvios e vulnerabilidades de segurança.

Com essa demonstração, vemos que o SonarCloud é eficiente no que diz respeito a validação da qualidade do código e ao mesmo tempo também consegue impor boas práticas de engenharia, como a necessidade de testes.

---

## 3. Dificuldades Enfrentadas

A implementação prática do SonarCloud em nosso pipeline de CI/CD apresentou uma série de desafios técnicos, cuja resolução foi fundamental para o aprendizado da equipe.

* **Configuração do Pipeline de CI/CD:** O principal obstáculo foi a correta configuração do arquivo de workflow (`.github/workflows/build.yml`). O pipeline falhou repetidamente devido à ausência de propriedades mandatórias (`sonar.projectKey` e `sonar.organization`). A depuração foi complexa e extremamente demorada, pois exigiu a análise detalhada dos logs do GitHub Actions para identificar a causa raiz do problema, gerando um ciclo de tentativas e erros.

    > ![Figura 1:]([LINK])

* **Ajuste Fino de Propriedades e Ambiente:** Encontramos erros na configuração de arquivos de suporte, como o `sonar-project.properties`, que continha valores incorretos para a organização. Um desafio adicional foi o erro `invalid value for the sonar.tests property`, que ocorria porque o scanner procurava um diretório de testes em um caminho inexistente.

    > ![Figura 2:]([LINK])


* **Diagnóstico e Correção Sequencial:** A solução final não foi um único ajuste, mas o resultado de uma correção sequencial de múltiplos problemas, incluindo a configuração de chaves de acesso, o ajuste de diretórios e a sincronização do repositório. O processo foi documentado nas interações do grupo até a validação final do funcionamento da ferramenta.

    > ![Figura 4:]([LINK])

A resolução desses desafios nos proporcionou um profundo conhecimento prático sobre a integração de ferramentas de DevSecOps, a importância da precisão na configuração de arquivos YAML e a dinâmica de trabalho em equipe para depurar sistemas complexos.

---

## 4. Conclusão: Para que tipo de projeto essa tecnologia é ideal?

Recomendamos o uso do **SonarCloud** para praticamente **qualquer tipo de projeto de software**, mas ele se destaca em:

* **Projetos com Múltiplos Desenvolvedores**: Garante que todos sigam um padrão de qualidade de código, facilitando a manutenção e a colaboração.
* **Aplicações Críticas e de Longa Duração**: Ajuda a manter a "saúde" do código ao longo do tempo, evitando o acúmulo de dívida técnica e falhas de segurança.
* **Equipes que Adotam DevOps/DevSecOps**: É uma ferramenta essencial para integrar a segurança no início do ciclo de desenvolvimento (*shift-left*), fornecendo feedback rápido e automatizado.
* **Projetos de Código Aberto**: Por ser gratuito para repositórios públicos, é a escolha perfeita para a comunidade open source que deseja manter um alto padrão de qualidade.
