class TaskScheduler:
    def _init_(self):
        self.tasks = {}
        self.dependencies = {}
        self.in_degree = {}
    
    def add_task(self, task_id, duration):
        self.tasks[task_id] = duration
        if task_id not in self.dependencies:
            self.dependencies[task_id] = []
        if task_id not in self.in_degree:
            self.in_degree[task_id] = 0
    
    def add_dependency(self, from_task, to_task):
        if from_task not in self.dependencies:
            self.dependencies[from_task] = []
        self.dependencies[from_task].append(to_task)
        if to_task not in self.in_degree:
            self.in_degree[to_task] = 0
        self.in_degree[to_task] += 1
    
    def compute_earliest_finish_times(self):
        queue = []
        earliest_start = {task: 0 for task in self.tasks}
        earliest_finish = {}
        
        # Initialize the queue with tasks having no incoming edges
        for task in self.tasks:
            if self.in_degree[task] == 0:
                queue.append(task)
        
        while queue:
            current_task = queue.pop(0)
            current_eft = earliest_start[current_task] + self.tasks[current_task]
            earliest_finish[current_task] = current_eft
            for dependent in self.dependencies.get(current_task, []):
                earliest_start[dependent] = max(earliest_start[dependent], current_eft)
                self.in_degree[dependent] -= 1
                if self.in_degree[dependent] == 0:
                    queue.append(dependent)
        
        return earliest_finish
    
    def compute_latest_finish_times(self, earliest_finish):
        latest_start = {task: float('inf') for task in self.tasks}
        latest_finish = {}
        queue = []
        
        # Initialize the queue with tasks having no outgoing edges
        for task in self.tasks:
            if not self.dependencies.get(task):
                latest_start[task] = earliest_finish[task]
                latest_finish[task] = earliest_finish[task]
                queue.append(task)
        
        while queue:
            current_task = queue.pop(0)
            current_lft = latest_start[current_task]
            latest_finish[current_task] = current_lft
            for task in self.tasks:
                if current_task in self.dependencies.get(task, []):
                    latest_start[task] = min(latest_start[task], current_lft - self.tasks[task])
                    self.in_degree[task] -= 1
                    if self.in_degree[task] == 0:
                        queue.append(task)
        
        return latest_finish

def main():
    scheduler = TaskScheduler()
    
    num_tasks = int(input("Enter the number of tasks: "))
    
    for _ in range(num_tasks):
        task_id = input("Enter task ID: ")
        duration = int(input(f"Enter duration for task {task_id}: "))
        scheduler.add_task(task_id, duration)
    
    num_dependencies = int(input("Enter the number of dependencies: "))
    
    for _ in range(num_dependencies):
        from_task = input("Enter task ID that has a dependency: ")
        to_task = input("Enter dependent task ID: ")
        scheduler.add_dependency(from_task, to_task)
    
    earliest_finish = scheduler.compute_earliest_finish_times()
    print("Earliest Finish Times:", earliest_finish)
    print("Earliest Time all tasks will be completed:", max(earliest_finish.values()))
    
    latest_finish = scheduler.compute_latest_finish_times(earliest_finish)
    print("Latest Finish Times:", latest_finish)
    print("Latest Time all tasks will be completed:", max(latest_finish.values()))

if __name__ == "_main_":
    main()