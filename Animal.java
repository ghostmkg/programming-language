package Assignment;

public class Animal extends MaintainFinance
{
    private String type;
    private String idTag;
    private String color;
    private double weight;
    private double pricePerKg;
    private Date arrivalDate;
    private long servicesCharges;
    private boolean animalStatus;


    // Constructor
    public Animal(String type, String idTag, String color, double weight, double pricePerKg, Date arrivalDate,long servicesCharges, boolean animalStatus) 
    {
        this.type = type;
        this.idTag = idTag;
        this.color = color;
        this.weight = weight;
        this.pricePerKg = pricePerKg;
        this.arrivalDate = arrivalDate;
        this.servicesCharges = servicesCharges;
        this.animalStatus = animalStatus;
    }


    // Getter and setters
    public String getType() 
    {
        return type;
    }
    public void setType(String type) 
    {
        this.type = type;
    }


    public String getIdTag() 
    {
        return idTag;
    }
    public void setIdTag(String idTag) 
    {
        this.idTag = idTag;
    }


    public String getColor() 
    {
        return color;
    }
    public void setColor(String color) 
    {
        this.color = color;
    }


    public double getWeight() 
    {
        return weight;
    }
    public void setWeight(double weight) 
    {
        this.weight = weight;
    }


    public double getPricePerKg() 
    {
        return pricePerKg;
    }
    public void setPricePerKg(double pricePerKg) 
    {
        this.pricePerKg = pricePerKg;
    }
    

    public Date getArrivalDate() 
    {
        return arrivalDate;
    }
    public void setArrivalDate(Date arrivalDate) 
    {
        this.arrivalDate = arrivalDate;
    }


    public long getServicesCharges() 
    {
        return servicesCharges;
    }
    public void setServicesCharges(long servicesCharges) 
    {
        this.servicesCharges = servicesCharges;
    }


    public boolean getAnimalStatus() 
    {
        return animalStatus;
    }
    public void setAnimalStatus(boolean animalStatus) 
    {
        this.animalStatus = animalStatus;
    }


    //method to calculate the price of animal based on its weight and price per KG
    public double price()
    {
        return weight*pricePerKg;
    }
    

    //common method for all the classes
    //here it calculates the price of animal based on its weight and price per KG
    @Override
    public void manageFinance()
    {
        System.out.println("Price of the animal is :" + price());
    }
    


    public String toString()
    {
        return String.format(
        "%s%n%-25s%s%n%-25s%s%n%-25s%s%n%-25s%s%n%-25s%s%n%-25s%s%n%-25s%s%n%-25s%s%n%-25s%s%n" ,"----------- Animal Information -----------",
         "Type :", type , "Identification Tag :" , idTag , "Color :" , color , "Weight :" , weight ,
         "Price Per KG :" , pricePerKg , "Arrival Date :" , arrivalDate , "Service Charges :" ,servicesCharges ,
         "Animal's Price :" , price() ,"Animal Status :", animalStatus );
    }

    
}
