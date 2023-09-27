#include <iostream>
using namespace std;

int main() {
	double num1, num2, resultado;
	char operador;
    cout << "Division C++" << endl;
    cout << "Ingrese el primer numero: ";
    cin >> num1;
    cout << "Ingrese el operador (+, -, *, /): ";
    cin >> operador;
    cout << "Ingrese el segundo numero: ";
    cin >> num2;
        
    switch (operador) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                resultado = num1 / num2;
            } else {
                cout << "Error: No se puede dividir por cero." << endl;
            }
            break;
        default:
            cout << "Operador no válido." << endl;
	}
    /*
    if (operador == '+') {
    	resultado = num1+num2;
	}
	if (operador == '-') {
		resultado = num1-num2;
	}
	if (operador == '*') {
		resultado = num1*num2;
	}
	if (operador == '/') {
		if (num2 != 0) {
			resultado = num1/num2;
		}
	}*/
    cout << "El resultado es: " << resultado;
    return 0;
}
