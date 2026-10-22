def generate_numbers():
    for i in range(10):
        print(i)
        yield i
        i += 1

def process_numbers():
    for number in generate_numbers():
        print("Received:", number)
        yield number
       
for number in process_numbers():
    print("Processed:", number)