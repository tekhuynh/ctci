package array

import (
	"fmt"
	"strings"
)

func q6(s string) string {
	var sb strings.Builder
	runeCount := 1
	currRune := rune(0)

	for _, r := range s {
		if r == currRune {
			runeCount++
			continue
		}
		if currRune == 0 {
			currRune = r
			continue
		}
		sb.WriteRune(currRune)
		fmt.Fprintf(&sb, "%d", runeCount)
		runeCount = 1
		currRune = r
	}
	sb.WriteRune(currRune)
	fmt.Fprintf(&sb, "%d", runeCount)
	res := sb.String()

	if len(res) < len(s) {
		return res
	}
	return s
}
