"""
Writer: Ranel Ben Simman Tov
"""


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_title: The title of the message.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f'User {recipient} does not exist')
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=None):
        """ Read the inbox of a user.
        :param str username: The username of the user to read the inbox of.
        :param n: The number of the first n messages to read.
        :type n: int, optional if not given, read all messages.
        :return: The messages read.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f'User {username} does not exist')
        user_box = self.boxes[username]
        messages = user_box[:n] if n else user_box
        messages = [msg for msg in messages if not msg['read']]
        for msg in messages:
            msg['read'] = True

        # return the list of messages read:
        return messages

    def search_inbox(self, username, st):
        """ Search for all messages in a user's inbox that contain the given string in their title or body.
        :param str username: The username of the user to search the inbox of.
        :param str st: The string to search for.
        :return: The list of messages that contain the given string in their title or body.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f'User {username} does not exist')
        user_box = self.boxes[username]
        return [msg for msg in user_box if st in msg['body'] or st in msg['title']]


if __name__ == "__main__":
    # test the PostOffice class
    try:
        usernames = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        po = PostOffice(usernames)
        po.send_message('Alice', 'Bob', 'this is Alice - title1!!', 'this is Alice msg1!!')
        po.send_message('Alice', 'Bob', 'this is title2!!', 'this is msg2!!', urgent=True)
        po.send_message('Alice', 'Bob', 'this is Alice - title3!!', 'this is msg3!!')
        po.send_message('Alice', 'Bob', 'this is title4!!', 'this is msg4!!')
        po.send_message('Alice', 'Bob', 'this is title5!!', 'this is Alice msg5!!')

        print("\nread the 3 first messages of Bob's inbox:")
        print(*po.read_inbox('Bob', 3), sep='\n')
        # should return only the 2 last messages because the first 3 were already read
        print("\nread all of Bob's inbox:")
        print(*po.read_inbox('Bob'), sep='\n')
        print("\nthe messages that contain 'Alice' keyword in Bob's inbox (body or title):")
        print(*po.search_inbox('Bob', 'Alice'), sep='\n')

    except KeyError as e:
        print(e)


