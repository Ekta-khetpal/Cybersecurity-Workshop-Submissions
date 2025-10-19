comments = []  # list to store comments

print("=== Welcome to the Comment Box ===")
print("Type your comments below.")
print("Type 'exit' when you are done.\n")

while True:
    comment = input("Enter your comment: ")
    if comment.lower() == "exit":
        break
    if comment.strip() == "":
        print("Empty comment not allowed. Try again.")
        continue
    comments.append(comment)
    print("Comment added successfully!\n")

print("\n=== All Submitted Comments ===")
if comments:
    for i, c in enumerate(comments, start=1):
        print(f"{i}. {c}")
else:
    print("No comments submitted.")