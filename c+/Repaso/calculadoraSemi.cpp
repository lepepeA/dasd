#include <iostream>
using namespace std;

int main() {
	int numero;
	cout << "Determinar si un numero es positivo o negativo" << endl;
	cout << "Ingrese el numero: ";
    cin >> numero;
    if (numero == 0) {
    	cout << "El 0 no tiene signo";
	} else {	
	    if (numero > 0) {
	    	cout << "El numero es positivo" << endl;;	
		} else {
			cout << "El numero es negativo" << endl;;	
		}	
	}
	if (numero & 2 == 0) {
		cout << "El numero es par" << endl;
	} else {
		cout << "El numero es impar" << endl;
	}
	return 0;
}
