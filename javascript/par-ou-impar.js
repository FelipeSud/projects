// Mini Projeto 5 - Intensivo Dev Aprender
// https://www.youtube.com/watch?v=i6Oi-YtXnAU&list=PL75H3gordSHxMtVaiwKTRT9QrxEuWyFIB&index=1&t=10s

/* Receber uma quantidade de valores para avaliar
Função exibe se cada valor é par ou ímpar */

exibirTipo(5);

function exibirTipo(limite) {
    for (let i = 0; i <= limite; i++) {
        if (i % 2 === 0)
            console.log(i, 'PAR');
        else
            console.log(i, 'ÍMPAR');
    }
}