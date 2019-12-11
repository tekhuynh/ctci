package array

import "testing"

func TestQ4(t *testing.T) {
	s := "taro cat"
	res := q4(s)
	if res != false {
		t.Error(s)
	}
	s = "taco cat"
	res = q4(s)
	if res != true {
		t.Error(s)
	}
	s = "122333 "
	res = q4(s)
	if res != false {
		t.Error(s)
	}
	s = "122 4444"
	res = q4(s)
	if res != true {
		t.Error(s)
	}
	s = "22 4444 666666"
	res = q4(s)
	if res != true {
		t.Error(s)
	}
}
