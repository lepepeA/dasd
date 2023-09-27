#include <iostream>
using namespace std;

int main() {
    double num1, num2, resultado;
    char operador;
cout << "dar el primer numero para una operacion: ";
cin >> num1;
cout << "dar el segundo numero para la operacion: ";
cin >> num2;
cout << "dar el operador que quieras: ";
cin >> operador;

switch (operador) {
    case '+':
    resultado = num1 + num2;
    break;
case '-':
resultado = num1 - num2;
break;

case '*':
resultado = num1 *num2;

case '/':
if (num2 != 0) {

resultado = num1 / num2; 
}
else {
	cout << "no se puede dividir por cero " << endl;
}
break;
default:
	cout << "operador no valido" << endl;
	

}
cout << "el resultado es " << resultado;
}

