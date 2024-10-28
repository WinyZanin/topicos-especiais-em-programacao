# 1

**Prompt simples:**

*   **Pergunta:** Escreva uma carta de recomendação
*   **Formato:** Texto em branco, sem delimitadores

**Responsas do modelo com prompt simples:**
```
Olá,

Gostaria de recomendar João para qualquer oportunidade futura. Ele é um profissional muito motivado e tem habilidades excepcionais.

Atenciosamente,
[Seu Nome]
```

**Prompt revisado:**

*   **Pergunta:** Escreva uma carta de recomendação para o Professor Luiz, sobre as habilidades profissionais do candidato João.
*   **Contexto:** O Professor Luiz está procurando um candidato para uma vaga em seu departamento, e ele precisa de uma carta de recomendação para apresentar ao comitê de seleção. A carta deve destacar os pontos fortes de João como profissional e demonstrar sua excelência no trabalho.
*   **Delimitadores:** < Professor Luiz >, < Cartera de Recomendação >
*   **Formato:** Texto em branco

**Responsas do modelo com prompt revisado:**

```
<Professor Luiz>,
Gostaria de recomendar João para a vaga que você está procurando. Ele é um profissional muito motivado e tem habilidades excepcionais no que diz respeito ao trabalho de equipe, criatividade e atenção aos detalhes.

Sinceramente,
[Seu Nome]
```
O contexto adicionado ao prompt teve um impacto significativo na qualidade da resposta. Ao fornecer detalhes sobre o destinatário e propósito da carta, o modelo conseguiu:

*   **Destacar as habilidades relevantes:** O modelo destacou as habilidades de João que são mais pertinentes para a vaga solicitada pelo Professor Luiz.
*   **Demonstrar compreensão do contexto:** A resposta demonstra uma melhor compreensão da situação e do propósito da carta, o que resulta em um resultado mais específico e relevante.
*   **Melhorar a coesão e a fluidez:** A resposta foi mais coerente e fluída, pois o modelo teve mais informações para trabalhar com base nos detalhes fornecidos.

# 2

**Definindo a Persona:**

*   **Nome:** Luana
*   **Idade:** 25 anos
*   **Gênero:** Feminino
*   **Profissão:** Assistente Virtual da Livraria
*   **Personagem:** Luana é uma assistente virtual amigável, curiosa e sempre disposta a ajudar. Ela gosta de aprender sobre diferentes assuntos e está sempre atualizada sobre as últimas tendências literárias.
*   **Objetivos:**
    *   Auxiliar os clientes na busca por livros que atendam às suas necessidades
    *   Proporcionar recomendações personalizadas de livros
    *   Oferecer informações sobre diferentes categorias de livros e autores
*   **Comportamento:** Luana é uma pessoa organizada e detalhista, sempre procurando aprimorar suas habilidades. Ela é muito ativa em redes sociais e gosta de compartilhar recomendações de livros com seus amigos.
*   **Percepção da Clientela:** Luana considera que os clientes são pessoas com necessidades específicas e gostam de ajudá-los a encontrar o livro perfeito.

**Prompt:**

```
Olá! Estou procurando por um livro sobre astronomia para uma pesquisa universitária. Você tem alguma recomendação?
```

---

**Responsas do Modelo com Prompt Padrão:**

*   "Parece que você está procurando por um livro sobre astronomia. Vamos começar a pesquisar juntos!"
*   "Aqui estão alguns títulos populares sobre astronomia: \[ lista de livros ]"
*   "Você pode nos dizer mais sobre o que você está procurando? Quais temas específicos gostaria de explorar?"

**Impacto da Definição da Persona na Resposta do Modelo:**

A definição da persona Luana teve um impacto significativo na resposta do modelo:

*   **Relevância:** A resposta foi mais relevante, pois o modelo considerou as necessidades específicas da cliente (pesquisa universitária) e ofereceu recomendações relevantes.
*   **Personalização:** O modelo personalizou a resposta com base nas informações fornecidas pela persona (nome do livro, pesquisa universitária). Isso fez com que a resposta fosse mais útil e específica para o cliente.
*   **Corresponsabilidade:** A definição da persona Luana também fez com que o modelo se sentisse mais responsável em fornecer uma resposta de alta qualidade. Isso resultou em um tom mais amigável e empático na resposta.

# 3

**Prompt Vago:**

"Descreva um cenário futurista sem dar detalhes."

---

**Resposta do Modelo com Prompt Padrão:**

*   "Um futuro distante onde as tecnologias avançadas mudaram o mundo."

---

**Reescrita do Prompt com Instruções Claras e Específicas:**

```
Descreva um cenário futurista em um planeta colonizado por humanos, com uma cidade escura e desolada à noite, onde as luzes sejam fornecidas por lanternas de energia solar. A cidade seja rodeada por colinas brancas e montanhas de gelo. Inclua também robôs que patrulham a cidade e máquinas que geram energia a partir da energia solar."
```

---

**Comparação das Respostas:**

*   **Resposta Vaga:** A resposta foi muito vaga, não fornecendo detalhes suficientes para criar uma cena vívida.
*   **Resposta Reescrita com Instruções Claras e Específicas:** A resposta foi mais específica e incluiu todos os detalhes solicitados. Isso permitiu ao modelo criar uma cena futurista mais rica e detalhada.

**Importância da Clareza nas Instruções:**

*   **Significância da Claridade**: A claridade nas instruções é crucial para garantir que o modelo entenda exatamente o que está solicitando.
*   **Eficácia das Instruções:** As instruções claras e específicas permitem ao modelo criar respostas mais precisas, completas e relevantes.
*   **Redução dos Erros:** Ao fornecer instruções claras, reduz-se o número de erros cometidos pelo modelo.

# 4

**Prompt Inicial:**

"Descreva uma figura histórica de destaque com uma curta biografia."

---

**Resposta do Modelo com Prompt Padrão:**


*   "Nelson Mandela foi um líder político sul-africano que lutou contra o apartheid. Ele foi preso e passou 27 anos na prisão, mas se tornou presidente da África do Sul após a dissolução da república. Ele faleceu em 2013."

---

**Análise da Resposta:**

*   **Precisão**: A resposta foi precisa em relação à identidade de Nelson Mandela e suas atividades políticas, mas não incluiu detalhes suficientes sobre sua infância, educação ou carreira profissional.
*   **Falta de Contexto**: A resposta não forneceu contexto sobre a época histórica em que Nelson Mandela viveu e suas contribuições para o movimento anti-apartheid.

**Refinamento do Prompt:**

```
Descreva uma figura histórica de destaque com uma curta biografia. Especifique seu nome completo, data de nascimento, origem familiar, educação formal e carreira profissional. Inclua também detalhes sobre suas contribuições políticas, perspectivas culturais e impacto significativo em sua época. Finalize a descrição com a data de morte ou atualização do status.
```

---

**Resposta Refinada:**

*   "Nelson Rolihlahla Mandela foi um líder político sul-africano nascido em 18 de julho de 1918, em Mvezo, província de Ciswana. Ele era filho de um rei local e recebeu uma educação básica antes de estudar na Universidade de Fort Hare. Após a graduação, ele se tornou membro da União Nacional Africana (UNA) e trabalhou como advogado.

Ele foi preso pela primeira vez em 1956 e passou 27 anos na prisão por sua participação no movimento anti-apartheid. Durante sua estadia na prisão, ele se tornou um símbolo de resistência e liderança para o povo sul-africano.

Após a dissolução da república em 1994, Nelson Mandela foi eleito presidente da África do Sul e serviu dois mandatos até 1999. Ele trabalhou incansavelmente para promover a reconciliação e reconstruir a nação após os anos de apartheid.

Ele faleceu em 5 de dezembro de 2013, deixando um legado duradouro como um dos líderes mais importantes da história africana."

---

**Iterações:**

*   **Iteração 1:** Adicionei detalhes sobre a infância e educação de Mandela. Isso permitiu ao modelo criar uma biografia mais completa.
*   **Iteração 2:** Incluí informações adicionais sobre as contribuições políticas e culturais de Mandela. Isso ajudou o modelo a criar uma descrição mais equilibrada e precisa.

---

**Análise das Iterações:**

*   **Melhoria na Precisão**: As iterações refinadas melhoraram significativamente a precisão da resposta, fornecendo detalhes adicionais sobre a vida de Mandela.
*   **Contexto Ampliado**: As instruções adicionaram contexto sobre a época histórica em que Mandela viveu e suas contribuições para o movimento anti-apartheid. Isso permitiu ao modelo criar uma biografia mais completa e precisa.

**Observações:**

*   **Importância da Claridade**: A claridade nas instruções é crucial para garantir que o modelo entenda exatamente o que está solicitando.
*   **Eficácia das Instruções:** As instruções claras e específicas permitem ao modelo criar respostas mais precisas, completas e relevantes.

# 5

Para desenvolver um prompt personalizado para um posto de gasolina, consideraremos as seguintes técnicas:

1.  **Definição clara do objetivo**: Estabelecermos o que queremos que o modelo faça.
2.  **Modelagem do contexto**: Definiremos o contexto em que o modelo operará.
3.  **Formato de entrada**: Especificaremos como será a entrada para o modelo, incluindo quais informações precisam ser fornecidas e no formato que elas devem ser apresentadas.

Aqui está um exemplo de prompt:

Prompt:

```json
P: Você é um gerente de um posto de gasolina. Necessita realizar uma atualização do estoque de combustível com base nos dados históricos. Como eu, a partir dos dados históricos, faça uma previsão para o próximo mês.
```

**Avaliação da eficácia do prompt:**

Depois de fornecer esse prompt, o modelo respondeu como segue:

`Resposta:`

-   `O que é um posto de gasolina? Um posto de gasolina é uma estação de combustível que vende gasolina e outros produtos derivados do petróleo.`
-   `Como atualizar os estoques de combustível? A atualização dos estoques de combustível envolve realizar contagens regulares dos níveis de combustível nos tanques, comparar os dados com as estimativas previamente feitas e ajustar a quantidade de combustível adquirida.`

**Ajustes necessários:**

*   **Mais contexto**: O prompt precisa ser mais claro e fornecer mais contexto sobre o que está sendo pedido.
*   **Formato da entrada**: O modelo está pedindo informações de entrada específicas, como as datas históricas para prever os estoques futuros. Certifique-se de fornecer todos esses detalhes com precisão.

# 6

Para criar dois prompts sobre o mesmo tema com diferentes entonações (formal e casual), consideraremos as seguintes técnicas:

1.  **Definição clara do objetivo**: Estabelecermos o que queremos que o modelo faça.
2.  **Modelagem do contexto**: Definiremos o contexto em que o modelo operará.
3.  **Formato de entrada**: Especificaremos como será a entrada para o modelo, incluindo quais informações precisam ser fornecidas e no formato que elas devem ser apresentadas.

Aqui estão os dois prompts:

**Prompt Formal (Entonação: 4)**

```json
P: Como um gerente de um posto de gasolina, é sua responsabilidade garantir que o estoque de combustível esteja sempre atualizado e em conformidade com as necessidades do mercado. Por favor, forneça uma previsão para o próximo mês baseada nos dados históricos.
```

**Prompt Casual (Entonação: 9)**

```json
P: Olá! Estou aqui para gerenciar um poste de gasolina e quero saber se você pode me ajudar a fazer uma previsão do que vai acontecer com o estoque de combustível no próximo mês. Você poderia nos fornecer os dados históricos para que eu possa fazer uma ideia melhor?
```

**Ajustes necessários:**

*   **Mudanças na linguagem**: O prompt formal usa termos mais formais e evita contratos, enquanto o prompt casual usa uma linguagem mais informal e inclui expressões como "olá".
*   **Tono da entrada**: A entrada deve refletir a entonação escolhida. Por exemplo, o prompt formal usa frases mais longas e complexas, enquanto o prompt casual usa frases curtas e concisas.

# 7

Para criar dois prompts para gerar textos com diferentes sentimentos sobre o mesmo assunto, consideraremos as seguintes técnicas:

1.  **Definição clara do objetivo**: Estabelecermos o que queremos que o modelo faça.
2.  **Modelagem do contexto**: Definiremos o contexto em que o modelo operará.
3.  **Formato de entrada**: Especificaremos como será a entrada para o modelo, incluindo quais informações precisam ser fornecidas e no formato que elas devem ser apresentadas.

Aqui estão os dois prompts:

**Prompt com Sentimento Positivo (Entonação: 8)**

```json
P: A tecnologia de inteligência artificial está revolucionando a forma como vivemos nossos dias. Ela está nos ajudando a resolver problemas complexos e a melhorar nossa qualidade de vida. Por exemplo, os sistemas de IA estão sendo usados em campos como saúde, finanças e meio ambiente para otimizar processos e reduzir custos. Vamos explorar como essa tecnologia está melhorando nossas vidas.
```

**Prompt com Sentimento Negativo (Entonação: 3)**

```json
P: A tecnologia de inteligência artificial está ameaçando o emprego humano em muitas áreas. Ela está tornando possíveis tarefas rotineiras e monótonas que antes eram realizadas por humanos, levando a uma redução significativa na demanda por mão-de-obra qualificada. Além disso, os sistemas de IA estão sendo usados em campos como saúde para tomar decisões que podem ter consequências graves para a vida das pessoas. É hora de refletir sobre as implicações desse avanço tecnológico.
```

**Ajustes necessários:**

*   **Mudanças na linguagem**: O prompt com sentimento positivo usa termos mais elogiosos e entusiastas, enquanto o prompt com sentimento negativo usa termos mais críticos e alarmistas.
*   **Tono da entrada**: A entrada deve refletir o sentimento escolhido. Por exemplo, o prompt com sentimento positivo usa frases mais longas e encorajadoras, enquanto o prompt com sentimento negativo usa frases curtas e preocupantes.

---

### Dicas adicionais

-   **Verifique as opiniões**: Verifique as opiniões dos especialistas em cada área e busque informações de fontes confiáveis para garantir que o texto seja preciso e informativo.
-   **Mantenha a objetividade**: Tente manter uma postura objetiva ao gerar textos com diferentes sentimentos. Evite expressar opiniões pessoais ou partidárias.
-   **Considere o público-alvo**: Considere o público-alvo do texto e ajuste o sentimento de acordo com as necessidades e preferências do público.

---

# 8

**Prompt 1 - Primeira Pessoa (Perspectiva de 2)**

"Você entende como a tecnologia da inteligência artificial está mudando o mundo? Ela está tornando possíveis tarefas rotineiras e monótonas que antes eram realizadas por humanos, levando a uma redução significativa na demanda por mão-de-obra qualificada. Além disso, os sistemas de IA estão sendo usados em campos como saúde para tomar decisões que podem ter consequências graves para a vida das pessoas. É hora de refletir sobre as implicações desse avanço tecnológico."

**Prompt 2 - Segunda Pessoa (Perspectiva de 3)**

"Eles estão começando a entender como a tecnologia da inteligência artificial está mudando o mundo. Ela está tornando possíveis tarefas rotineiras e monótonas que antes eram realizadas por humanos, levando a uma redução significativa na demanda por mão-de-obra qualificada. Além disso, os sistemas de IA estão sendo usados em campos como saúde para tomar decisões que podem ter consequências graves para a vida das pessoas. É hora de refletir sobre as implicações desse avanço tecnológico."

**Prompt 3 - Terceira Pessoa (Perspectiva de 1)**

"Ela é uma ferramenta poderosa que está mudando o mundo. Ela está tornando possíveis tarefas rotineiras e monótonas que antes eram realizadas por humanos, levando a uma redução significativa na demanda por mão-de-obra qualificada. Além disso, os sistemas de IA estão sendo usados em campos como saúde para tomar decisões que podem ter consequências graves para a vida das pessoas."

**Explicação:**

*   **Perspectiva 1 (Primeira Pessoa)**: O prompt começa com "Você entende..." e usa uma linguagem direta, como se o leitor fosse o protagonista.
*   **Perspectiva 2 (Segunda Pessoa)**: O prompt começa com "Eles estão começando a entender...", usando uma linguagem mais distante, como se o leitor estivesse observando um grupo de pessoas.
*   **Perspectiva 3 (Terceira Pessoa)**: O prompt começa com "Ela é uma ferramenta poderosa...", usando uma linguagem objetiva, como se o leitor fosse alguém que está estudando a tecnologia da inteligência artificial.

# 9

**Prompt 1 - Nível de Detalhe Baixo (2)**

"Uma pessoa está sentada em uma sala com uma mesa de madeira e cadeiras vermelhas."

**Prompt 2 - Nível de Detalhe Alto (7)**

"A pessoa está sentada na parte central da sala, rodeada por móveis de estilo clássico, como um sofá marrom e uma poltrona preta. A mesa de madeira é uma combinação de esculpido e carpintaria artesanal, com detalhes em ouro e prata. As cadeiras vermelhas são de um tipo específico, com formas geométricas e suportes elegantes. Há também uma planta vermelha no canto da mesa, com folhas aromáticas que emitem um aroma agradável. A luz natural entra pela janela, iluminando os objetos e criando sombras interessantes nos cantos."

**Explicação:**

*   **Nível de Detalhe Baixo (2)**: O prompt descreve apenas o ambiente geral da sala, sem mencionar objetos específicos ou detalhes. É um resumo rápido da cena.
*   **Nível de Detalhe Alto (7)**: O prompt fornece uma descrição mais detalhada e completa da cena, incluindo objetos específicos, como a mesa, as cadeiras e a planta. Isso cria uma imagem mais vívida na mente do leitor.