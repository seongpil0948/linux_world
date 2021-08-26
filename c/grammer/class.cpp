#include <iostream>

using namespace std;

// TODO: 생성자 함수 호출 안됌.
// TODO: vscode 자동 컴파일 Short cut  .
// TODO: multiline 주석 뭔데 ㅋㅋㅋ

class Login {
    private:
    char id[12];
    char pwd[20];
    char site[40];

    public:
    void print();
    void cin_site();
    void cin_id();
    void cin_pwd();
    void init();
};

void Login::init() {
  cout << "생성자 함수 호출";
}

// 만약 using space 없었다면 std::Login::print
void Login::print() {
  cout << "\n Site Name: " << site << "\n id: " << id << "\n Password: " << pwd << endl;
};

void Login::cin_site() {
  cout << "Input Site Name:  ";
  cin >> site;
};

void Login::cin_id() {
  cout << "Input ID:  ";
  cin >> id;
};
void Login::cin_pwd() {
  cout << "Input Password:  ";
  cin >> pwd;
};

int main() {
  Login intellisys;
  intellisys.cin_site();
  intellisys.cin_id();
  intellisys.cin_pwd();
  cout << "=======================";
  intellisys.print();
  return 0;
}