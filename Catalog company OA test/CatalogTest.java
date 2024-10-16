public class CatalogTest {
    public static void main(String[] args) {
        // Create a catalog
        Catalog catalog = new Catalog();

        // Create products
        Product product1 = new Product("Laptop", 999.99, "High-performance laptop");
        Product product2 = new Product("Smartphone", 499.99, "Latest model smartphone");

        // Add products to the catalog
        catalog.addProduct(product1);
        catalog.addProduct(product2);

        // Display all products
        System.out.println("Catalog Products:");
        for (Product product : catalog.getProducts()) {
            System.out.println(product);
        }

        // Find a product by name
        String searchName = "Laptop";
        Product foundProduct = catalog.findProductByName(searchName);
        if (foundProduct != null) {
            System.out.println("Found product: " + foundProduct);
        } else {
            System.out.println("Product not found: " + searchName);
        }

        // Remove a product
        catalog.removeProduct(product1);
        System.out.println("Catalog after removing Laptop:");
        for (Product product : catalog.getProducts()) {
            System.out.println(product);
        }
    }
}
