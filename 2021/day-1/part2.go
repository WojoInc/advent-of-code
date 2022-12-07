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
	for i:=0; i < len(input)-3; i++{
		win1 := input[i] + input[i+1] + input[i+2]
		win2 := input[i+1] + input[i+2] + input[i+3]
		if win2 > win1 {count++}
	}
	fmt.Printf("Count %d\n", count)
}
