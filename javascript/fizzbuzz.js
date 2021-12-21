// Mini Projeto 3 - Intensivo Dev Aprender
// https://www.youtube.com/watch?v=i6Oi-YtXnAU&list=PL75H3gordSHxMtVaiwKTRT9QrxEuWyFIB&index=1&t=10s

//Divisível por 3 => Fizz
//Divisível por 5 => Buzz
//Divisível por 3 e 5 => FizzBuzz
//Não divisível por 3 ou 5 => entrada
//Não é um número => 'Não é um número'

const resultado = fizzBuzz(3);
console.log(resultado);

function fizzBuzz(entrada) {
    if (typeof entrada !== 'number')
        return 'Não é um número';
    if (entrada % 3 === 0 && entrada % 5 === 0)
        return 'FizzBuzz';
    if (entrada % 3 === 0)
        return 'Fizz';
    if (entrada % 5 === 0)
        return 'Buzz';

    return entrada;
}