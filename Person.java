package CMS;
public abstract class Person 
{
    private String name;    
    private String cnic;    
    private String contact;    
    private String address;

    public Person(String name, String cnic, String contact, String address) {
        this.name = name;
        this.cnic = cnic;
        this.contact = contact;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCnic() {
        return cnic;
    }

    public void setCnic(String cnic) {
        this.cnic = cnic;
    }

    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

     public abstract String account();

    public String toString()
    {
        return String.format("-------Personal Details-------%n%-20s%s%n%-20s%s%n%-20s%s%n%-20s%s%n","Name : ",name,"Contact : "
        ,contact, "Address : ",address ,"Cnic No. : ",cnic);
    }
    
    
}
