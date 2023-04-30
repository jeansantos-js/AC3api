importar  psicopg2
from  flask  import  Flask , jsonify , request , make_response

app  =  Frasco ( __name__ )

# configurações do banco de dados
db_config  = {
    'host' : 'localhost' ,
    'usuário' : 'gerente' ,
    'senha' : 'gerente' ,
    'banco de dados' : 'dados'
}

# rota GET
@ aplicativo . rota ( '/registros' , metodos = [ 'GET' ])
def  get_registros ():
    # conecta ao banco de dados
    conn  =  psicopg2 . conectar ( ** db_config )
    cursor  =  conn . cursor ()

    # busca os registros no banco de dados
    cursor . execute ( 'SELECT id, nome, idade FROM registros' )
    registros  = []
    para  id , nome , idade  no  cursor . buscar ():
        registros . append ({ 'id' : id , 'nome' : nome , 'idade' : idade })

    # fecha a conexão com o banco de dados
    cursor . fechar ()
    conn . fechar ()

    resposta  =  make_response ( jsonify ( registros ), 200 )
     resposta de retorno

# rota POST
@ aplicativo . rota ( '/registros' , metodos = [ 'POST' ])
def  post_registros ():
    # conecta ao banco de dados
    conn  =  psicopg2 . conectar ( ** db_config )
    cursor  =  conn . cursor ()

    # cadastra o registro no banco de dados
    registro  =  solicitação . get_json ()
    nome  =  registro [ 'nome' ]
    idade  =  registro [ 'idade' ]
    cursor . execute ( 'INSERT INTO registros (nome, idade) VALUES (%s, %s)' , ( nome , idade ))
    conn . cometer ()

    # fecha a conexão com o banco de dados
    cursor . fechar ()
    conn . fechar ()

    resposta  =  make_response ( jsonify ( registro ), 201 )
     resposta de retorno

# rota APAGAR
@ aplicativo . rota ( '/registros/<int:id>' , metodos = [ 'DELETE' ])
def  delete_registro ( id ):
    # conecta ao banco de dados
    conn  =  psicopg2 . conectar ( ** db_config )
    cursor  =  conn . cursor ()

    # exclui o registro do banco de dados
    cursor . execute ( 'DELETE FROM registros WHERE id = %s' , ( id ,))
    conn . cometer ()

    # fecha a conexão com o banco de dados
    cursor . fechar ()
    conn . fechar ()

    response  =  make_response ( jsonify ({ 'message' : f'Registro { id } excluído com sucesso' }), 200 )
     resposta de retorno

se  __name__  ==  '__main__' :
    app . executar ( depurar = Verdadeiro )
