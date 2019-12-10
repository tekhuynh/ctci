package array

import "testing"

func TestQ1(t *testing.T) {
	inputs := []string{
		"",
		"a",
		"aa",
		"apple",
		"analyst",
		"artsy",
		"1",
		"123",
		"121",
		"11",
		"0",
	}
	outputs := []bool{
		true,
		true,
		false,
		false,
		false,
		true,
		true,
		true,
		false,
		false,
		true,
	}

	for i := 0; i < len(inputs); i++ {
		if q1(inputs[i]) != outputs[i] {
			t.Errorf("q1 error for %s", inputs[i])
		}
		if q1a(inputs[i]) != outputs[i] {
			t.Errorf("q1a error for %s", inputs[i])
		}
	}
}
