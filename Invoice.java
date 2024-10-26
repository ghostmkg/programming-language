package Assignment;

public class Invoice extends MaintainFinance
{
    private Buyer buyer;
    private Dealer dealer;
    private Animal animal;
    private Seller seller;

    public Invoice(Buyer buyer , Dealer dealer , Animal animal, Seller seller)
    {
        this.buyer = buyer;
        this.dealer = dealer;
        this.animal = animal;
        this.seller = seller;
    }



    //getter and setter
    public Buyer getBuyer() 
    {
        return buyer;
    }
    public void setBuyer(Buyer buyer) 
    {
        this.buyer = buyer;
    }


    public Dealer getDealer() 
    {
        return dealer;
    }
    public void setDealer(Dealer dealer) 
    {
        this.dealer = dealer;
    }


    public Animal getAnimal() 
    {
        return animal;
    }
    public void setAnimal(Animal animal) 
    {
        this.animal = animal;
    }


    public Seller getSeller() 
    {
        return seller;
    }
    public void setSeller(Seller seller) 
    {
        this.seller = seller;
    }

    
    //method to calculate the total amount to be deposited (includes buyer + dealer + 7% tax)
    public double totalAmount()
    {
        double total = dealer.commision() + buyer.dueAmount();
        double tax = total * 0.07;
        double amountToPay = tax + total;

        //sets animal status as sold i.e sold
        animal.setAnimalStatus(true);
        return amountToPay;
    }


    // it is a commom method that keeps track of the finance of each class
    //not added in to string method can only be shown when specifically called 
    public void manageFinance()
    {
        System.out.printf("%-25s%s%n " , "Total amount to be paid : ", totalAmount());
    }


    //to string method
    public String toString()
    {
        return String.format("%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%-25s%s%n%s","=========================================="
        ,"----------------- Invoice ----------------" ,"==========================================\n"
        , animal.toString() , dealer.toString() , buyer.toString() , seller.toString(), "==========================================",
         "Net Total to be paid :", totalAmount(), "==========================================");
    }




    
}
