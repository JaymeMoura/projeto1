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

def atualizarValor():
    Nome_produto = input('Digite o nome do produto que voce quer atualizar:')
    novo_Valor = input(f'Digite o novo valor do produto {Nome_produto}:')
    comando = f'UPDATE vendas SET Valor = {novo_Valor} WHERE Nome_produto = "{Nome_produto}"'

    cursor.execute(comando)
    conexao.commit()#editar o banco de dados

#Delete
def deletarProduto():

    comando = 'SELECT Nome_produto FROM pythonmysql.vendas;'
    cursor.execute(comando)
    resultado = cursor.fetchall()#ler o banco de dados
    print('existe ', len(resultado), 'itens que podem ser Deletados')
    for row in resultado:

        print(row[0])


    Nome_produto = input('Digite o nome do produto que voce quer Deletar:')
    comando = f'DELETE FROM vendas WHERE Nome_produto = "{Nome_produto}"'

    cursor.execute(comando)
    conexao.commit()#editar o banco de dados
    print (resultado)

num = int( input('digite o que deseja realizar:\n'
            '1) Cria um produto\n'
            '2) Ver o produto\n'
            '3) Atualizar o produto\n'
            '4) Deletar o produto\n'))

print('\n')

if num == 1:
    criarProduto()
elif num == 2:
    lerProdutos()
elif num == 3:
    cont = input('Digite 1 para alterar o nome do produto\n'
                 'e 2 para alterar valor do produto')
    if cont == 1:
        atualizarNome()
    elif cont == 2:
        atualizarValor()
    else:
        print('o mumero invalido')
elif num == 4:
    deletarProduto()
else: 
    print('numero invalido')



cursor.close()
conexao.close()