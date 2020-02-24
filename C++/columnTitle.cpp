auto columnTitle(int n) {
   string r;

   while (n) {
	   r = char(--n % 26 + 65) + r;
	   n /= 26;
   }

   return r;
}
