

class Session():

    def __enter__(self):
        print("entered")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        print(exc_type, exc_val, exc_tb)
    


def get_a_number():

    with Session() as session:
        for i in range(100):
            yield i

def main():

    gen = get_a_number()
    print(next(gen))

if __name__ == "__main__":
    main()
