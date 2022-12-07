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

	for scanner.Scan() {
		packs := [3]string{
			scanner.Text(),
			func() string { scanner.Scan(); return scanner.Text() }(),
			func() string { scanner.Scan(); return scanner.Text() }(),
		}

		packMaps := [3]map[rune]interface{}{
			make(map[rune]interface{}), 
			make(map[rune]interface{}), 
			make(map[rune]interface{}),
		}
		for p := range packs {
			for i := range packs[p] {
				r := rune(packs[p][i])
				packMaps[p][r] = nil
			}
		}
		for i := range packMaps[0] {
			if _, found1 := packMaps[1][i]; !found1 {
				continue
			}
			if _, found2 := packMaps[2][i]; !found2 {
				continue
			}
			if i >= 97 {
				priSum += int(i - 96)
			} else {
				// skipping any error checking here, ideally we'd want to say
				// only do this for uppercase
				priSum += int(i - 38)
			}
			break
		}

	}
	fmt.Printf("Sum of priorities: %d\n", priSum)
	f.Close()
}
