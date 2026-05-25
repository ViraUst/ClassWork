# Question 16(a)
# Name and School: Vira Ustymenko
# Date: 8th May 2026

books = []
num = int(input("How many books have you read? "))

for i in range(num):
    book = input("Enter the title of the book you've read: ")
    books.append(book)
if num>=3:
    print("Fantastic! You've read",num,"books - keep reading!")
print("Book(s) read:")
for t in range(num):
    print(books[t])