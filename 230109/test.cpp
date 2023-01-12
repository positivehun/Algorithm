#include <iostream> //stdio.h printf scanf 
using namespace std; // std::cout
int main(void)
{
  int N = 10;
  int score;
  for (int i = 0; i < N; i++)
  {
    cin >> score;
    cout << "입력받은 점수는 "<<score<<"점 입니다.";
  }
}
