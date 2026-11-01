import pandas

dictionary = {'A': 1, 'D': 2, 'C': 3}

data_frame = pandas.DataFrame(list(dictionary.items()), columns=["key", "value"])   #Frame erzeugen aus Dict

data_frame_sorted = data_frame.sort_values(by="key", ascending=True)    #Frame sortieren nach key (A, D, C)

data_frame_sorted.to_csv("Einfuehrung_Vorlesung1/Aufgabe3_data/output.csv", index=False)   #Frame als csv speichern

data_frame_loaded = pandas.read_csv("Einfuehrung_Vorlesung1/Aufgabe3_data/output.csv")     #Frame mit csv laden

print(data_frame)
print(data_frame_sorted)
print(data_frame_loaded)