class Comment:
    DELETED_MESSAGE = "This comment has been deleted."
    
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply_comment):
        self.replies.append(reply_comment)

    def remove_reply(self):
        self.text = self.DELETED_MESSAGE
        self.author = ""
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level
        
        if self.is_deleted:
            # Display only the deleted message and continue recursion for children
            print(f"{indent}{self.text}")
        else:
            # Display author and text
            print(f"{indent}{self.author}: {self.text}")

        # Recursively display all replies
        for reply in self.replies:
            reply.display(level + 1)

if __name__ == '__main__':
    # Creating the initial hierarchy
    root_comment = Comment("What a wonderful book!", "Mike")
    reply1 = Comment("The book is a complete disappointment :(", "John")
    reply2 = Comment("What's so wonderful about it?", "Mary")

    # Building the first level
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    # Creating a reply to the first reply
    reply1_1 = Comment("Not a book, but a waste of paper for nothing...", "Chris")
    reply1.add_reply(reply1_1)

    # Removing the first reply
    reply1.remove_reply()
    
    # Displaying the final result
    print("--- Comment System Output ---")
    root_comment.display()