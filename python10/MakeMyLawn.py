def lawn_and_fence(lawn_height, fence_height):

    print('**' + ' ' * (lawn_height - fence_height))

    for i in range(lawn_height - fence_height):
        if i == lawn_height - i :
            print('**' + ' ' * (lawn_height - fence_height))
        else:
            print('**' + 'x' * (lawn_height - fence_height))




lawn_height = int(input("Enter the height of the lawn: "))
fence_height = int(input("Enter the height of the fence: "))
lawn_and_fence(lawn_height, fence_height)
