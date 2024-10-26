package Assignment;

public abstract class Person extends MaintainFinance
{
    // Instance variables
    private String name;
    private String id;
    private String address;
    private String contact;

    // Constructor
    public Person (String name , String id , String address , String contact)
    {
        this.name = name;
        this.id = id;
        this.address = address;
        this.contact = contact;
    }

    // Getter and setters for each instance variable

    public void setname(String name)
    {
        this.name = name;
    }
    public String getname()
    {
        return name;
    }


    public void setid(String id)
    {
        this.id = id;
    }
    public String getid()
    {
        return id;
    }


    public void setaddress(String address)
    {
        this.address = address;
    }
    public String getaddress()
    {
        return address;
    }

    
    public void setcontact(String contact)
    {
        this.contact = contact;
    }
    public String getcontact()
    {
        return contact;
    }


    // ToString method to return values 

    public String toString()
    {
        return String.format("%-25s%s%n%-25s%s%n%-25s%s%n%-25s%s%n",
            "Name :", name ,
            "ID :", id ,
            "Address :", address ,
            "Contatc :" , contact );
    }
}
