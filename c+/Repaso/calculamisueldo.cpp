#include <iostream>
using namespace std;

int main() {
	int horas, sueldo_por_hora, sueldo;
	cout << "Determinar el sueldo y la valoracion" << endl;
	cout << "Ingrese las horas trabajadas: ";
    cin >> horas;
    cout << "Ingrese el sueldo por hora: ";
    cin >> sueldo_por_hora;
    //logica
    sueldo = horas*sueldo_por_hora;
    cout << "El sueldo es: " << sueldo << endl;
    //comparativo
    if (sueldo < 1500) {
    	cout << "Escala baja";
	}
	if (sueldo > 1500 && sueldo < 3500) {
		cout << "Escala media";
	}
	if (sueldo > 3500) {
    	cout << "Escala alta";
	}
	return 0;
}
