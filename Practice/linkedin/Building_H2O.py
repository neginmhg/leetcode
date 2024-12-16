"""
There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.
We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up with. The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

 

Example 1:

Input: water = "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2:

Input: water = "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
 

Constraints:

3 * n == water.length
1 <= n <= 20
water[i] is either 'H' or 'O'.
There will be exactly 2 * n 'H' in water.
There will be exactly n 'O' in water.
"""
from threading import Semaphore
from threading import Barrier
import threading
class H2O:
    def __init__(self):
        # Semaphore for hydrogen: allows 2 hydrogen threads at a time
        self.sem_h = Semaphore(2)
        
        # Semaphore for oxygen: allows 1 oxygen thread at a time
        self.sem_o = Semaphore(1)
        
        # Barrier that waits for 3 threads: 2 hydrogen + 1 oxygen
        self.barrier = Barrier(3)
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            self.barrier.wait()
            releaseHydrogen()  # releaseHydrogen() outputs "H". Do not change or remove this line.

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.barrier.wait()
            releaseOxygen()     # releaseOxygen() outputs "O". Do not change or remove this line.

# Methods to simulate hydrogen and oxygen release
def releaseHydrogen():
    print("H", end="")

def releaseOxygen():
    print("O", end="")

# Function to create hydrogen threads
def hydrogen_thread(h2o):
    h2o.hydrogen(releaseHydrogen)

# Function to create oxygen threads
def oxygen_thread(h2o):
    h2o.oxygen(releaseOxygen)

# Instantiate the H2O class
h2o = H2O()

# Create a list to hold the threads
threads = []

# Example input: 6 hydrogen atoms and 3 oxygen atoms to form 3 water molecules (H2O)
input_sequence = ['H', 'H', 'O', 'H', 'H', 'O', 'H', 'H', 'O']

# Create and start threads based on input sequence
for atom in input_sequence:
    if atom == 'H':
        t = threading.Thread(target=hydrogen_thread, args=(h2o,))
        threads.append(t)
    else:
        t = threading.Thread(target=oxygen_thread, args=(h2o,))
        threads.append(t)

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("\nWater molecules formed!")
""""
This means:
- 2 hydrogen atoms (H) and 1 oxygen atom (O) should always group together before they can "release" and form water.
- We need to make sure the right number of hydrogen and oxygen atoms are released at the same time to form the molecule.

 Tools We Use

- Semaphore: This is like a "ticket counter" that controls how many threads (hydrogen or oxygen) can pass through. For example, if you have a ticket counter with 2 tickets, only 2 threads can pass through at a time. If more threads come, they wait until someone finishes and a ticket becomes available.
- Barrier: This acts like a "gate." It waits until a specific number of threads arrive at the gate, then it lets them all pass together. In our case, we set the barrier to wait for 3 threads (2 hydrogen + 1 oxygen).

 Code Explanation

 1. Semaphores: Controlling the Number of Threads

```python
self.sem_h = Semaphore(2)
self.sem_o = Semaphore(1)
```

- `self.sem_h = Semaphore(2)`: This semaphore allows only 2 hydrogen threads to enter. If more hydrogen threads come, they have to wait for their turn.
- `self.sem_o = Semaphore(1)`: This semaphore allows only 1 oxygen thread to enter at a time.

This ensures that exactly 2 hydrogen atoms and 1 oxygen atom are ready to form a molecule.

 2. Barrier: Waiting for 3 Threads to Group Together

```python
self.barrier = Barrier(3)
```

- `self.barrier = Barrier(3)`: This barrier waits for 3 threads (2 hydrogen + 1 oxygen) to arrive before letting them continue. Once the 3 threads arrive, they can all move forward at the same time.

 3. Hydrogen Function (Releasing hydrogen)

```python
def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
    with self.sem_h:
        self.barrier.wait()
        releaseHydrogen()
```

- `with self.sem_h:`: This ensures that only 2 hydrogen threads can enter this section at a time. If more than 2 hydrogen threads try to enter, they will wait until one of them leaves.
- `self.barrier.wait()`: The hydrogen thread waits at the barrier until 3 threads (2 hydrogen + 1 oxygen) are ready.
- `releaseHydrogen()`: This function simulates the "release" of a hydrogen atom, meaning it's ready to form a water molecule.

 4. Oxygen Function (Releasing oxygen)

```python
def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
    with self.sem_o:
        self.barrier.wait()
        releaseOxygen()
```

- `with self.sem_o:`: This ensures that only 1 oxygen thread can enter this section at a time. If another oxygen thread tries to enter while one is already there, it will wait.
- `self.barrier.wait()`: The oxygen thread also waits at the barrier until 3 threads (2 hydrogen + 1 oxygen) are ready.
- `releaseOxygen()`: This function simulates the "release" of an oxygen atom, meaning it's ready to form a water molecule.

 How It All Works Together

1. Hydrogen and oxygen threads are created and run.
2. Hydrogen threads use `sem_h`, which only allows 2 of them to move forward at a time.
3. Oxygen threads use `sem_o`, which only allows 1 of them to move forward.
4. Both hydrogen and oxygen threads wait at the barrier until there are exactly 3 threads (2 H + 1 O) ready.
5. Once the barrier gets all 3 threads, it lets them all move forward together, and the molecule of water is formed (2 H + 1 O).

 Why This Works

- The semaphore ensures that only the correct number of hydrogen and oxygen atoms are released at the same time.
- The barrier ensures that all three atoms (2 hydrogen + 1 oxygen) wait for each other before forming a water molecule.

This solution makes sure that threads are synchronized correctly to form water molecules without mixing up atoms or letting one molecule get formed before the other threads are ready.
"""