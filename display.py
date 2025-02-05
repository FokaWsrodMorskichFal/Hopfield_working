import matplotlib.pyplot as plt

def display(x, dims):
    plt.imshow(x.reshape(dims[1], dims[0]), cmap='gray', norm='linear')
    plt.show()

def save_img(x, dims, save_as):
    plt.imshow(x.reshape(dims[1], dims[0]), cmap='gray', norm='linear')
    plt.savefig(save_as)

def user_choose_display(num_of_patterns):
    question = 'Which training pattern would you like to see? Choose [1-' + str(num_of_patterns) + '] : '
    bool = True
    
    while bool:
        try:
            tmp = int(input(question))
            if (tmp < 1 or tmp>num_of_patterns):
                print("Invalid integer range.")
            else:
                bool = False
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return tmp-1