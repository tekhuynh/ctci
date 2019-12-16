package array

import "testing"

func TestQ6(t *testing.T) {
	s := q6("aaaa")
	if s != "a4" {
		t.Error(s)
	}
	s = q6("aa")
	if s != "aa" {
		t.Error(s)
	}
	s = q6("aabbb")
	if s != "a2b3" {
		t.Error(s)
	}
}
