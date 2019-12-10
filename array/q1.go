package array

import "strings"
import "sort"

// q1 return true if string is unique and false otherwise
func q1(s string) bool {
	h := make(map[rune]bool)
	for _, r := range s {
		if h[r] {
			return false
		}
		h[r] = true
	}
	return true
}

// no data structures
func q1a(s string) bool {
	letters := strings.Split(s, "")
	sort.Strings(letters)
	for i := 0; i < len(letters)-1; i++ {
		if letters[i] == letters[i+1] {
			return false
		}
	}
	return true
}
