#Alfred Gachanja
#19-07-2023.
#In this program I am practing what I learned about passing arguments.

def make_tshirts(size='large', message='matthew 5:48'):
    """Displays the information about the t-shit made."""
    print("\nThis is a {} size t-shirt." .format(size))
    print("Read the verse {} printed in my {} size t-shirt." .format(message.title(), size))

make_tshirts('large', 'john 15:13')
make_tshirts(size='medium', message='matthew 6:33')
make_tshirts()