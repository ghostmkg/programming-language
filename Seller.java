package Assignment;

public class Seller extends Person
{
    private double profitRate;
    private double salesTaxRate;
    private Animal animal;

    //constructor
    public Seller (String name , String id , String address , String contact , double profitRate , double salesTaxRate , Animal animal)
    {
        super(name, id, address, contact);
        this.profitRate = profitRate;
        this.salesTaxRate = salesTaxRate;
        this.animal = animal; // to get access to the price method of animal
    }
        
        
    //getter and setters
     
    
    public double getProfitRate() 
    {
        return profitRate;
    }
    public void setProfitRate(double profitRate) 
    {
        this.profitRate = profitRate;
    }


    public double getSalesTaxRate() 
    {
        return salesTaxRate;
    }
    public void setSalesTaxRate(double salesTaxRate) 
    {
        this.salesTaxRate = salesTaxRate;
    }

    public Animal getAnimal() 
    { 
        return animal;
    }
    public void setAnimal(Animal animal) 
    {
        this.animal = animal;
    }
    

    //method to calculate sellers profit
    public double grossProfit() 
    {
        return animal.price()*(profitRate/100);// will return the profit based on animal price and profit percentage
    }
    
    
    // method to calculate sales TAX
    // Standard rate is 17%
    public double tax()
    {
        return grossProfit() * (salesTaxRate/100);
    }


    // method to calculate net income/profit for the seller
    public double netProfit()
    {
            return grossProfit() - tax();
    }
        
    // method to calculate net income/profit for the seller
    //not added in to string method can only be shown when specifically called 
    public void manageFinance()
    {
        System.out.printf("%-25s%s%n-25s%s%n-25s%s%n" , "Gross income :", grossProfit() ,"Tax on profit (17% is standard) :" , tax() , "Net profit for the seller :" , netProfit()  );
    }


    // ToString method
    public String toString()
    {
        return String.format("%s%n%s%-25s%s%n%-25s%s%n%-25s%s%n", "----------- Seller Information -----------" , super.toString() ,
         "Seller's Gross profit :", grossProfit(),"Tax On Profit :", tax() , "Seller's Net Profit :" , netProfit());
    }
}
