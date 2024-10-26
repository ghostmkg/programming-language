package Assignment;

public class Date 
{
    private int day = 8;
    private int month = 5;
    private int year = 2024 ;

    public Date(int day, int month , int year)
    {
        if (day > 0 && day <= 30  )
        this.day = day ;
        if (month > 0 && month <= 12  )
        this.month = month ;
        if (year > 0   )
        this.year = year ;
    }

    public int getDay() 
    {
        return day;
    }

    public void setDay(int day) 
    {
        this.day = day;
    }

    public int getMonth() 
    {
        return month;
    }

    public void setMonth(int month) 
    {
        this.month = month;
    }

    public int getYear() 
    {
        return year;
    }

    public void setYear(int year) 
    {
        this.year = year;
    }

    // public void Display_date()
    // {
    //     System.out.println(day + " / " + month + " / "  + year );
    // }
    public String toString()
    {
        return day + " / " + month + " / "  + year ;
    }

    
}
