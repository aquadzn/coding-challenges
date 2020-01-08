import "sort"
func triangleExistence(t []int) bool {
    sort.Ints(t)
    return t[0] + t[1] > t[2]
}
