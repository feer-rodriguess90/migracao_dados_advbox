# Projeto de Migração de Dados

Teste prático. Objetivo criar um script em Python para realizar a migração de dados e tratá-los de acordo com o modelo de tabelas preestabelecido, garantindo que os dados sejam corretamente estruturados, formatados e prontos para a migração.

## Desafios Encontrados

- **Tratamento de dados inconsistentes**: Muitas informações vinham em formatos não padronizados, como números de processos como strings ou códigos de clientes em formatos não unificados.
- **Formatação das datas**: Garantir que as datas fossem padronizadas no formato correto para a migração.
- **Múltiplos encodings:** Durante a leitura dos arquivos extraídos, foi necessário detectar e ajustar dinamicamente o encoding dos arquivos para evitar erros de leitura, já que os arquivos não seguiam um padrão único.
- **Integração de diferentes fontes de dados**: As tabelas continham informações relacionadas, mas com diferentes identificadores, exigindo a combinação e o mapeamento adequado.
- **Integração de Funções:** Garantir que as funções de extração, tratamento e formatação trabalhem juntas dentro do fluxo da interface.
- **Tempo Limitado:** O prazo curto para execução do teste exigiu priorização de tarefas e soluções simplificadas, com foco em entregar uma solução funcional. Com isso, a complexidade das tarefas teve que ser gerenciada de forma rápida e eficiente.

## TODO - Etapas Finais para o Tratamento de Dados

1. **Atualizar o campo `cod_usuario`**:
   - O campo `cod_usuario` precisa ser alterado para se alinhar ao padrão de "codigo" utilizado nas demais tabelas.
   
2. **Tratar o número dos processos**:
   - O número dos processos atualmente está como string e precisa ser tratado para garantir que possa ser manipulado e carregado corretamente.

3. **Padronizar os nomes das cidades**:
   - As cidades precisam ser normalizadas para que estejam em um formato consistente, conforme o esperado pelo sistema.

4. **Coletar a origem do cliente**:
   - A origem do cliente deve ser coletada da tabela `v_campo_livre2_CodEmpresa_92577.csv` e atribuída corretamente na tabela de **Clientes**.

5. **Integração Completa com a Interface:**
   - Ligar as funções de extração e tratamento à interface para que, ao carregar o arquivo desejado, as tabelas `clientes` e `processos` sejam geradas automaticamente, já formatadas para migração.
   - Atualmente, o sistema apenas carrega o arquivo selecionado pelo usuário.

## Dependências

Este projeto foi desenvolvido utilizando as seguintes bibliotecas:

- `pandas` - Para manipulação e análise de dados.
- `tkinter` - Para a criação da interface gráfica simples para upload e download de arquivos.

## Interdace Gráfica

- Tela principal para o usuário final carregar o arquivo desejado.

![interface_grafica](https://github.com/feer-rodriguess90/migracao_dados_advbox/blob/main/assets/interface_tkinter.png)

- Mensagem de arquivo carregado com sucesso ou caso surja algum erro no carregamento.

![mensagem_arq_carregado](https://github.com/feer-rodriguess90/migracao_dados_advbox/blob/main/assets/mensagem_tkinte.png)

## Instruções de Uso

1. Clone o repositório:
   ```bash
   git clone https://github.com/feer-rodriguess90/migracao_dados_advbox.git

   cd migracao_dados_advbox

2. Instale as dependências
   ```bash
    pip install -r requirements.txt

3. Execute o sistema de interface:
   ```bash
   python interface.py

4. Siga as instruções na interface para selecionar o arquivo `.rar` ou `.csv` e processar os dados.

## Considerações Finais

Este teste prático foi uma excelente oportunidade para aplicar conhecimentos técnicos em um cenário real e desafiador. Uma oportunidade incrível de aprendizado e crescimento. Dentro do período proposto, foi possível aplicar conhecimentos adquiridos e aprender mais sobre o tratamento de dados e a integração de sistemas. 

Este projeto representa um ponto de partida para o desenvolvimento de soluções mais robustas e eficientes. Melhorias futuras, como automações adicionais e refinamentos na interface, são os próximos passos para garantir a evolução contínua. 

Sugestões e feedbacks são sempre bem-vindos! Juntos, podemos aprimorar ainda mais este sistema! 


## Happy coding! 👩🏽‍💻 
[![linkedin](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/datavizwithfer/) 
[![medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@DataVizWithFer)

<div align="center">
<img src="https://forthebadge.com/images/badges/built-with-love.svg" />
</div>

