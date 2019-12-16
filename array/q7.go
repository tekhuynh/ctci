package array

func q7(a [][]int32) {
	max := len(a)
	mid := max / 2
	for i := 0; i < max; i++ {
		for j := i + 1; j < max; j++ {
			a[i][j], a[j][i] = a[j][i], a[i][j]
		}
	}
	for i := 0; i< len(a); i++ {
		for j :=0; j < mid; j++ {
			a[i][j], a[i][max -1 - j] = a[i][max -1 - j], a[i][j]
		}
	}
}
