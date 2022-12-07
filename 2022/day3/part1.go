package main

import (
	"bufio"
	"fmt"
	"os"
)


func main() {
	priSum := 0
	fName := os.Args[1]
	f, _ := os.Open(fName)
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan(){
		packSize := len(scanner.Text())
		pack := scanner.Text()
		foundSet := map[rune]bool{}
		for i := range(pack) {
			c := rune(pack[i])
			if i >= (packSize / 2) {
				if hit, exists := foundSet[c]; exists && ! hit {
					// If we're on the second compartment, check if we've already seen
					// this rune. Add to priority sum if so, but not if already included
					// in the sum
					foundSet[c] = true
					if c >= 97 {
						priSum += int(c - 96)
					} else {
						// skipping any error checking here, ideally we'd want to say
						// only do this for uppercase
						priSum += int(c - 38)
					}
				}
			} else {
				foundSet[c] = false
			}
		}

	}
	fmt.Printf("Sum of priorities: %d\n", priSum)
	f.Close()
}