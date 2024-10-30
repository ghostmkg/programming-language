#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_USERS 5
#define RECORD_SIZE 7

typedef struct {
    int id;
    int attendance[RECORD_SIZE]; // Stores attendance records (hour, minute, second, day, month, year)
} User;

User users[MAX_USERS];
int userCount = 0;

void enrollUser(int id);
void displayUsers();
void resetSystem();
void recordAttendance(int id);
void downloadData();
void deleteUser(int id);
void showTime();

int main() {
    char command[50];
    int id;

    while (1) {
        printf("Commands: enroll <id>, display, reset, record <id>, download, delete <id>, exit\n");
        printf("Enter command: ");
        fgets(command, sizeof(command), stdin);
        command[strcspn(command, "\n")] = 0; // Remove newline character

        if (strncmp(command, "enroll", 6) == 0) {
            sscanf(command + 7, "%d", &id);
            enrollUser(id);
        } else if (strcmp(command, "display") == 0) {
            displayUsers();
        } else if (strcmp(command, "reset") == 0) {
            resetSystem();
        } else if (strncmp(command, "record", 6) == 0) {
            sscanf(command + 7, "%d", &id);
            recordAttendance(id);
        } else if (strcmp(command, "download") == 0) {
            downloadData();
        } else if (strncmp(command, "delete", 6) == 0) {
            sscanf(command + 7, "%d", &id);
            deleteUser(id);
        } else if (strcmp(command, "exit") == 0) {
            break;
        } else {
            printf("Unknown command. Please try again.\n");
        }
    }

    return 0;
}

void enrollUser(int id) {
    if (userCount < MAX_USERS) {
        users[userCount].id = id;
        memset(users[userCount].attendance, 0xff, sizeof(users[userCount].attendance)); // Initialize attendance data
        userCount++;
        printf("User enrolled with ID: %d\n", id);
    } else {
        printf("Maximum user limit reached!\n");
    }
}

void displayUsers() {
    if (userCount == 0) {
        printf("No users enrolled.\n");
        return;
    }

    printf("Enrolled Users:\n");
    for (int i = 0; i < userCount; i++) {
        printf("ID: %d\n", users[i].id);
    }
}

void resetSystem() {
    memset(users, 0, sizeof(users));
    userCount = 0;
    printf("System reset successfully.\n");
}

void recordAttendance(int id) {
    for (int i = 0; i < userCount; i++) {
        if (users[i].id == id) {
            time_t t = time(NULL);
            struct tm *tm_info = localtime(&t);

            users[i].attendance[0] = tm_info->tm_hour;
            users[i].attendance[1] = tm_info->tm_min;
            users[i].attendance[2] = tm_info->tm_sec;
            users[i].attendance[3] = tm_info->tm_mday;
            users[i].attendance[4] = tm_info->tm_mon + 1; // Months are 0-based
            users[i].attendance[5] = tm_info->tm_year + 1900; // tm_year is years since 1900

            printf("Attendance recorded for User ID: %d\n", id);
            return;
        }
    }
    printf("User ID %d not found.\n", id);
}

void downloadData() {
    printf("Attendance Data:\n");
    for (int i = 0; i < userCount; i++) {
        printf("User ID: %d, Attendance: ", users[i].id);
        for (int j = 0; j < RECORD_SIZE; j++) {
            if (users[i].attendance[j] != 0xff) {
                printf("%d ", users[i].attendance[j]);
            } else {
                printf("N/A ");
            }
        }
        printf("\n");
    }
}

void deleteUser(int id) {
    for (int i = 0; i < userCount; i++) {
        if (users[i].id == id) {
            for (int j = i; j < userCount - 1; j++) {
                users[j] = users[j + 1]; // Shift users down
            }
            userCount--;
            printf("User ID %d deleted successfully.\n", id);
            return;
        }
    }
    printf("User ID %d not found.\n", id);
}
