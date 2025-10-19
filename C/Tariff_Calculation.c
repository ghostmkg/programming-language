#include <stdio.h>
#include <stdlib.h>

struct Consumer {
    char name[50];
    char type;      
    int time;       
    double energy;  
    double tariff;  
};

void calculateTariff(struct Consumer *consumer) {
    consumer->tariff = 0.0;

    if (consumer->type == 'D') {
        consumer->tariff = 0.1 * consumer->energy;
    } else if (consumer->type == 'I') {
        consumer->tariff = 0.15 * consumer->energy;
    } else {
        printf("Invalid consumer type for %s.\n", consumer->name);
    }

    if (consumer->time >= 9 && consumer->time <= 17) {
        consumer->tariff += 0.05 * consumer->energy;
    } else {
        consumer->tariff += 0.03 * consumer->energy;
    }
}

int main() {
    int numConsumers;
    printf("Enter the number of consumers: ");
    scanf("%d", &numConsumers);

    struct Consumer *consumers = (struct Consumer *)malloc(numConsumers * sizeof(struct Consumer));
    if (consumers == NULL) {
        printf("Memory allocation failed. Exiting...\n");
        return 1;
    }

    for (int i = 0; i < numConsumers; i++) {
        printf("Enter consumer %d information:\n", i + 1);
        printf("Name: ");
        scanf("%s", consumers[i].name);
        printf("Type (D for domestic, I for industrial): ");
        scanf(" %c", &consumers[i].type); 
        printf("Time (in hours): ");
        scanf("%d", &consumers[i].time);
        printf("Energy consumed (in kWh): ");
        scanf("%lf", &consumers[i].energy);

        calculateTariff(&consumers[i]);
    }

    int choice;
    while (1) {
        printf("\nMenu:\n");
        printf("1. View Consumer Information\n");
        printf("2. Update Consumer Information\n");
        printf("3. Delete Consumer Information\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: // View Consumer Information
                printf("Enter the consumer number to view (1 to %d): ", numConsumers);
                int viewIndex;
                scanf("%d", &viewIndex);
                if (viewIndex >= 1 && viewIndex <= numConsumers) {
                    struct Consumer consumer = consumers[viewIndex - 1];
                    printf("Consumer Information:\n");
                    printf("Name: %s, Type: %c, Tariff: $%.2lf\n", consumer.name, consumer.type, consumer.tariff);
                } else {
                    printf("Invalid input. Please enter a valid consumer number.\n");
                }
                break;

            case 2: // Update Consumer Information
                printf("Enter the consumer number to update (1 to %d): ", numConsumers);
                int updateIndex;
                scanf("%d", &updateIndex);
                if (updateIndex >= 1 && updateIndex <= numConsumers) {
                    struct Consumer *consumer = &consumers[updateIndex - 1];
                    printf("Update Consumer Information for %s:\n", consumer->name);
                    // Prompt user to update fields like type, time, energy, etc.
                    // Then recalculate tariff using calculateTariff function.
                } else {
                    printf("Invalid input. Please enter a valid consumer number.\n");
                }
                break;

            case 3: // Delete Consumer Information
                printf("Enter the consumer number to delete (1 to %d): ", numConsumers);
                int deleteIndex;
                scanf("%d", &deleteIndex);
                if (deleteIndex >= 1 && deleteIndex <= numConsumers) {
                    // Implement code to delete the selected consumer, which may require shifting elements in the array.
                    // Be sure to free any memory if needed.
                } else {
                    printf("Invalid input. Please enter a valid consumer number.\n");
                }
                break;

            case 4: // Exit
                free(consumers); // Free dynamically allocated memory
                return 0;

            default:
                printf("Invalid choice. Please select a valid option.\n");
        }
    }

    return 0;
}
