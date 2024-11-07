from peewee import Model, SqliteDatabase, CharField, IntegerField, TextField

db = SqliteDatabase('ORM.db')

class BaseModel(Model):
    class Meta:
        database = db 

class Jogo(BaseModel):
    id_jogo = IntegerField(primary_key=True)
    nome = CharField()
    sobre = TextField()

    class Meta:
        database = db


class Noticia(BaseModel):
    id_noticia = IntegerField(primary_key=True)
    titulo = CharField()
    data = IntegerField()
    email = CharField()
    senha = CharField()

    class Meta:
        database = db

        
class Usuario(BaseModel):
    id_usuario = IntegerField(primary_key=True)
    nome = CharField()
    email = CharField()
    senha = CharField()

    class Meta:
        database = db


class Mensagens(BaseModel):
    id_mensagem = IntegerField(primary_key=True)
    idChat = IntegerField()
    idJogo = IntegerField()
    idUsuario = IntegerField()

    class Meta:
        database = db

class ChatGeral(BaseModel):
    idChat = IntegerField(primary_key=True)
    idJogo = IntegerField()
    idUsuario = IntegerField()

    class Meta:
        database = db


def inicializar_banco():
    db.connect()
    db.create_tables([Jogo, Noticia, Usuario, Mensagens, ChatGeral]) 
    db.close()


if __name__ == "__main__":
    inicializar_banco()
    print("Banco de dados conectado e tabelas criadas.")