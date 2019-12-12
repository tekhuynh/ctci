package array

import "strings"

func q5(s1, s2 string) bool {

	s1runes := strings.Split(s1, "")
	s2runes := strings.Split(s2, "")
	s1len := len(s1runes)
	s2len := len(s2runes)

	diff := s1len - s2len
	switch {
	case diff < -1:
		return false
	case diff > 1:
		return false
	}

	edits := 0
	for s1ptr, s2ptr := 0, 0; s1ptr < s1len; {

		if s1runes[s1ptr] == s2runes[s2ptr] {
			s1ptr++
			s2ptr++
			continue
		}
		edits++

		if s1len > s2len {
			s1ptr++
		} else if s1len == s2len {
			s1ptr++
			s2ptr++
		} else {
			s2ptr++
		}
	}

	if edits == 0 && s1len < s2len {
		return true
	} else if edits == 1 {
		return true
	} else {
		return false
	}
}
