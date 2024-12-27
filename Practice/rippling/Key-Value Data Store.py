"""
### Problem Statement: Key-Value Data Store with Transactions

Implement a key-value data store with support for the following operations:

1. `set(key, value)`: 
   - Set the value of a key in the data store.
   - If a transaction is active, the change should be part of the current transaction.

2. get(key): 
   - Retrieve the value of the given key.
   - If the key does not exist, return None.

3. delete(key): 
   - Remove the key from the data store.
   - If a transaction is active, mark the key for deletion in the current transaction.

4. begin(): 
   - Start a new transaction.
   - Any changes made after this call should be part of the current transaction.

5. rollback(): 
   - Revert all changes made in the most recent transaction.
   - If no transaction is active, this operation should return an error or a message indicating failure.

6. commit(): 
   - Apply all changes in the active transactions to the permanent data store.
   - If no transaction is active, this operation should return an error or a message indicating failure.

### Additional Requirements:
- Support nested transactions, where multiple begin calls can create nested transaction scopes.
- Ensure space efficiency by maintaining only the necessary changes in active transactions.
- Use a stack or similar data structure to handle the rollback and commit logic for nested transactions.


### Constraints:
- The solution must run efficiently and handle operations in O(1) or O(n) where applicable.
- Implement error handling for invalid operations (e.g., calling `rollback` or `commit` without an active transaction).

### Key Design Points:
1. Use a permanent dictionary to store committed values.
2. Use a stack of dictionaries to maintain temporary changes during transactions.
3. Handle deletions explicitly by marking keys for deletion in the temporary data store.
4. Carefully merge temporary changes into the permanent store during commits.


"""
class KeyValueStore:
    def __init__(self):
        self.permanent_store = {}  # Permanent key-value store
        self.transaction_stack = []  # Stack to store nested transaction states

    def set(self, key, value):
        if self.transaction_stack:
            self.transaction_stack[-1][key] = value
        else:
            self.permanent_store[key] = value

    def get(self, key):
        # Check the latest transaction first, then permanent store
        for transaction in reversed(self.transaction_stack):
            if key in transaction:
                return transaction[key] if transaction[key] != "__DELETE__" else None
        return self.permanent_store.get(key, None)

    def delete(self, key):
        if self.transaction_stack:
            self.transaction_stack[-1][key] = "__DELETE__"  # Mark for deletion
        elif key in self.permanent_store:
            del self.permanent_store[key]

    def begin(self):
        self.transaction_stack.append({})

    def rollback(self):
        if not self.transaction_stack:
            print("NO TRANSACTION")
        else:
            self.transaction_stack.pop()

    def commit(self):
        if not self.transaction_stack:
            print("NO TRANSACTION")
        else:
            # Merge all transactions into the permanent store
            while self.transaction_stack:
                transaction = self.transaction_stack.pop(0)
                for key, value in transaction.items():
                    if value == "__DELETE__":
                        self.permanent_store.pop(key, None)
                    else:
                        self.permanent_store[key] = value

# Test cases
def test_key_value_store():
    store = KeyValueStore()

    # Basic set and get
    store.set("a", 10)
    assert store.get("a") == 10
    store.set("b", 20)
    assert store.get("b") == 20

    # Delete operation
    store.delete("a")
    assert store.get("a") is None

    # Transaction begin, set, and rollback
    store.begin()
    store.set("c", 30)
    assert store.get("c") == 30
    store.rollback()
    assert store.get("c") is None

    # Transaction begin, set, and commit
    store.begin()
    store.set("d", 40)
    assert store.get("d") == 40
    store.commit()
    assert store.get("d") == 40

    # Nested transactions
    store.begin()
    store.set("e", 50)
    store.begin()
    store.set("f", 60)
    assert store.get("f") == 60
    store.rollback()
    assert store.get("f") is None
    assert store.get("e") == 50
    store.commit()
    assert store.get("e") == 50

    print("All test cases passed!")

test_key_value_store()
