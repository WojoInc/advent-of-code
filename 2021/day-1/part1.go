package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, _ := os.Open(os.Args[1])
	s := bufio.NewScanner(f)
	s.Split(bufio.ScanLines)
	var input []int64
	for s.Scan() {
		i, _ := strconv.ParseInt(s.Text(), 0, 64)
		input = append(input, i)
	}
	count := 0
	last := input[0]
	for _, e := range(input){
		if e > last{count++}
		last = e
	}
	fmt.Printf("Count %d\n", count)
}
