from connection.conexao import Conexao


class AgendaDao:

    def cadastrar_contato_agenda(self, nome, sobrenome, endereco, numero, complemento, bairro, uf, data):
        conexao = Conexao()
        comando_sql = f"INSERT INTO tb_agenda (nome, sobrenome, endereco, numero, complemento, bairro, uf, " \
                      f"data_atual) VALUES ('{nome}', '{sobrenome}', '{endereco}', {numero}, '{complemento}', " \
                      f"'{bairro}', '{uf}', '{data}')"
        conexao.executar_query(comando_sql)

    def alterar_contato_agenda(self, id_agenda, nome, sobrenome, endereco, numero, complemento, bairro, uf, data):
        conexao = Conexao()
        comando_sql = f"UPDATE tb_agenda SET nome='{nome}', sobrenome='{sobrenome}', endereco='{endereco}'," \
                      f"numero='{numero}', complemento='{complemento}', bairro='{bairro}', uf='{uf}'," \
                      f"data_atual='{data}' WHERE id_agenda={id_agenda}"
        conexao.executar_query(comando_sql)

    def listar_contatos_tabela(self):
        conexao = Conexao()
        comando_sql = "SELECT id_agenda, nome, sobrenome, endereco, numero, complemento, bairro, uf, " \
                      "date_format(data_atual, '%d/%m/%Y') FROM tb_agenda"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def consultar_contato_id(self, id_agenda):
        conexao = Conexao()
        comando_sql = f"SELECT id_agenda, nome, sobrenome, endereco, numero, complemento, bairro, uf," \
                      f"date_format(data_atual, '%d/%m/%Y') FROM tb_agenda WHERE id_agenda={id_agenda}"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado

    def excluir_contato(self, id_agenda):
        conexao = Conexao()
        comando_sql = f"DELETE FROM tb_agenda WHERE id_agenda={id_agenda}"
        conexao.executar_query(comando_sql)

    def consulta_contato_nome(self, nome):
        conexao = Conexao()
        comando_sql = f"SELECT id_agenda, nome, sobrenome, endereco, numero, complemento, bairro, uf," \
                      f"date_format(data_atual, '%d/%m/%Y') FROM tb_agenda WHERE nome LIKE '%{nome}%'"
        resultado = conexao.executar_consulta(comando_sql)
        return resultado
