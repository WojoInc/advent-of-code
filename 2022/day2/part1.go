package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	letterMap = map[string]int {
		"X": 1,
		"Y": 2,
		"Z": 3,
	}
	// map holds all the possible outcomes since there aren't many
	// 1st key is our choice, 2nd is opponents choice
	ruleMap = map[string]map[string]int {
		"X": {
			"A": 3,
			"B": 0,
			"C": 6,
		},
		"Y": {
			"A": 6,
			"B": 3,
			"C": 0,
		},
		"Z": {
			"A": 0,
			"B": 6,
			"C": 3,
		},
	}
)

func main() {
	fName := os.Args[1]
	f, _ := os.Open(fName)
	myScore := 0
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan(){
		round := strings.Split(scanner.Text(), " ")
		opp := round[0]
		me := round[1]
		myScore += ruleMap[me][opp] + letterMap[me]
	}
	fmt.Printf("My total score: %d\n", myScore)
}