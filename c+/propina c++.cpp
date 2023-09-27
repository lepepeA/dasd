#include <iostream>
using namespace std;
int main () {
	double gasto, prop, propina;
	string siono, yes, no;
	cout << "Contador de propinas pero en c++" << endl;
	cout << "ingrese la cantidad de dinero que debe: " << endl;
	cin >> gasto;
	cout << "su gasto completo seria: " << gasto << " desea dar propina? (yes/no) " << endl;
	cin >> siono;
	if (siono == "yes"){
		cout << "indique la cantidad de porcentaje que quiere dejar como propina: ";
		cin >> prop;
		propina = gasto * ( prop / 100);
		cout << "Su gasto total sera: " << gasto + propina << " juntando su gasto y propina.";
		cout << "Sus gastos individuales seran: " << gasto << " y " << propina << endl;
	} else { if  (siono == "no") {
		cout << "gratis tenga buen dia" << endl;
}
		}
		cout << "elpepe" << endl;		
	} 


