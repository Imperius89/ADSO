#include <iostream>

using namespace std;

int num1=12;
int num2=14;

bool booleana=true;

int main()
{
    if (num1 < num2)
    {
        cout << "Es menor" << endl;
    }
    else if (num1 == num2)
    {
        cout << "Valen lo mismo" << endl;
    }
    else 
    {
        cout << "No es  menor" << endl;
    }
    cin.get();
    return 0;
}