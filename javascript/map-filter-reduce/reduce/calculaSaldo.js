function calculaSaldo(saldo, itens) {
	if (!saldo || !itens || !itens.length) return 'Envie todos os parâmetros';

	const saldoFinal = itens.reduce((acc, item) => acc - item.preco, saldo);

	return `O saldo final será de ${saldoFinal} reais`;
}

lista = [
	{
		preco: 2,
		nome: 'leite',
	},
	{
		preco: 30,
		nome: 'carne',
	},
	{
		preco: 25,
		nome: 'frango',
	},
];

saldo = 100;

console.log(calculaSaldo(saldo, lista));
