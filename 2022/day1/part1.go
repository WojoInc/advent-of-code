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
	highest := 0
	fName := os.Args[1]
	f, _ := os.Open(fName)
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan(){
		if scanner.Text() == "" {
			if cur >= highest{
				highest = cur
			}
			cur = 0
			elfNum++
			continue
		}
		temp, _ := strconv.Atoi(scanner.Text())
		cur += temp
	}
	fmt.Printf("Elf number: %d, is carrying %d calories\n", elfNum, highest)
	f.Close()
}