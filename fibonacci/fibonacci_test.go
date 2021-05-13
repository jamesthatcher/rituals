package main


import "testing"

func Test_calculateEvenFibonacciSum(t *testing.T) {
        type args struct {
                n int
        }
        tests := []struct {
                name    string
                args    args
                wantSum int
        }{
                {"Sums n = 100", args{100}, 3736710778780434371},
        }
        for _, tt := range tests {
                t.Run(tt.name, func(t *testing.T) {
                        if gotSum := CalculateEvenFibonacciSum(tt.args.n); gotSum != tt.wantSum {
                                t.Errorf("calculateEvenFibonacciSum() = %v, want %v", gotSum, tt.wantSum)
                        }
                })
        }
}