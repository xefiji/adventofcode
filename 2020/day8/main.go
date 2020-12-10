package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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

	input := get_input()
	acc := 0
	passed := make(map[int]struct{})

	i := 0
	for {
		if i >= len(input) {
			break
		}

		if _, ok := passed[i]; ok && i > 0 {
			break
		}

		parts := strings.Split(input[i], " ")
		action, val := parts[0], parts[1]

		to := 1
		passed[i] = struct{}{}

		switch action {
		case "nop":
			//
		case "acc":
			val, _ := strconv.Atoi(val)
			acc += val
		case "jmp":
			to, _ = strconv.Atoi(val)
		}

		i += to
	}

	return acc
}

func part2(input []string, j int) int {
	acc := 0
	passed := make(map[int]struct{})

	i := 0
	for {
		if i >= len(input) {
			return acc
		}

		if _, ok := passed[i]; ok && i > 0 {

			var newInput []string
			var modified string

			if input[j][0:3] == "nop" || input[j][0:3] == "jmp" {
				for k, original := range get_input() {
					if k == j {
						if input[j][0:3] == "nop" {
							modified = fmt.Sprintf("jmp %s", input[j][4:])
						} else if input[j][0:3] == "jmp" {
							modified = fmt.Sprintf("nop %s", input[j][4:])
						}
						newInput = append(newInput, modified)
					} else {
						newInput = append(newInput, original)
					}
				}
			} else {
				newInput = get_input()
			}
			j++

			return part2(newInput, j)
		}

		parts := strings.Split(input[i], " ")
		action, val := parts[0], parts[1]

		to := 1
		passed[i] = struct{}{}

		switch action {
		case "nop":
			//
		case "acc":
			val, _ := strconv.Atoi(val)
			acc += val
		case "jmp":
			to, _ = strconv.Atoi(val)
		}

		i += to
	}

	return acc
}

//run resolver
func main() {
	fmt.Printf("result of part 1 is %d\n", part1())
	fmt.Printf("result of part 2 is %d\n", part2(get_input(), 1))
}
