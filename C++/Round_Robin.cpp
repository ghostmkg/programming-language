#include <iostream>
#include <queue>
#include <vector>

struct Process {
    int id;
    int burstTime;
    int remainingTime;
    int waitingTime;
    int turnaroundTime;
};

void roundRobin(std::vector<Process>& processes, int quantum) {
    std::queue<Process*> readyQueue;
    int currentTime = 0;
    
    for (auto& process : processes) {
        process.remainingTime = process.burstTime;
        readyQueue.push(&process);
    }

    while (!readyQueue.empty()) {
        Process* currentProcess = readyQueue.front();
        readyQueue.pop();

        if (currentProcess->remainingTime > quantum) {
            currentTime += quantum;
            currentProcess->remainingTime -= quantum;
            readyQueue.push(currentProcess);
        } else {
            currentTime += currentProcess->remainingTime;
            currentProcess->waitingTime = currentTime - currentProcess->burstTime;
            currentProcess->turnaroundTime = currentTime;
            currentProcess->remainingTime = 0;
        }
    }
}

void printResults(const std::vector<Process>& processes) {
    std::cout << "Process\tBurst Time\tWaiting Time\tTurnaround Time\n";
    for (const auto& process : processes) {
        std::cout << "P" << process.id << "\t\t" << process.burstTime << "\t\t" 
                  << process.waitingTime << "\t\t" << process.turnaroundTime << "\n";
    }
}

int main() {
    int n, quantum;
    
    std::cout << "Enter the number of processes: ";
    std::cin >> n;
    
    std::vector<Process> processes(n);
    
    for (int i = 0; i < n; i++) {
        processes[i].id = i + 1;
        std::cout << "Enter burst time for process " << i + 1 << ": ";
        std::cin >> processes[i].burstTime;
    }
    
    std::cout << "Enter the time quantum: ";
    std::cin >> quantum;

    roundRobin(processes, quantum);
    printResults(processes);
    
    return 0;
}
