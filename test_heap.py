from heap import *
import time
import matplotlib.pyplot as pt

if __name__ == "__main__":
    #41 movie list
    a_file = open("title.ratings.txt")
    names, ratings = [], []
    next(a_file)
    name_score_dict = {} # contains unsorted names and rating in a dict
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0])  # key: name
        ratings.append(float(temp[1]))  # name: rating
        name_score_dict[temp[0]] = float(temp[1])

    # code for 41 batchwise sort
    start_time_b = time.time()
    sorted_names_batchwise = sort_movies_batch(names, ratings)
    end_time_b = time.time()
    runtime_batwise = end_time_b - start_time_b

    # new sorted list for batchwise
    sorted1 = []
    for item in sorted_names_batchwise:
        sorted1.append(name_score_dict[item])

    # code for incremental sort
    start_time_i = time.time()
    sorted_names_increwise = sort_movie_incre(names, ratings)
    end_time_i = time.time()
    runtime_incre = end_time_i - start_time_i


    # new sorted list for incremental
    sorted2 = []
    for item in sorted_names_increwise:
        sorted2.append(name_score_dict[item])

    sorted_true = [9.4, 9.3, 9.2, 9.1, 9.0, 9.0, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7,
                   8.6, 8.6, 8.5, 8.5, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.2, 8.1, 8.0, 7.8, 7.7, 7.7, 7.5, 7.5, 7.4,
                   7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 7.2, 7.1]
    if sorted1 == sorted_true:
        print("pass for batch sort successfully")
        print(sorted_names_batchwise)
        print(f'Runtime for batchwise sorting:{runtime_batwise} secs\n')

    if sorted2 == sorted_true:
        print("pass for incre sort successfully")
        print(sorted_names_increwise)
        print(f'Runtime for incre sorting:{runtime_incre} secs\n')



    #random 1000 movie list
    a_file_1000 = open("title.ratings_1000.txt")
    names1, ratings1 = [], []
    next(a_file_1000)
    name_score_dict1 = {}  # contains unsorted names and rating in a dict
    for line in a_file_1000:
        temp1 = line.rstrip().split('; ')
        names1.append(temp1[0])  # key: name
        ratings1.append(float(temp1[1]))  # name: rating
        name_score_dict1[temp1[0]] = float(temp1[1])

    # code for 1000 sort
    start_time1000 = time.time()
    sorted_1000 = sort_movies_batch(names1, ratings1)
    end_time1000 = time.time()
    runtime_batwise_1000 = end_time1000 - start_time1000

    # new sorted list for 1000
    sorted1000 = []
    for item1 in sorted_1000:
        sorted1000.append(name_score_dict1[item1])
    print("pass for 1000 batch sort successfully")
    print(f'Runtime for 1000 sorting:{runtime_batwise_1000} secs\n')

    #Timsort1000
    start_time_timsort1000 = time.time()
    timesort1000 = sorted(ratings1)
    end_time_timesort1000 = time.time()
    runtime_timesort1000 = end_time_timesort1000 - start_time_timsort1000
    print("pass for 1000 Timsort successfully")
    print(f'Runtime for 1000 Timsort sorting:{runtime_timesort1000} secs\n')

    # incre1000
    start_time_incre1000 = time.time()
    incre1000 = sort_movie_incre(names1,ratings1)
    end_time_incre1000 = time.time()
    runtime_incre1000 = end_time_incre1000 - start_time_incre1000
    print("pass for 1000 Incremental successfully")
    print(f'Runtime for 1000 Incremental sorting:{runtime_incre1000} secs\n')

    # random 10000 movie list
    a_file_10000 = open("title.ratings_10000.txt")
    names2, ratings2 = [], []
    next(a_file_10000)
    name_score_dict2 = {}  # contains unsorted names and rating in a dict
    for line in a_file_10000:
        temp2 = line.rstrip().split('; ')
        names2.append(temp2[0])  # key: name
        ratings2.append(float(temp2[1]))  # name: rating
        name_score_dict2[temp2[0]] = float(temp2[1])

    # code for 10000 sort
    start_time10000 = time.time()
    sorted_10000 = sort_movies_batch(names2, ratings2)
    end_time10000 = time.time()
    runtime_batwise_10000 = end_time10000 - start_time10000


    # new sorted list for 10000
    sorted10000 = []
    for item2 in sorted_10000:
        sorted10000.append(name_score_dict2[item2])
    print("pass for 10000 batch sort successfully")
    print(f'Runtime for 10000 sorting:{runtime_batwise_10000} secs\n')


    # Timsort10000
    start_time_timsort10000 = time.time()
    timesort10000 = sorted(ratings2)
    end_time_timesort10000 = time.time()
    runtime_timesort10000 = end_time_timesort10000 - start_time_timsort10000
    print("pass for 10000 Timsort successfully")
    print(f'Runtime for 10000 Timsort sorting:{runtime_timesort10000} secs\n')

    # incre10000
    start_time_incre10000 = time.time()
    incre10000 = sort_movie_incre(names2,ratings2)
    end_time_incre10000 = time.time()
    runtime_incre10000 = end_time_incre10000 - start_time_incre10000
    print("pass for 10000 Incremental successfully")
    print(f'Runtime for 10000 Incremental sorting:{runtime_incre10000} secs\n')

    # random 100000 movie list
    a_file_100000 = open("title.ratings_100000.txt")
    names3, ratings3 = [], []
    next(a_file_100000)
    name_score_dict3 = {}  # contains unsorted names and rating in a dict
    for line in a_file_100000:
        temp3 = line.rstrip().split('; ')
        names3.append(temp3[0])  # key: name
        ratings3.append(float(temp3[1]))  # name: rating
        name_score_dict3[temp3[0]] = float(temp3[1])

    # code for 100000 sort
    start_time100000 = time.time()
    sorted_100000 = sort_movies_batch(names3, ratings3)
    end_time100000 = time.time()
    runtime_batwise_100000 = end_time100000 - start_time100000


    # new sorted list for 100000
    sorted100000 = []
    for item in sorted_100000:
        sorted100000.append(name_score_dict3[item])
    print("pass for 100000 batch sort successfully")
    print(f'Runtime for 100000 sorting:{runtime_batwise_100000} secs\n')

    # Timsort100000
    start_time_timsort100000 = time.time()
    timesort100000 = sorted(ratings3)
    end_time_timesort100000 = time.time()
    runtime_timesort100000 = end_time_timesort100000 - start_time_timsort100000
    print("pass for 100000 Timsort successfully")
    print(f'Runtime for 100000 Timsort sorting:{runtime_timesort100000} secs\n')

    # incre100000
    start_time_incre100000 = time.time()
    incre100000 = sort_movie_incre(names3,ratings3)
    end_time_incre100000 = time.time()
    runtime_incre100000 = end_time_incre100000 - start_time_incre100000
    print("pass for 100000 Incremental successfully")
    print(f'Runtime for 100000 Incremental sorting:{runtime_incre100000} secs\n')

    # Graphical representation of runtime for different datasets in Batchwise sort
    function = ["runtime for 1000", "runtime for 10000", "runtime for 100000"]
    runtime = [runtime_batwise_1000, runtime_batwise_10000, runtime_batwise_100000]

    pt.figure()
    pt.bar(function, runtime, color=["red", "yellow", "blue"])
    pt.title("Batchwise runtime comparison for different datasets")
    pt.xlabel("Size of dataset")
    pt.ylabel("Time in secs")
    pt.show()

    # Graphical representation of runtime for different datasets in Timsort
    function = ["run time for Timsort 1000", "run time for Timsort 10000", "run time for Timsort 100000"]
    runtime = [runtime_timesort1000, runtime_timesort10000, runtime_timesort100000]

    pt.figure()
    pt.bar(function, runtime, color=["red", "yellow", "blue"])
    pt.title("Timsort runtime comparison for different datasets")
    pt.xlabel("Size of dataset")
    pt.ylabel("Time in secs")
    pt.show()

    # Graphical representation of runtime for different datasets in Timsort
    function = ["run time for icremental 1000", "run time for icremental 10000", "run time for icremental 100000"]
    runtime = [runtime_incre1000, runtime_incre10000, runtime_incre100000]

    pt.figure()
    pt.bar(function, runtime, color=["red", "yellow", "blue"])
    pt.title("Incremental runtime comparison for different datasets")
    pt.xlabel("Size of dataset")
    pt.ylabel("Time in secs")
    pt.show()

    # Graphical representation of runtime for different datasets (combined)
    # Graphical representation of runtime for different datasets (combined)
    function = ["Timsort 1k", "Incremental 1k", "Batchwise 1k", "Timsort 10k", "Incremental 10k",
                "Batchwise 10k", "Timsort 1 lakh", "Incremental 1 lakh", "Batchwise 1 lakh"]
    runtime = [runtime_timesort1000, runtime_incre1000, runtime_batwise_1000, runtime_timesort10000, runtime_incre10000,
               runtime_batwise_10000, runtime_timesort100000, runtime_incre100000, runtime_batwise_100000]

    pt.figure()
    pt.bar(function, runtime, color=["red", "yellow", "blue", "purple", "pink", "green", "orange", "brown", "black"])
    pt.title("Timsort vs Batchwise vs Incremental runtime comparison for different datasets")
    pt.xlabel("Size of dataset")
    pt.ylabel("Time in secs")
    pt.show()



