#include <iostream>
using namespace std;

int main() {
	//declarar variables
	double temperatura, probabilidad, cantidad;
	//ingresar variables
	cout << "Debo lavar Ropa?" << endl;
	cout << "Ingrese la temperatura del dia: ";
    cin >> temperatura;
    cout << "Ingrese la probabilidad de Shuvia: ";
    cin >> probabilidad;
    cout << "Ingrese la cantidad de ropa: ";
    cin >> cantidad;
	//logica
	if (temperatura > 17) {
		if (probabilidad < 35) {
			if (cantidad < 4 || cantidad == 4) {
				cout << "lava Ahorita";
			} else {
				cout << "Hay demasiada ropa";
			}
		} else {
			cout << "Puede que llueva NO lavo";
		}
	}
	else {
		cout << "hace mucho frio no lavo";
	}
	
	return 0;
}
