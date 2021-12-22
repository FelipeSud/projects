// Mini Projeto 7 - Intensivo Dev Aprender
// https://www.youtube.com/watch?v=i6Oi-YtXnAU&list=PL75H3gordSHxMtVaiwKTRT9QrxEuWyFIB&index=1&t=10s

// Criar função somar que retorna a soma de todos os múltiplos de 3 e 5

somar(10);

function somar(limite) {
    let multiplosDe3 = 0;
    let multiplosDe5 = 0;
    for (i = 0; i <= limite; i++) {
        if (i % 3 === 0)
            multiplosDe3 += i;
        if (i % 5 === 0)
            multiplosDe5 += i;
    }
    console.log(multiplosDe3 + multiplosDe5);
}