// Mini Projeto 6 - Intensivo Dev Aprender
// https://www.youtube.com/watch?v=i6Oi-YtXnAU&list=PL75H3gordSHxMtVaiwKTRT9QrxEuWyFIB&index=1&t=10s

/* Criar um método para ler as propriedades de um objeto
 Exibir somente as propriedades do tipo string que existem nesse objeto */

const filme = {
    titulo: 'Vingadores',
    ano: 2018,
    diretor: 'Robin',
    personagem: 'Thor'
}
exibirPropriedades(filme);

function exibirPropriedades(obj) {
    for (prop in obj)
        if (typeof obj[prop] === 'string')
            console.log(prop, obj[prop])
}