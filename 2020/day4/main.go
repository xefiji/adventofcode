package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
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

//get_passports groups all passports line (skips empty or line feed)
func get_passports() map[int]string {
	passeports := map[int]string{}
	curline := 0
	for _, line := range get_input() {
		if line == "" {
			curline++
			continue
		}
		passeports[curline] = fmt.Sprintf("%s %s", passeports[curline], line)
	}
	return passeports
}

func part1() int {

	compulsary := map[string]bool{"cid": false, "byr": true, "iyr": true, "eyr": true, "hgt": true, "hcl": true, "ecl": true, "pid": true}
	totalValid := 0
	for _, passport := range get_passports() {
		parts := strings.Split(passport, " ")
		passportValid := 0
		for _, part := range parts {
			field := strings.Split(part, ":")[0]
			if is, ok := compulsary[field]; ok {
				if is == true {
					passportValid++
				}
			}
		}
		if passportValid == 7 {
			totalValid += 1
		}
	}
	return totalValid
}

func part2() int {

	patterns := map[string]string{
		"byr": `(?m)^(19[2-9][0-9]|200[0-2])$`,
		"iyr": `(?m)^(201[0-9]|2020)$`,
		"eyr": `(?m)^(202[0-9]|2030)$`,
		"hgt": `(?m)(^(15[0-9]|16[0-9]|17[0-9]|18[0-9]|19[0-3])cm$)|^((59|6[0-9]|7[0-6])in$)`,
		"hcl": `(?m)^(#[0-9a-f]{6})$`,
		"ecl": `(?m)^(amb|blu|brn|gry|grn|hzl|oth)$`,
		"pid": `(?m)^([0-9]{9})$`,
	}
	totalValid := 0

	for _, passport := range get_passports() {

		parts := strings.Split(strings.TrimSpace(passport), " ")
		passportValid := 0
		for _, part := range parts {

			tmp := strings.Split(part, ":")
			field := strings.TrimSpace(tmp[0])
			val := strings.TrimSpace(tmp[1])

			if pattern, ok := patterns[field]; ok {
				re := regexp.MustCompile(pattern)
				if true == re.MatchString(val) {
					passportValid++
				}
			}
		}
		if passportValid >= 7 {
			totalValid += 1
		}
	}
	return totalValid
}

//run resolver
func main() {
	fmt.Printf("result of part 1 is %d\n", part1())
	fmt.Printf("result of part 2 is %d\n", part2())
}
