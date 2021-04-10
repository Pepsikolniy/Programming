#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

const auto PI = 3.141592653589793;

class Point
{
private:
    double x;
    double y;
    enum CoordEnum { Cartesian, Polar };
public:
    Point(double a1 = 0, double a2 = 0, CoordEnum coord_system = Cartesian)
    {
        if (coord_system == Cartesian)
        {
            x = a1;
            y = a2;
        }
        else
        {
            x = cos(a2) * a1;
            y = sin(a2) * a1;
        }
    }
    bool operator == (Point other)
    {
        /* if ((std::abs(left.x - right.x) < pow(10, -10))&&(std::abs(left.x - right.x) < pow(10, -10)))
            return true;
        else
            return false; */
        return std::abs(this->x - other.x) < pow(10, -10) && std::abs(this->x - other.x) < pow(10, -10);
    }
    bool operator != (Point other)
    {
        /*if (!((std::abs(this->x - other.x) < pow(10, -10)) && (std::abs(this->x - other.x) < pow(10, -10))))
            return true;
        else
            return false;*/
        return !(std::abs(this->x - other.x) < pow(10, -10) && (std::abs(this->x - other.x) < pow(10, -10)));
    }
    friend std::ostream& operator<< (std::ostream& out, Point& point)
    {
        out << '(' << point.get_x() << ',' << point.get_y() << ')';
        return out;
    }
    friend std::istream& operator>> (std::istream& in, Point& point)
    {
        double temp;
        in.ignore(1);
        in >> temp;
        point.set_x(temp);
        in.ignore(1);
        in >> temp;
        point.set_y(temp);
        in.ignore(1);
        return in;
    }
    double get_x() { return x; }
    double get_y() { return y; }
    double get_r() { return sqrt(x * x + y * y); }
    double get_phi() { return atan2(y, x); }
    void set_x(double x) { this->x = x; }
    void set_y(double y) { this->y = y; }
    void set_r(double r) {
        auto phi = get_phi();
        x = cos(phi) * r;
        y = sin(phi) * r;
    }
    void set_phi(double phi) {
        auto r = get_r();
        x = cos(phi) * r;
        y = sin(phi) * r;
    }

};
// Ваш код тут

int main() {
    std::vector<Point> original;
    std::ifstream fin("data.txt");
    if (!fin.is_open()) {
        std::cout << "Can't open file" << std::endl;
        return 1;
    }
    else {
        while (!fin.eof()) {
            Point p;
            fin >> p;
            fin.ignore(2); // Точки разделены двумя символами ", "
            original.push_back(p);
        }
        fin.close();
    }

    std::vector<Point> simulacrum(original);
    for (auto& p : simulacrum) {
        std::cout << p;
        p.set_x(p.get_x() + 10);
        p.set_phi(p.get_phi() + 180 * PI / 180);
        p.set_y(-p.get_y());
        p.set_x(-p.get_x() - 10);
        std::cout << p << std::endl;
    }

    if (std::equal(original.begin(), original.end(), simulacrum.begin()))
        std::cout << "\nIt works!\n";
    else
        std::cout << "\nIt not works!\n";
}
