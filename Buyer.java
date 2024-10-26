package Assignment;

public class Buyer extends Person 
{
    private Animal animal;
    private Date transactionDate;
    public Buyer(String name , String id , String address , String contact , Animal animal , Date transactionDate)
    {
        super(name, id, address, contact);
        this.animal = animal;
        this.transactionDate = transactionDate;
    }
    
    public Animal getAnimal() 
    {
        return animal;
    }
    public void setAnimal(Animal animal) 
    {
        this.animal = animal;
    }


    public Animal gettransactionDate() 
    {
        return animal;
    }
    public void settransactionDate(Animal animal) 
    {
        this.animal = animal;
    }

    
    //method to calculate the total amount to be paid
    public double dueAmount()
    {
        return animal.getServicesCharges() + animal.price();
    }


    // it is a commom method that keeps track of the finance of each class
    //not added in to string method can only be shown when specifically called 
    public void manageFinance()
    {
        System.out.printf("%-25s%s%n%-25s%s%n%-25s%s%n" , "Animal Service Charges :" , animal.getServicesCharges() , "Animal's Price :" , animal.price() , "Total Amount to be Payed" , dueAmount());
    }


    // tostring method
    public String toString()
    {
        return String.format("%s%n%s%-25s%s%n%-25s%s%n","----------- Buyer  Information -----------",super.toString() ,"Amount To Be Paid :" , dueAmount(), "Date of Transaction :" , transactionDate);
    }
}




