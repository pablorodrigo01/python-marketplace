# Reman Aplicativo - Marketplace

O Reman Aplicativo - Marketplace é uma ferramenta desenvolvida para facilitar a atualização de tabelas em diferentes plataformas de e-commerce. Com este aplicativo, é possível atualizar automaticamente as informações de estoque e preço de produtos em plataformas como Mercado Livre, Shopee e Via Marketplace (Casas Bahia, Pontofrio e Extra), e pode ser facilmente estendido para suportar outras plataformas no futuro.

## Funcionamento

O aplicativo é desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e a biblioteca pandas para manipulação de dados. Ele permite que o usuário selecione um arquivo de entrada contendo informações de produtos, como nome, estoque e preço. Em seguida, o usuário pode clicar no botão "Atualizar Arquivo" para iniciar o processo de atualização das tabelas nas diferentes plataformas.

Ao clicar no botão, o aplicativo lê o arquivo de entrada e extrai as informações necessárias, como nome do produto, estoque e preço. Em seguida, ele percorre as planilhas das plataformas configuradas e procura pelos produtos correspondentes. Quando encontra um produto correspondente, o aplicativo atualiza as células de estoque e preço na planilha da plataforma.

O aplicativo suporta as seguintes plataformas atualmente:
- Mercado Livre
- Shopee
- Via Marketplace (Casas Bahia, Pontofrio e Extra)

No entanto, é possível adicionar suporte a outras plataformas facilmente. Agora, a configuração das plataformas é feita no arquivo config.json. No arquivo config.json, você pode adicionar uma nova configuração para a plataforma desejada, incluindo o nome da plataforma, o nome da planilha, as colunas correspondentes ao nome do produto, estoque e preço, e o caminho do arquivo de saída da plataforma. Dessa forma, você pode estender facilmente o suporte a novas plataformas sem precisar modificar diretamente o código-fonte.

## Planejamento de Melhorias

- [x] Sistema de Log
- [x] Configuração para outras lojas
- [ ] Implementação do Selenium
- [ ] Versão Web

## Implementação do Selenium e Versão Web

A implementação do Selenium não foi continuada devido à dificuldade de realizar a automatização por meio de um executável. No entanto, o aplicativo continua a ser executado com sucesso por meio da interface gráfica construída com a biblioteca Tkinter.

Quanto à versão web, ela ainda não foi desenvolvida, uma vez que a versão atual do aplicativo já atende às necessidades dos usuários. Caso haja demanda por uma versão web no futuro, podemos considerar sua implementação.

## Melhorias Recentes

### 1.2 - 07/07/2023
- A plataforma Magalu foi removida da configuração devido à indisponibilidade do serviço de atualização por planilha oferecido pela plataforma.

### 1.1 - 07/06/2023
- Adicionado sistema de log para mostrar produtos que não foram atualizados corretamente.
- A configuração das lojas agora é feita por meio de arquivos .json, proporcionando uma maneira mais flexível e fácil de adicionar novas plataformas.

![Exemplo do arquivo de log](https://i.imgur.com/7yX76c0.png)

Essas são apenas algumas das melhorias recentes feitas no projeto. Continuamos trabalhando para aprimorar o aplicativo e fornecer uma experiência cada vez melhor aos usuários.

## Requisitos

- Python 3.x
- Bibliotecas: tkinter, pandas, openpyxl

## Como usar - Código fonte

1. Certifique-se de ter Python instalado em seu sistema.
2. Clone o repositório para o seu computador ou faça o download dos arquivos.
3. Instale as dependências necessárias executando o seguinte comando no terminal:
   `pip install -r requirements.txt`
4. Execute o script `Aplicativo.py` com o seguinte comando:
   `python Aplicativo.py`
5. A janela do aplicativo será aberta. Selecione o arquivo de entrada clicando no botão "Procurar".
6. Clique no botão "Atualizar Arquivo" para iniciar o processo de atualização.
7. Aguarde até que o aplicativo conclua a atualização das tabelas.
8. Uma caixa de diálogo informará se a atualização foi concluída com sucesso ou se ocorreu algum erro.

## Contribuição

Contribuições para este projeto são bem-vindas. Se você deseja adicionar suporte a novas plataformas ou fazer melhorias no código, sinta-se à vontade para enviar uma solicitação de pull.

## Aviso

>Este aplicativo foi desenvolvido com o propósito de facilitar a atualização de tabelas em plataformas de e-commerce. Certifique-se de ter permissão adequada para atualizar as tabelas nas plataformas desejadas e esteja ciente das implicações de atualizar grandes volumes de dados em plataformas ao vivo.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

## Contato

Se você tiver alguma dúvida, sugestão ou problema relacionado a este projeto, sinta-se à vontade para entrar em contato comigo.

- Autor: Pablo Rodrigo
- Email: pablorodrigo210104@hotmail.com

Obrigado por usar o Reman Aplicativo - Marketplace! Espero que seja útil para você atualizar suas tabelas nas plataformas de e-commerce de forma mais eficiente.
