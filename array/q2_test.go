package array

import "testing"

func TestQ2(t *testing.T) {
	in := [][]string{
		[]string{"", ""},
		[]string{"a", "a"},
		[]string{"a", "b"},
		[]string{"1", "1"},
		[]string{"1", "2"},
		[]string{"ab", "ba"},
		[]string{"aab", "baa"},
		[]string{"abc", "abb"},
		[]string{"love", "evol"},
		[]string{"a", "ab"},
		[]string{"ab", "a"},
		[]string{"c", "ab"},
		[]string{"ab", "c"},
	}

	out := []bool{
		true,
		true,
		false,
		true,
		false,
		true,
		true,
		false,
		true,
		false,
		false,
		false,
		false,
	}

	for i := 0; i < len(in); i++ {
		if q2(in[i][0], in[i][1]) != out[i] {
			t.Errorf("%s %s %v", in[i][0], in[i][1], out[i])
		}
	}
}
