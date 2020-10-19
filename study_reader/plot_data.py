from file_function import read_file_data, show_plot


# 打开文件，对文件中需要的信息进行读取
file_name_sitka = 'data/sitka_weather_2018_simple.csv'
file_name_death = 'data/death_valley_2018_simple.csv'

data_sitka = read_file_data(file_name_sitka)
data_death = read_file_data(file_name_death)
show_plot(data_sitka)
show_plot(data_death)

