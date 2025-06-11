### ✅ 1-Task: `Book` klassi

**Vazifa:** `Book` nomli class yarating. Unda quyidagi methodlar bo‘lsin:

* `__init__(self, title, author)` – kitob nomi va muallifini saqlaydi.
* `get_info(self)` – `"Kitob: <title>, Muallif: <author>"` ko‘rinishida ma’lumot qaytarsin.

**Misol:**

```python
book1 = Book("1984", "George Orwell")
print(book1.get_info())  
# Natija: Kitob: 1984, Muallif: George Orwell
```

---

### ✅ 2-Task: `Calculator` klassi

**Vazifa:** `Calculator` nomli class yarating. Quyidagi methodlarni qo‘shing:

* `add(self, a, b)` – ikki sonni qo‘shib natijasini qaytaradi.
* `subtract(self, a, b)` – ayirma
* `multiply(self, a, b)` – ko‘paytma
* `divide(self, a, b)` – bo‘linma (agar `b == 0` bo‘lsa `"0 ga bo‘lish mumkin emas"` deb qaytarsin)

**Misol:**

```python
calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.divide(10, 0))    # 0 ga bo‘lish mumkin emas
```

---

### ✅ 3-Task: `Student` klassi

**Vazifa:** `Student` nomli class yarating. Unda:

* `__init__(self, name)` – ism saqlaydi
* `add_grade(self, grade)` – baho qo‘shadi (baho integer bo‘lishi kerak)
* `get_average(self)` – barcha baholarning o‘rtacha qiymatini hisoblab qaytaradi

**Misol:**

```python
student1 = Student("Ali")
student1.add_grade(5)
student1.add_grade(4)
print(student1.get_average())  # 4.5
```

