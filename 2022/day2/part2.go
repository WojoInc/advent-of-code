package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	choiceMap = map[string]int {
		"A": 1,
		"B": 2,
		"C": 3,
	}
	resultsMap = map[string]int {
		"X": 0,
		"Y": 3,
		"Z": 6,
	}
	// map holds all the possible outcomes since there aren't many
	// 1st key is the desired result, 2nd is opponents choice
	ruleMap = map[string]map[string]string {
		"X": {
			"A": "C",
			"B": "A",
			"C": "B",
		},
		"Y": {
			"A": "A",
			"B": "B",
			"C": "C",
		},
		"Z": {
			"A": "B",
			"B": "C",
			"C": "A",
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
		res := round[1]
		me := ruleMap[res][opp]
		myScore += (choiceMap[me] + resultsMap[res])
	}
	fmt.Printf("My total score: %d\n", myScore)
}