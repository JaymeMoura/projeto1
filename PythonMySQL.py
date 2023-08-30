import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pythonmysql',
)
cursor = conexao.cursor()



#Create
def criarProduto():
    Nome_produto = input('Digite o nome do produto: ')
    Valor = input('Digite o valor do produto: ')

    comando = f'INSERT INTO vendas (Nome_produto, Valor) values("{Nome_produto}", {Valor})'
    cursor.execute(comando)
    conexao.commit()#editar o banco de dados

#Read
def lerProdutos():
    comando = 'SELECT * FROM pythonmysql.vendas;'
    cursor.execute(comando)
    resultado = cursor.fetchall()#ler o banco de dados
    print (resultado)

#Update
def atualizarNome():
    Nome_produto = input('Digite o nome do produto que voce quer atualizar: ')
    novo_nome_produto = input('Digite o novo nome: ')

    comando = f'UPDATE vendas SET Nome_produto = "{novo_nome_produto}" WHERE Nome_produto = "{Nome_produto}"'

    cursor.execute(comando)
    conexao.commit()#editar o banco de dados

    cursor.close()
    conexao.close()