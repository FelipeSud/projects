// Mini Projeto 4 - Intensivo Dev Aprender
// https://www.youtube.com/watch?v=i6Oi-YtXnAU&list=PL75H3gordSHxMtVaiwKTRT9QrxEuWyFIB&index=1&t=10s

/* Velocidade máxima de até 70
A cada 5km acima do limite você ganha 1 ponto
Math.Floor()
Caso os pontos sejam maior que 12 mostrar "Carteira Suspensa" */

verificarVelocidade(200);

function verificarVelocidade(velocidade){
    const velocidadeMaxima = 70;
    const kmPorPonto = 5;
    const limitePontos = 12
    if (velocidade <= velocidadeMaxima)
        console.log('Ok');
    else {
     const pontos = Math.floor(((velocidade - velocidadeMaxima)/ kmPorPonto));
     if (pontos >= limitePontos)
     console.log('Carteira Suspensa');
     else
     console.log('Pontos', pontos);
    }
}