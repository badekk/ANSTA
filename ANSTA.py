#Zadanie numero uno
def post_code_gen(start_gen : str, end_gen : str):

    start_gen = start_gen.split("-")
    start_gen = "".join(start_gen)
    start_gen = int(start_gen)

    end_gen = int(''.join(end_gen.split("-")))

    generated_post_codes = []

    for post_code in range (start_gen, end_gen + 1):
        generated_post_codes.append(post_code)
        print('%02d-%03d' % (post_code/1000, post_code%1000))


#Zadanie numero dos
def find_missing_elem(elem: list, n):
    check_against = range(1, n+1)
    print(list(set(check_against) - set(elem)))


#Zadanie numero dres
def range_float(start, end, by):
    list = [start]
    while start < end:
        start += by
        list.append(start)
    print(list)


post_code_gen("79-900", "80-155")
find_missing_elem([2,3,7,4,9], 10)
range_float(2, 5.5, 0.5)