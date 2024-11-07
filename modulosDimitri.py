from peewee import Model, SqliteDatabase, CharField, IntegerField, TextField

db = SqliteDatabase('Dimitri.db')

class BaseModel(Model):
    class Meta:
        database = db 

class tb_cidades(BaseModel):
    cod_cidade = IntegerField(primary_key=True)
    nome_cidade = TextField()

    class Meta:
        database = db


class tb_especialidades(BaseModel):
    cod_especialidade = IntegerField(primary_key=True)
    descricao_especialidade = TextField()
 

    class Meta:
        database = db

        
class tb_estado(BaseModel):
    cod_estado = IntegerField(primary_key=True)
    sigla = CharField()
    nome_estado = TextField()


def inicializar_banco():
    db.connect()
    db.create_tables([tb_cidades, tb_especialidades, tb_estado]) 
    db.close()


if __name__ == "__main__":
    inicializar_banco()
    print("Banco de dados conectado e tabelas criadas.")