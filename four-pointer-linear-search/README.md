# 🔍 Four-Pointer Linear Search

A creative search algorithm that probes an unsorted array from both ends and the center simultaneously using four pointers: `i`, `j`, `mid`, and `k`.

---

## 🚀 How It Works

Instead of scanning left-to-right like classic linear search, this algorithm checks:
- `i`: from the start
- `j`: from the end
- `mid`: center of the array
- `k`: one step right of center

Each iteration moves the pointers inward until the key is found or all zones are exhausted.

---

## 📈 Time Complexity

| Algorithm               | Time Complexity | Comparisons per Iteration | Sorted Required |
|------------------------|------------------|----------------------------|------------------|
| Linear Search           | O(n)             | 1                          | ❌ No            |
| Four-Pointer Search     | O(n)             | Up to 4                    | ❌ No            |

While both are linear in worst-case time, the Four-Pointer Search can outperform classic linear search when the key is near the edges or center of the array.

---

## 📦 Usage

```bash
python four_pointer_search.py
