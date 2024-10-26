package Assignment;
import java.util.ArrayList;

public class assignmentTest 
{
    public static void main(String[] args) 
    {
//ArrayList object
        ArrayList <Animal> animals = new ArrayList<>();


//Object declaration 
        Date Tdate = new Date(4, 10, 2023);
        Date date = new Date(3, 03, 2023);
        
        //animal's objects
        Animal a = new Animal("Cow", "An-123", "white", 500.0 , 400.0, date , 5000 , false);
        Animal a1 = new Animal("Cow", "An-124", "white", 2000.0 , 400.0, date , 5000 , false);
        
        //Dealer's objects
        Dealer d = new Dealer("Wasiq Tanveer", "14301-2345867-6", "Seni Gumabt", "0345-9655464", 10.0, a, animals);
        Dealer d1 = new Dealer("Wasiq Tanveer", "14301-2345867-6", "Seni Gumabt", "0345-9655464", 10.0, a1, animals);
        
        //seller's objects
        Seller s = new Seller("Imran Khan", "14301-2354965-7", "Peshawar", "0335-3344545", 25.0, 17.0, a);
        Seller s1 = new Seller("Imran Khan", "14301-2354965-7", "Peshawar", "0335-3344545", 25.0, 17.0, a1);
        
        //buyer's objects
        Buyer b = new Buyer("Nazim Ullah", "14301-1232353-2", "Islamabad","0349-2354569", a  , Tdate);
        Buyer b1 = new Buyer("Nazim Ullah", "14301-1232353-2", "Islamabad","0349-2354569", a1, Tdate);
        
        //invoice objects
        Invoice i = new Invoice(b, d, a, s);
        Invoice i1 = new Invoice(b1, d1, a1, s1);

       
//making an array that print details in loop
/*since all the classes implement a common interface
(ManageFinance)there for we use MaintainFinance in the loop 
so that we can access their objects through the interface*/

        MaintainFinance [] loop = {i, i1};

        for(MaintainFinance j : loop)
        {
                System.out.println(j.toString());
        }

        // d1.manageFinance();
        


//declaring animals objects
        Animal animal1 = new Animal("goat", "An-153", "Light Brown", 150.0 , 400.0, date , 5000 , false);
        Animal animal2 = new Animal("sheep", "An-145", "Brown", 110.0 , 400.0, date , 5000 , false);
        Animal animal3= new Animal("camel", "An-134", "Black", 990.0 , 400.0, date , 5000 , false);
        

//adding animals objects to dealers Array list
        animals.add(animal1);
        animals.add(animal2);
        animals.add(animal3);


// Printing all the added animals
        //d.displayObjects();



 //adding animal
        //d.addAnimal(animal3);



//checking the animal's avalibility
        //System.out.println(d.contains("An-153"));



//printing all the objects individually
        // System.out.println(d);
        // System.out.println(a);
        // System.out.println(s);
        // System.out.println(b);

//printing all the info including invoice
        // System.out.println(i);
       
    }    
}
