public class BankingSystem {
    static class BankAccount {
        private double balance;
        
        public BankAccount(double initialBalance) {
            this.balance = initialBalance;
        }

        public synchronized void deposit(double amount) throws IllegalArgumentException {
            if (amount <= 0) throw new IllegalArgumentException("Deposit amount must be positive");
            balance += amount;
            System.out.println("Deposited: " + amount + ", New Balance: " + balance);
        }

        public synchronized void withdraw(double amount) throws IllegalArgumentException, IllegalStateException {
            if (amount <= 0) throw new IllegalArgumentException("Withdrawal amount must be positive");
            if (amount > balance) throw new IllegalStateException("Insufficient balance");
            balance -= amount;
            System.out.println("Withdrew: " + amount + ", New Balance: " + balance);
        }

        public synchronized double getBalance() {
            return balance;
        }
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);

        Thread user1 = new Thread(() -> {
            try {
                account.deposit(200);
                account.withdraw(150);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        });

        Thread user2 = new Thread(() -> {
            try {
                account.deposit(100);
                account.withdraw(200);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        });

        user1.start();
        user2.start();
    }
}
