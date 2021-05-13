package main

func CalculateEvenFibonacciSum(n int) (sum int) {

	// formula for a fibonacci sequence is F(n)=F(n−1)+F(n−2)
	if n == 0 {
		return 0
	} else if n % 2 != 0 {
		return CalculateEvenFibonacciSum(n-1)
	} else {
		return n + CalculateEvenFibonacciSum(n-2)
	}

} 

