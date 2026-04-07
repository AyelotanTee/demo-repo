import numpy as np

class score():
    def print_score(func):
        def wrapper(*args, **kwargs):
            print("="*20)
            print(f"Your score: {func(*args, **kwargs)}")
            print("="*20)
        return wrapper
    
    @print_score
    def ip__mersenne_numbers(mersennes):
        result = np.array([7, 31, 127, 2047, 8191, 131071, 524287, 8388607, 536870911, 2147483647, 137438953471, 2199023255551,
                           8796093022207, 140737488355327, 9007199254740991, 576460752303423487, 2305843009213693951
                 ])
        mersennes = np.array(mersennes)
        
        return (mersennes == result).sum() / result.size
    
    @print_score
    def ip__lucas_lehmer(ll_result):
        result = np.array([4, 14, 194, 37634, 95799, 119121, 66179, 53645, 122218, 126220, 70490, 69559, 99585, 78221, 130559, 0])
        ll_result = np.array(ll_result)
        
        return (ll_result == result).sum() / result.size
    
    @print_score
    def ip__mersenne_primes(mersenne_primes):
        result = np.array([(3, 1), (5, 1), (7, 1), (11, 0), (13, 1), (17, 1), (19, 1), (23, 0), (29, 0), (31, 1), (37, 0), (41, 0), (43, 0),
                           (47, 0), (53, 0), (59, 0), (61, 1)
                          ]).flatten()
        mersenne_primes = np.array(mersenne_primes).flatten()
        
        return (mersenne_primes == result).sum() / result.size

        
    @print_score
    def ip__is_prime_fast(get_primes_fast):
        result = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        
        return (np.array(get_primes_fast(100)) == result).sum() / result.size
    
    
    @print_score
    def ip__eratosthenes(sieve):
        result = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        
        return (np.array(sieve(100)) == result).sum() / result.size

    @staticmethod
    def get_points():
        x = np.round(np.linspace(-10, 10, 50))
        f = lambda x: np.sin(x) + np.cos(x) if x < 0 else np.sqrt(25 - (x-5)**2)
        y = np.array(np.round([f(i) for i in x]))
        points = list(zip(x, y))
                      
        return points
    
    @print_score
    def vc__point_repr(func):
        points = score.get_points()[:10]
        result =             [
            'Point(-10.0, -0.0)',
            'Point(-10.0, -0.0)',
            'Point(-9.0, -1.0)',
            'Point(-9.0, -1.0)',
            'Point(-8.0, -1.0)',
            'Point(-8.0, -1.0)',
            'Point(-8.0, -1.0)',
            'Point(-7.0, 0.0)',
            'Point(-7.0, 0.0)',
            'Point(-6.0, 1.0)'
            ]
        return (np.array(func(points)) == np.array(result)).sum() / len(result)
    
    @print_score
    def vc__add_subtract(func):
        points = score.get_points()[:10]
        result = [
            'Point(-82.0, -4.0)', 'Point(62.0, 4.0)'
            ]
        return (np.array(func(points)) == np.array(result)).sum() / len(result)
    
    @print_score
    def vc__multiplication(func):
        points = score.get_points()[:10]
        result = [200.0, 200.0, 164.0, 164.0, 130.0, 130.0, 130.0, 98.0, 98.0, 74.0]
        return (np.array(func(points)) == np.array(result)).sum() / len(result)
    
    @print_score
    def vc__distance(func):
        points = score.get_points()[:10]
        result = [0.0,
                0.0,
                1.4142135623730951,
                1.4142135623730951,
                2.23606797749979,
                2.23606797749979,
                2.23606797749979,
                3.0,
                3.0,
                4.123105625617661]
        lst = func(points)
        return (np.round(np.array(lst), 2) == np.round(np.array(result), 2)).sum() / len(result)
    
    @print_score
    def vc__k_means(func):
        points = score.get_points()
        result = [
            (5.333333333333333, 3.958333333333333),
            (-4.923076923076923, -0.19230769230769232)
        ]
        lst = func(points)
        return (np.round(np.array(lst), 2) == np.round(np.array(result), 2)).sum() / np.array(result).size
    
    
if __name__ == "__main__":
    pass