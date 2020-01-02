// std::string greetPerson(std::string n) {
//     std::string s = "Hello, ";
//     return s += n;
// }

auto greetPerson(auto n) {
    return "Hello, " + n;
}