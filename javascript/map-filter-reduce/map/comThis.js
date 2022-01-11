const lemon = {
	price: 2,
};

const strawberry = {
	price: 1.5,
};

function mapArray() {
	const array = [1, 2, 3, 4, 5];

	return array.map(function (item) {
		return item * this.price;
	}, lemon);
}

console.log(mapArray());
