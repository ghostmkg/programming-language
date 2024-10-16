#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>  // For sleep()

#define MAX 5
#define TOTAL_OPERATIONS 10  // Number of items to produce and consume

int buffer[MAX];
int count = 0; // Items in buffer
int produced = 0, consumed = 0;  // Counters to track total produced and consumed items

sem_t empty;  // Semaphore for empty slots
sem_t full;   // Semaphore for full slots
pthread_mutex_t mutex; // Mutex for critical section

void *producer(void *arg) {
    while (produced < TOTAL_OPERATIONS) {
        sem_wait(&empty);  // Wait for an empty slot
        pthread_mutex_lock(&mutex); // Lock before modifying buffer

        if (produced < TOTAL_OPERATIONS) {  // Check if we should continue
            buffer[count++] = 1;  // Produce item
            produced++;
            printf("Produced, Items in buffer: %d\n", count);
        }

        pthread_mutex_unlock(&mutex); // Unlock after modifying buffer
        sem_post(&full);  // Signal that a full slot is available
        sleep(1);  // Simulate time taken to produce
    }
    pthread_exit(0);
}

void *consumer(void *arg) {
    while (consumed < TOTAL_OPERATIONS) {
        sem_wait(&full);  // Wait for a full slot
        pthread_mutex_lock(&mutex); // Lock before modifying buffer

        if (consumed < TOTAL_OPERATIONS) {  // Check if we should continue
            buffer[--count] = 0;  // Consume item
            consumed++;
            printf("Consumed, Items in buffer: %d\n", count);
        }

        pthread_mutex_unlock(&mutex); // Unlock after modifying buffer
        sem_post(&empty);  // Signal that an empty slot is available
        sleep(1);  // Simulate time taken to consume
    }
    pthread_exit(0);
}

int main() {
    pthread_t prodThread, consThread;

    // Initialize semaphores and mutex
    sem_init(&empty, 0, MAX); // Initially, all slots are empty
    sem_init(&full, 0, 0);    // Initially, no slots are full
    pthread_mutex_init(&mutex, NULL);

    // Create producer and consumer threads
    pthread_create(&prodThread, NULL, producer, NULL);
    pthread_create(&consThread, NULL, consumer, NULL);

    // Wait for both threads to finish
    pthread_join(prodThread, NULL);
    pthread_join(consThread, NULL);

    // Clean up resources
    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    printf("Production and consumption completed.\n");
    return 0;
}
