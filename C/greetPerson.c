// char * greetPerson(char * n) {
//
// }

greetPerson(n) {
    char * s = malloc(strlen(n) + 8);
    return strcat(strcpy(s, "Hello, "), n);
}