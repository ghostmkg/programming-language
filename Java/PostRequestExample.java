import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class PostRequestExample {
    public static void main(String[] args) {
        try {
            // Endpoint to post data to
            String url = "http://www.example.com/api/project";

            // Data to send in POST body (example JSON)
            String jsonData = "{\"projectName\":\"MyProject\",\"description\":\"A test project\"}";

            // Create HttpClient
            HttpClient client = HttpClient.newHttpClient();

            // Build POST request
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonData))
                    .build();

            // Send request and get response
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            // Print response status and body
            System.out.println("Response code: " + response.statusCode());
            System.out.println("Response body: " + response.body());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
