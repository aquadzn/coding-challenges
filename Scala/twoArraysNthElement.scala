def twoArraysNthElement(a: Seq[Int], b: Seq[Int], n: Int): Int = {
    val c = (a ++ b).sorted
    c(n)
}