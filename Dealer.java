package Assignment;
import java.util.ArrayList;

public class Dealer extends Person 
{
    // instance variables
    private double commisionRate;
    private Animal animal; 
    private ArrayList<Animal> animals = new ArrayList<>(); 
    
    public Dealer(String name , String id , String address , String contact , double commisionRate , Animal animal , ArrayList<Animal> animals)
    {
        super(name, id, address, contact);
        this.commisionRate = commisionRate;
        this.animal = animal;
        this.animals = animals;
    }

    // Getters and Setters
    public double getCommisionRate() 
    {
        return commisionRate;
    }

    public void setCommisionRate(double commisionRate) 
    {
        this.commisionRate = commisionRate;
    }


    public Animal getAnimal() 
    {
        return animal;
    }
    public void setAnimal(Animal animal) 
    {
        this.animal = animal;
    }
    
    
    public ArrayList<Animal> getAnimals() 
    {
        return animals;
    }
    public void setAnimals(ArrayList<Animal> animals) 
    {
        this.animals = animals;
    }


    //method to add animals into dealers class
    public void addAnimal(Animal a)
    {
        if (!animals.contains(a))
        {
            animals.add(a);
            System.out.println("Animal added...! ");
        }
        else
            System.out.println("Animal is Already avalible!");
    }


    //method to remove animal , after confirming its avalibility
    public String removeAnimal(String idTag)
    {
        for(Animal animal : animals)
        {
            if(animal.getIdTag().equals(idTag))
            {
                animals.remove(animal);
                animal.setAnimalStatus(true);
                return "Animal removed";
            }
        }
        return "animal with ID TAg :" + idTag + " not found";
    }


    //method to check animals avalibility
    //using for each loop
    public String contains(String idTag)
    {
        for(Animal animal : animals)
        {
            if(animal.getIdTag().equals(idTag))
            {
                return "Animal avalible";
            }
        }  
        return "Animal not avalible";
        
    }

    //method to display all animal objects
    //variable i help us keeep track of the number of animals
    public void displayObjects()
    {
        int i = 1;
        for (Animal animal : animals)
        {
            System.out.println("Animal " + i + " : \n" + animal );
            i++;
        }
    }

    // Method to calculate the commision earned by dealer  
    public double commision()
    {
        return animal.price()*(commisionRate/100) ;
    }



    //method for discount on commision in realtime, here we are keeping it 2%
    public double realtimeDiscount()
    {
        double discount = commision() * 0.02;
        double calculation = commision() - discount;
        return calculation;
    }


    // it is a commom method that keeps track of the finance of each class
    //not added in to string method can only be shown when specifically called 
    public void manageFinance()
    {
        System.out.printf("%-25s%s%s%n%-25s%s%n%-25s%s%n%-25s%s%n" ,
         "Commision Rate :" , commisionRate ,"%",
          "Animal's Price :" , animal.price() , "Dealer's Commision :" ,
           commision() , "Post Discount commision :"  , realtimeDiscount());
    }


    //ToString method 

    public String toString()
    {
        return String.format("%s%n%s%-25s%s%n","----------- Dealer Information -----------",   super.toString() , "Dealer's Commision :", commision() );
    }


}

