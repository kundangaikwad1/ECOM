function
PrimeCheck(candidate)
{

    var
isPrime = true;
var
i = 2;
while (i < candidate){
if (candidate %i == = 0){
i = candidate;
isPrime = false;
}
i++;
}
return isPrime;
}

var
numPrimes = prompt("How many primes?");
var
j = 2;
while (primeArray.length < numPrimes){
if (PrimeCheck(j)){
primeArray.push(j);
}
j++;
}

console.log(primeArray);