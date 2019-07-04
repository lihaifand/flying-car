#include "gc_pointer.h"
#include "LeakTester.h"

int main()
{
    Pointer<int> p = new int(19);
    // std::cout<<"1"<<p << "is" << *p <<std::endl;
    p = new int(21);
    // std::cout<<"2"<<p << "is" << *p <<std::endl;
    p = new int(28);
    Pointer<int, 2> p1 = new int[2];
    p1 = new int[2];
    // std::cout<<"3"<<p << "is" << *p <<std::endl;
    // p = new int[3];
    // std::cout<<"4"<<p << "is" << *p <<std::endl;
    // p.collect();
    // std::cout<<"5"<<p << "is" << *p <<std::endl;
    return 0;
}