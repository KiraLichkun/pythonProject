import csv

with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=','))  # Создаём объект для чтения файла
    sum_score = {}
    count_scores = {}
    for row in reader:  # Считываем данные из файла
        if 'Хадаров Владимир' in row['Name']:
            print(f'Ты получил: {row["score"]}, за проект - {row["titleProject_id"]}')

        sum_score[row['class']] = sum_score.get(row['class'], 0) + (int(row['score']) if row['score'] != 'None' else 0)
        # Ищем сумму оценок
        count_scores[row['class']] = count_scores.get(row['class'], 0) + 1  # Ищем количество оценок

    for row in reader:
        if row['score'] == 'None':
            row['score'] = round(sum_score[row['class']] / count_scores[row['class']], 3)
            # Находим среднее арифметическое значение

with open('students_new.csv', 'w') as file:  # Сохраняем данные в новый файл
    writer = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writeheader()
    writer.writerows(reader)
