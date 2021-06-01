# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


even_integers_generator_object = even_integers_generator()

[x for x in even_integers_generator_object]
