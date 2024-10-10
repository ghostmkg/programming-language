package Cube_3D;

import java.util.Scanner;

public class atm {
BankAccount account;
    Scanner sc = new Scanner(System.in);

    public atm(double startingBalance) {
        this.account = new BankAccount(startingBalance);
    }

    public void bankAccountMenu() {
        int choice;
        int amount;

        do {
            displayMenu();
            System.out.println("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Enter amount to withdraw: ");
                    amount = sc.nextInt();
                    account.withdraw(amount);
                    break;

                case 2:
                    System.out.println("Enter amount to deposit: ");
                    amount = sc.nextInt();
                    account.deposit(amount);
                    break;

                case 3:
                    System.out.println("Current balance: " + account.checkBalance());
                    break;

                case 4:
                    System.out.println("Thank you for using the ATM.");
                    break;

                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);
    }

    public void displayMenu() {
        System.out.println("\nATM Menu:");
        System.out.println("Click 1. for  Withdrawal Money ");
        System.out.println("Click 2. for  Deposit Money ");
        System.out.println("Click 3. for  Checking Current Balance  ");
        System.out.println("Click 4. for  Exit ");
    }
}
class BankAccount {
    double balance;

    public BankAccount(double startingBalance) {
        this.balance = startingBalance;
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Your Amount is  Withdrawal is successfully.");
            System.out.println("Your Remaining balance is: " + balance);
        } else {
            System.out.println("Sorry Withdrawal is not possible insufficient balance in your account.");
        }
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Your amount "+amount+ " is Deposited successfully.");
            System.out.println("Your Current balance is: " + balance);
        } else {
            System.out.println(" Invalid amount entered.");
        }
    }

    public double checkBalance() {
        return balance;
    }


    public static void main(String[] args) {
        System.out.println(" Welcome to The ATM .\n Hoping your transaction will be Right");
        atm a = new atm(100000);
        a.bankAccountMenu();
    
    }
}

