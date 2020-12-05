package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

// get_input returns a slice of all input rows (not using csv reader because of https://github.com/golang/go/issues/39119)
func get_input() []string {
	file, _ := os.Open("input.csv")
	defer file.Close()
	input := []string{}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	file.Close()
	return input
}

func part1() int {

	var highestSeatId int

	for _, boardingPass := range get_input() {

		seatId := getSeatId(boardingPass)
		if seatId > highestSeatId {
			highestSeatId = seatId
		}
	}

	return highestSeatId
}

func part2() int {
	var seatId int

	seatIds := []int{}
	for _, boardingPass := range get_input() {
		seatId = getSeatId(boardingPass)
		seatIds = append(seatIds, seatId)
	}

	sort.Ints(seatIds)

	var prev int
	for i, id := range seatIds {
		if i != 0 && prev != id-1 {
			seatId = id - 1
			break
		}
		prev = id
	}
	return seatId
}

func getSeatId(boardingPass string) int {
	rows, cols := map[string]int{"min": 0, "max": 127}, map[string]int{"min": 0, "max": 7}

	for _, char := range strings.Split(boardingPass, "") {
		switch char {
		case "F":
			rows["max"] = rows["max"] - sep(rows["max"], rows["min"]) - 1
		case "B":
			rows["min"] = rows["min"] + sep(rows["max"], rows["min"]) + 1
		case "L":
			cols["max"] = cols["max"] - sep(cols["max"], cols["min"]) - 1
		case "R":
			cols["min"] = cols["min"] + sep(cols["max"], cols["min"]) + 1
		default:
			panic("Direction failed ?")
		}
	}

	if rows["max"] != rows["min"] || cols["max"] != cols["min"] {
		panic("Join point failed ?")
	}

	return (rows["max"] * 8) + cols["max"]
}

func sep(max int, min int) int {
	return ((max - min) / 2)
}

//run resolver
func main() {
	fmt.Printf("result of part 1 is %d\n", part1())
	fmt.Printf("result of part 2 is %d\n", part2())
}
