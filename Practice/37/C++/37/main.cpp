#include <iostream>
#include <cmath>

using namespace std;

double sqr(double a);
bool equal(double a, double b, double e = 1E-10);

class Vector;

class Point
{
    friend Vector;
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

class Vector
{
Point point;

public: 
    Vector (): point(1,0){}
    Vector (const Point& end): point(end.x, end.y) {}
    Vector (const Point& begin, const Point& end): point(end.x - begin.x, end.y - begin.y) {}

    bool operator==(Vector other)
    {
        return point == other.point;
    }
    Vector operator-()
    {
        Point p = point;
        p.set_x(-p.x);
        p.set_y(-p.y);
        return Vector(p);
    }
    Vector operator+(Vector other)
    {
        Point p;
        p.set_x(point.x + other.point.x);
        p.set_y(point.y + other.point.y);
        return Vector(p);
    }
    Vector operator-(Vector other)
    {
        Point p;
        p.set_x(point.x - other.point.x);
        p.set_y(point.y - other.point.y);
        return Vector(p);
    }
    Vector operator*(double num)
    {
        Point p = point;
        p.set_x(p.x*num);
        p.set_y(p.y*num);
        return Vector(p);
    }
    double length()
    {
        return point.get_r();
    }
    double operator*(Vector other)
    {
        double scalar = length() * other.length() * cos(point.get_phi() - other.point.get_phi());
        return scalar;
    }
};

int main()
{
    Vector a(Point(1, 2)), b(Point(-2, 0), Point(-1, 2));
    if (a == b && b == a) cout << "Equality test passed\n";
    else cout << "Equality test failed\n";

    Vector na(Point(-1, -2)), ox(Point(1, 0)), nox(Point(-1, 0)), oy(Point(0, 1)), noy(Point(0, -1));
    if (a == -na && na == -a && -ox == nox && -oy == noy) cout << "Invert test passed\n";
    else cout << "Invert test failed\n";

    if (ox + oy + oy == a && -ox == -a + oy + oy) cout << "Summation test passed\n";
    else cout << "Summation test failed\n";

    if (-ox + oy == oy - ox && -oy + ox == ox - oy) cout << "Subtraction test passed\n";
    else cout << "Subtraction test failed\n";

    if (ox * 3 == ox + ox + ox &&
        oy * 3 == oy + oy + oy &&
        ox * (-3) == -ox - ox - ox &&
        oy * (-3) == -oy - oy - oy) cout << "Multiplication by number test passed\n";
    else cout << "Multiplication by number test failed\n";

    if (equal(ox.length(), 1) &&
        equal(oy.length(), 1) &&
        equal((ox * 3 + oy * 4).length(), 5)) cout << "Length test passed\n";
    else cout << "Length test failed\n";

    if (equal(ox*ox, sqr(ox.length())) &&
        equal(oy*oy, sqr(oy.length())) &&
        equal((ox*3 + oy*4)*(ox*3 + oy*4), sqr((ox*3 + oy*4).length()))) cout << "Multiplication by Vector test passed\n";
    else cout << "Multiplication by Vector test failed\n";
}

bool equal(double a, double b, double e) {
    if (-e < a - b && a - b < e) return true;
    else return false;
}

double sqr(double a) {
    return a * a;
}
