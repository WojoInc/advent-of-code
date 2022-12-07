package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	cur := 0
	elfNum := 0
	elves := [3]int{}
	fName := os.Args[1]
	f, _ := os.Open(fName)
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan(){
		if scanner.Text() == "" {
			cmp := cur
			for i := range(elves){
				if cmp >= elves[i]{
					temp := elves[i]
					elves[i] = cmp
					cmp = temp
				}
			}
			
			cur = 0
			elfNum++
			continue
		}
		temp, _ := strconv.Atoi(scanner.Text())
		cur += temp
	}
	sum := 0
	for i := range(elves){
		fmt.Printf("Top Elf %d is carrying %d calories\n", i, elves[i])
		sum += elves[i]
	}
	fmt.Printf("Total: %d\n", sum)
	f.Close()
}