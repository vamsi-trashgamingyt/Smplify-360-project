class FriendNetwork:
    def _init_(self):
        self.network = {}

    def add_friend(self, person, friend):
        if person not in self.network:
            self.network[person] = []
        if friend not in self.network:
            self.network[friend] = []
        self.network[person].append(friend)
        self.network[friend].append(person)

    def get_friends(self, person):
        return self.network.get(person, [])
#
    def common_friends(self, person1, person2):
        friends1 = set(self.get_friends(person1))
        friends2 = set(self.get_friends(person2))
        return list(friends1 & friends2)

    def nth_connection(self, start, end):
        if start == end:
            return 0
        visited = set()
        queue = [(start, 0)]
        while queue:
            current, depth = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            for friend in self.get_friends(current):
                if friend == end:
                    return depth + 1
                if friend not in visited:
                    queue.append((friend, depth + 1))
        return -1

    def print_network(self):
        for person in self.network:
            print(f'{person}: {self.network[person]}')

def main():
    fn = FriendNetwork()
    
    # Adding default friends Alice and Bob
    fn.add_friend('Alice', 'Bob')
    
    # Take custom input
    while True:
        choice = input("\nChoose an option:\n1. Add friend\n2. Get friends\n3. Find common friends\n4. Find nth connection\n5. Print network\n6. Exit\n")
        
        if choice == '1':
            person = input("Enter the name of the first person: ")
            friend = input("Enter the name of the friend: ")
            fn.add_friend(person, friend)
            print(f"Added friendship between {person} and {friend}.")
        
        elif choice == '2':
            person = input("Enter the name of the person: ")
            friends = fn.get_friends(person)
            print(f"Friends of {person}: {friends}")
        
        elif choice == '3':
            person1 = input("Enter the name of the first person: ")
            person2 = input("Enter the name of the second person: ")
            common = fn.common_friends(person1, person2)
            print(f"Common friends of {person1} and {person2}: {common}")
        
        elif choice == '4':
            start = input("Enter the starting person's name: ")
            end = input("Enter the ending person's name: ")
            connection = fn.nth_connection(start, end)
            print(f"Connection between {start} and {end}: {connection}")
        
        elif choice == '5':
            fn.print_network()
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()