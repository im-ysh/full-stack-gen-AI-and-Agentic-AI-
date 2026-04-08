class chai:
    pass

print(type(chai))

ginger_tea = chai()
print(type(ginger_tea))
print(type(ginger_tea) is chai)
print(type(ginger_tea) is chai())




# ```python
# class chai:
#     pass

# ginger_tea = chai()
# ```

# ### After this, there are **THREE things** in memory:

# ### ✅ 1. `chai`

# *   This is a **class**
# *   Think: **recipe**

# ### ✅ 2. `ginger_tea`

# *   This is an **object**
# *   Think: **tea made from the recipe**

# ### ✅ 3. `chai()`

# *   This makes a **NEW object every time**
# *   Think: **another cup of tea**

# ***

# ## Now let’s check them ONE BY ONE

# ### What is `ginger_tea`?

# ```python
# ginger_tea
# ```

# ➡️ an **object (cup of tea)**

# ***

# ### What is `chai()`?

# ```python
# chai()
# ```

# ➡️ ALSO an **object (another cup of tea)**  
# ⚠️ **Not the same cup as `ginger_tea`**

# Even this is important:

# ```python
# chai() is chai()   # False
# ```

# Two cups ≠ one cup

# ***

# ### What is `type(ginger_tea)`?

# ```python
# type(ginger_tea)
# ```

# Python answers:

# > “Which recipe made this tea?”

# Answer:

# ```python
# chai
# ```

# ✅ **NOT** `chai()`
# ✅ The **recipe itself**

# ***

# ## NOW the problem line 👇

# ```python
# type(ginger_tea) is chai()
# ```

# Replace words with meanings:

# ```text
# recipe  IS  cup of tea ?
# ```

# ❌ NO  
# A recipe is NOT a cup of tea

# So Python prints:

# ```python
# False
# ```

# ***

# ## Why this line is TRUE ✅

# ```python
# type(ginger_tea) is chai
# ```

# Replace meanings:

# ```text
# recipe  IS  recipe ?
# ```

# ✅ YES → `True`

# ***

# ## VERY short table (read slowly)

# | Code               | What it really is |
# | ------------------ | ----------------- |
# | `chai`             | recipe            |
# | `chai()`           | cup of tea        |
# | `ginger_tea`       | cup of tea        |
# | `type(ginger_tea)` | recipe            |

# ***

# ## ✅ THE RIGHT QUESTION YOU WANT TO ASK

# You were really asking:

# > “Was ginger\_tea made from chai?”

# ✅ Correct Python way:

# ```python
# isinstance(ginger_tea, chai)
# ```

# Output:

# ```python
# True
# ```

# ***

# ## FINAL ONE‑LINE RULE (memorize this)

# 👉 **Never compare a class to `class()`**  
# 👉 Use **`isinstance(object, class)`**

# ***

# If you want, next I can explain this using **memory numbers (`id`)** or a **literal drawing**.  
# Just say which one 👍
