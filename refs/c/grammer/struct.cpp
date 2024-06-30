struct Member1 {
    char name;
    int age;

    void init(char name, int age) {
        this->name = name;
        this->age = age;
    }
};

struct Member2 {
    char name[10];
    int age[5];
};

struct Member1 suheon;
struct Member2 spchoi {"성필", 27};

void main() {
    char name[10] = "수헌";
    suheon.init(*name, 26);
}