package CMS;

public class Date {
    private int day ;
    private int month ;
    private int year ;

    private static final int[] daysPerMonth = { 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    public Date(int day, int month, int year) 
    {

        if (day <= 0 || (day > daysPerMonth[month] && !(month == 2 && day == 29)))
            throw new IllegalArgumentException("day (" + day + ") out-of-range for the specified month and year");

        if (month <= 0 && month >= 12)
            throw new IllegalArgumentException("month (" + month + ") must be 1-12");

        if (month == 2 && day == 29 && !(year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)))
        throw new IllegalArgumentException("day (" + day + ") out-of range for the specified month and year");

        this.day = day;
        this.month = month;
        this.year = year;
    }

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    // public void Display_date()
    // {
    // System.out.println(day + " / " + month + " / " + year );
    // }
    public String toString() 
    {
        return day + " / " + month + " / " + year;
    }

}