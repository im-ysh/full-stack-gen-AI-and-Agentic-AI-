class chai:
    temperature = "hot"
    strength = "strong"

cutting = chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup  = "small"
print("after changing : " , cutting.temperature)
print("cup size : " , cutting.cup)
print("class temperature : " , chai.temperature)


del cutting.temperature
del cutting.cup

print("after deleting cutting temp: " , cutting.temperature)
print("after deleting cutting cup: " , cutting.cup)



"""
YES 👍 — a **diagram** is exactly what you need.  
Forget everything else. Just look at this slowly.

***

## Your code (reference)

```python
class chai:
    temperature = "hot"
    strength = "strong"

cutting = chai()
```

***

## STEP 1: After the class is created

    ┌───────────────┐
    │  class chai   │
    ├───────────────┤
    │ temperature → "hot"
    │ strength    → "strong"
    └───────────────┘

Only **ONE thing exists** so far: the **class**.

***

## STEP 2: After `cutting = chai()`

    ┌───────────────┐        ┌────────────────┐
    │  class chai   │        │ object cutting │
    ├───────────────┤        ├────────────────┤
    │ temperature → "hot"    │ (nothing yet)  │
    │ strength    → "strong" │                │
    └───────────────┘        └────────────────┘

Important:

*   `cutting` has **NO temperature**
*   It **borrows** from the class

So:

```python
print(cutting.temperature)   # hot
```

✅ Python looks:

1.  In object ❌
2.  In class ✅ → `"hot"`

***

## STEP 3: After `cutting.temperature = "mild"`

    ┌───────────────┐        ┌────────────────┐
    │  class chai   │        │ object cutting │
    ├───────────────┤        ├────────────────┤
    │ temperature → "hot"    │ temperature → "mild"
    │ strength    → "strong" │                │
    └───────────────┘        └────────────────┘

🚨 CRITICAL POINT

*   You did **NOT** change the class
*   You created a **NEW attribute ONLY inside the object**

So now:

```python
print(cutting.temperature)   # mild
print(chai.temperature)      # hot
```

Object value **hides** (shadows) class value.

***

## STEP 4: After `del cutting.temperature`

    ┌───────────────┐        ┌────────────────┐
    │  class chai   │        │ object cutting │
    ├───────────────┤        ├────────────────┤
    │ temperature → "hot"    │ (nothing)      │
    │ strength    → "strong" │                │
    └───────────────┘        └────────────────┘

✅ `del` removes **ONLY the object’s copy**

The class is untouched.

***

## STEP 5: Access again

```python
print(cutting.temperature)
```

Python searches again:

1.  Object? ❌ (deleted)
2.  Class? ✅ `"hot"`

So result is:

    hot

***

## ONE LINE TO REMEMBER (PLEASE MEMORIZE THIS)

> **Object → first priority**  
> **Class → fallback**

***

## REAL-LIFE ANALOGY 🏠

    Class  → apartment building rules (default)
    Object → your own flat changes

*   If you repaint your flat → you see YOUR color
*   If you remove your paint → building color shows again

***

## WHY `del` FEELS LIKE MAGIC

Because `del cutting.temperature` means:

❌ “Do NOT store temperature in object anymore”

So Python says:

> “Okay, I’ll use the class one again.”

***

## ✅ Final simple summary

    cutting.temperature = "mild"  → creates object attribute
    del cutting.temperature       → removes object attribute
    cutting.temperature           → falls back to class attribute

***

If you want, next I can:

*   draw this with **multiple objects**
*   show `cutting.__dict__` to prove it
*   explain when changing `chai.temperature` affects all objects

Just tell me 👍

""" 

cutting = chai()


