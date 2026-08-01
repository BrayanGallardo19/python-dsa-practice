def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    if square_target == 0 or square_target == 1:
        print(f'The square root of {square_target} is {square_target}')
        return square_target
    
    low = 0
    high = max(1, square_target)
    
    for i in range(max_iterations):
        root = (low + high) / 2
        
        if high - low <= tolerance:
            print(f'The square root of {square_target} is approximately {root}')
            return root
        
        if root ** 2 < square_target:
            low = root
        else:
            high = root
    
    print(f'Failed to converge within {max_iterations} iterations')
    return None