package array

import "testing"

func TestQ3(t *testing.T) {
	res := q3("  Mr John Smith             ")
	if res != "Mr%20John%20Smith" {
		t.Error(res)
	}
}
