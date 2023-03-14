//let x = 4;

//console.log ("x: ", x);

const lista = [1, 2, 3];
lista.push(4);
console.log(lista);

// oggetto
const homer = {
    first: "Homer",
    last: "Simpson"
};
console.log(homer);

//function stampa(elem) {
//    console.log(elem);
//}
lista.forEach(function (elem) {
    console.log(elem);
});

lista.forEach((elem) => console.log(elem));


// map, filter, reduce

const pari = [0, 2, 4, 6];
const dispari= pari.map((elem) => elem+1);
console.log("dispari", dispari);

const mag5 = pari.filters((elem) => elem > 5);
console.log("mag5", mag5);

const somma = numbers.reduce((prev, curr) => prev+curr, 0);
console.log("somma", somma);


