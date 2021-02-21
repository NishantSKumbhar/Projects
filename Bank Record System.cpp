#include<iostream>
#include<fstream>
using namespace std;


class account_query{
    private:
        char account_number[20];
        char firstName[10];
        char lastName[10];
        float tota_Balance;

    public:
        void read_data();
        void show_data();
        void write_rec();
        void read_rec();
        void search_rec();
        void edit_rec();
        void delete_rec();

};

void account_query::read_data(){
    cout<<"\nEnter the account Number : ";
    cin>>account_number;
    cout<<"\nEnter the First Name : ";
    cin>>firstName;
    cout<<"\nEnter the Last Name : ";
    cin>>lastName;
    cout<<"Enter the Balance : ";
    cin>>tota_Balance;
    cout<<endl;
}

void account_query::show_data(){
    cout<<"//////////////////////////////////////////////////////////////"<<endl;
    cout<<"Account Number               : "<<account_number<<endl;
    cout<<"First Name of Account Holder : "<<firstName<<endl;
    cout<<"Last Name of Account Holder  : "<<lastName<<endl;
    cout<<"Current Balance              : "<<tota_Balance<<endl;
    cout<<"//////////////////////////////////////////////////////////////"<<endl;
}

void account_query :: write_rec(){
    ofstream outfile;



}

int main(){
    account_query A;
    int choice;
    cout<<"///////////////// Account Information System /////////////////"<<endl;
    while(true){
        cout<<"Select one Option Below "<<endl;
        cout<<"Click -> 1 : Add Record to File."<<endl;
        cout<<"Click -> 2 : Show Record from File."<<endl;
        cout<<"Click -> 3 : Search Record from File."<<endl;
        cout<<"Click -> 4 : Update Record."<<endl;
        cout<<"Click -> 5 : Delete Record."<<endl;
        cout<<"Click -> 6 : Quit the Program / Leave ."<<endl;
        cout<<"Enter Your Choice :  "<<endl;
        cin>>choice;

    }

    return 0;
}
