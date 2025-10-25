#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>     
#include <time.h>

#define N_PHIL 5            
#define MEALS_PER_PHIL 3   

pthread_mutex_t forks[N_PHIL];
sem_t waiter;              
int meals_done[N_PHIL];

void rand_sleep_ms(int min_ms, int max_ms) {
    int ms = min_ms + rand() % (max_ms - min_ms + 1);
    usleep(ms * 1000);
}

void *philosopher(void *arg) {
    int id = *(int *)arg;
    int left = id;                       
    int right = (id + 1) % N_PHIL;     

    for (int meal = 1; meal <= MEALS_PER_PHIL; ++meal) {
       
        printf("Philosopher %d is THINKING (meal %d/%d).\n", id, meal, MEALS_PER_PHIL);
        fflush(stdout);
        rand_sleep_ms(100, 600);

        
        printf("Philosopher %d is HUNGRY and tries to get permission from waiter.\n", id);
        fflush(stdout);
        sem_wait(&waiter); // wait until it's safe to try picking forks

        
        printf("Philosopher %d is trying to pick LEFT fork %d.\n", id, left);
        fflush(stdout);
        pthread_mutex_lock(&forks[left]);
        printf("Philosopher %d picked LEFT fork %d.\n", id, left);
        fflush(stdout);

        printf("Philosopher %d is trying to pick RIGHT fork %d.\n", id, right);
        fflush(stdout);
        pthread_mutex_lock(&forks[right]);
        printf("Philosopher %d picked RIGHT fork %d.\n", id, right);
        fflush(stdout);

       
        printf("Philosopher %d is EATING (meal %d/%d).\n", id, meal, MEALS_PER_PHIL);
        fflush(stdout);
        rand_sleep_ms(150, 500);
        meals_done[id]++;

        
        pthread_mutex_unlock(&forks[right]);
        printf("Philosopher %d put DOWN RIGHT fork %d.\n", id, right);
        fflush(stdout);

        pthread_mutex_unlock(&forks[left]);
        printf("Philosopher %d put DOWN LEFT fork %d.\n", id, left);
        fflush(stdout);

      
        sem_post(&waiter);
        printf("Philosopher %d informed waiter (finished meal %d).\n", id, meal);
        fflush(stdout);

        
        rand_sleep_ms(50, 200);
    }

    printf("Philosopher %d is DONE (ate %d meals).\n", id, MEALS_PER_PHIL);
    fflush(stdout);
    return NULL;
}

int main(int argc, char *argv[]) {
    srand((unsigned int)time(NULL));

   
    pthread_t threads[N_PHIL];
    int ids[N_PHIL];

   
    for (int i = 0; i < N_PHIL; ++i) {
        if (pthread_mutex_init(&forks[i], NULL) != 0) {
            perror("pthread_mutex_init");
            exit(EXIT_FAILURE);
        }
        meals_done[i] = 0;
    }

 
    if (sem_init(&waiter, 0, N_PHIL - 1) != 0) {
        perror("sem_init");
        exit(EXIT_FAILURE);
    }

 
    for (int i = 0; i < N_PHIL; ++i) {
        ids[i] = i;
        if (pthread_create(&threads[i], NULL, philosopher, &ids[i]) != 0) {
            perror("pthread_create");
            exit(EXIT_FAILURE);
        }
    }


    for (int i = 0; i < N_PHIL; ++i) {
        pthread_join(threads[i], NULL);
    }

  
    for (int i = 0; i < N_PHIL; ++i) {
        pthread_mutex_destroy(&forks[i]);
    }
    sem_destroy(&waiter);

    printf("\nAll philosophers finished. Meals eaten by each:\n");
    for (int i = 0; i < N_PHIL; ++i) {
        printf("Philosopher %d: %d meals\n", i, meals_done[i]);
    }

    return 0;
}
