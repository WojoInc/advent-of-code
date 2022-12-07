package main

import (
	"bufio"
	"fmt"
	"os"
)

// FIFO queue
type Queue[T rune] struct {
	Limit int
	Elem []T
	weights map[T]int
	Weight int
}

// Checks that the total queue wait is equal to the
// current queue length.
// For example in a full queue of 4 with 2 duplicate elements,
// total weight is calculated as 1 + (1 + 2) + 1 + 1 for a weight of 5
func (q *Queue[T]) isUnique() bool{
	return q.Weight == len(q.Elem)
}

func (q *Queue[T]) Push(e T) {
	if len(q.Elem) >= q.Limit {
		// We've hit the queue limit, so need to pop first element off
		// before adding new
		temp := make([]T,0)
		// Remove the current weight of element from total
		q.Weight -= q.weights[q.Elem[0]]
		// Decrease the weight for the removed rune
		q.weights[q.Elem[0]]--
		// Append new item
		temp = append(temp, q.Elem[1:q.Limit]...)
		temp = append(temp, e)
		q.Elem = temp
	}else {
		q.Elem = append(q.Elem, e)
	}
	// Check if already in set, create if not
	if _, exists := q.weights[e]; !exists {
		q.weights[e] = 1
	} else {
		// Increment the rune's weight
		q.weights[e]++
	}
	// Add the rune's weight to the total
	// each time we increase the weight of a rune, we add it to the total
	// AFTERWARDS. Such that for a rune that appears 3 times,
	// we have (1) + (1 + 2) + (1 + 2 + 3)
	// We perform the reverse when removing a rune from the queue
	q.Weight += q.weights[e]
	
}

func main() {
	count := 0
	fName := os.Args[1]
	f, _ := os.Open(fName)
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanRunes)
	// Change limit here to 4 for part 1
	q := Queue[rune]{Limit:14, Elem: []rune{}, weights: map[rune]int{}, Weight: 0}
	for scanner.Scan(){
		r := []rune(scanner.Text())[0]
		q.Push(r)
		count++
		// Wait til queue is full
		if count < 4 {continue} 
		// Check if unique, break loop if true
		if q.isUnique() {break}
	}
	fmt.Printf("Start of packet after: %d\n", count)
	f.Close()
}