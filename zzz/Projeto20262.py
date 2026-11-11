import modulos.funcClientes as cliente

usuariosCadastrados = {
    "Caio":["caio@gmail.com" , 18 , True ],
    "Higor":["higor@gmail.com" , 27 , False],
    "Caio": ["aaaaaaaaaa@gmail.com" , 1222222 , True ]
}


print(usuariosCadastrados.keys())
print(usuariosCadastrados.values())

cliente.exibirusuarioscadastrados(usuariosCadastrados)






