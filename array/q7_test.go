package array

import "testing"

func TestQ7(t *testing.T) {
	a := [][]int32{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	// b := [][]int32{
	// 	{7, 4, 1},
	// 	{8, 5, 2},
	// 	{9, 6, 3},
	// }
	q7(a)
	t.Error(a)
}
