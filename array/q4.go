package array

import "unicode"

func q4(s string) bool {
	charCounts := make(map[rune]int)
	numChars := 0
	for _, char := range s {
		if !unicode.IsSpace(char) {
			charCounts[char]++
			numChars++
		}
	}

	numOdd := 0
	for _, v := range charCounts {
		if isOdd(v) {
			numOdd++
		}
	}

	if numOdd == 0 {
		return true
	}
	if numOdd == 1 && isOdd(numChars) {
		return true
	}
	return false
}

func isOdd(i int) bool {
	return i%2 == 1
}
