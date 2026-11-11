def exibirusuarioscadastrados( usuariosCadastrados:dict ):
    for user , (email , idade , adm) in usuariosCadastrados.items():
        print(f"USUARIO : {user}")
        print(f"EMAIL : {email}")
        print(f"IDADE : {idade}")
        print(f"ADM : {adm}")
        print("========")