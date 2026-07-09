#Challenge 1: The Duplicate Cleaner (Data Preprocessing Foundation)

data = [10, 20, 10, 30, 40, 20, 50, 40]
data1=set(data)
print(sorted(list(data1)))

# Challenge 2: The Recommendation Engine (Venn Diagram Logic)

a_fav_movie={"Inception", "Interstellar", "The Dark Knight", "Avatar"}
b_fav_movie={"Interstellar", "Prestige", "Avatar", "Memento"}\

print(a_fav_movie.intersection(b_fav_movie))
print(a_fav_movie.difference(b_fav_movie))