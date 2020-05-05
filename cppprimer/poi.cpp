
# include <iostream>
using namespace std;

void calcarea(const double* const pPi,const double*const pRadius,double *const pArea)
{
	if (pPi && pRadius && pArea)
		*pArea = (*pPi) * (*pRadius) * (*pRadius);
}

int main()
{
	const double Pi=3.1416;
	cout <<"enter radius of circle: ";
	double radius;
	cin >> radius;

	double Area =0;
	calcarea(&Pi,&radius,&Area);

	cout << "Area is "<<Area<<endl;

	return 0;
}