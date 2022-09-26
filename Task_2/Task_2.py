# Напишите программу для. проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for a in range(2):
        for b in range(2):
            for c in range(2):
                print(not (a or b or c) == (not a and not b and not c))
                print(a, b, c)