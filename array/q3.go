package array

import "strings"

func q3(s string) string {
	result := strings.TrimSpace(s)
	result = strings.ReplaceAll(result, " ", "%20")
	return result
}
