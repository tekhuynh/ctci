package array

import (
	"sort"
	"strings"
)

func q2(s1 string, s2 string) bool {

	if len(s1) != len(s2) {
		return false
	}

	s1letters := strings.Split(s1, "")
	s2letters := strings.Split(s2, "")
	sort.Strings(s1letters)
	sort.Strings(s2letters)

	for i := 0; i < len(s1); i++ {
		if s1letters[i] != s2letters[i] {
			return false
		}
	}
	return true
}
