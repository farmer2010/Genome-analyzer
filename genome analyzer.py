import pyperclip

genome_length = 64

file = open("D:\projects\Cyber Biology 2\Cyber Biology 2 Pro\saved objects\colony2.dat")
text = file.readline().split(" ")
file.close()

genome = []
for i in range(genome_length):
    genome.append(int(text[i]))

all_commands = [23, 24, 25, 26, 27, 28, 29, 30, 31, 34, 50, 35, 52, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
count_params = {
    23 : 1,
    24 : 1,
    26 : 1,
    28 : 1,
    30 : 1,
    34 : 1,
    50 : 1,
    36 : 1,
    37 : 1,
    41 : 1,
    43 : 1,
    44 : 1,
    45 : 1,
    46 : 1
}
count_transitions = {
    30 : 5,
    31 : 5,
    36 : 2,
    37 : 2,
    39 : 2,
    40 : 2,
    43 : 2,
    44 : 2,
    45 : 2,
    48 : 1
}

commands_names = {
    23 : "Повернуться на ",
    24 : "Повернуть ",
    25 : "Фотосинтез",
    26 : "Походить ",
    27 : "Походить вперед",
    28 : "Атаковаь ",
    29 : "Атаковать вперед",
    30 : "Посмотреть ",
    31 : "Посмотреть вперед",
    34 : "Отдать часть ресурсов ",
    50 : "Отдать часть ресурсов ",
    35 : "Отдать часть ресурсов вперед",
    52 : "Отдать часть ресурсов вперед",
    36 : "Энергии >= ",
    37 : "Минералов >= ",
    38 : "Преобразовать минералы в энергию",
    39 : "Возможен ли фотосинтез?",
    40 : "Есть ли приход минералов?",
    41 : "Поделиться ",
    42 : "Поделиться вперед",
    43 : "Позиция X >= ",
    44 : "Позиция Y >= ",
    45 : "Возраст >= ",
    46 : "Равномерное распределение ресурсов ",
    47 : "Равномерное распределение ресурсов вперед"
}
commands_shapes = {
    23 : "box",
    24 : "box",
    25 : "box",
    26 : "box",
    27 : "box",
    28 : "box",
    29 : "box",
    30 : "diamond",
    31 : "diamond",
    34 : "box",
    50 : "box",
    35 : "box",
    52 : "box",
    36 : "diamond",
    37 : "diamond",
    38 : "box",
    39 : "diamond",
    40 : "diamond",
    41 : "box",
    42 : "box",
    43 : "diamond",
    44 : "diamond",
    45 : "diamond",
    46 : "box",
    47 : "box"
}
commands_colors = {
    23 : "#eec803",
    24 : "#eec803",
    25 : "#008100",
    26 : "#00ffff",
    27 : "#00ffff",
    28 : "#FF0000",
    29 : "#FF0000",
    30 : "#fd81ef",
    31 : "#fd81ef",
    34 : "#ff4400",
    50 : "#ff4400",
    35 : "#ff4400",
    52 : "#ff4400",
    36 : "#ee9a04",
    37 : "#4267eb",
    38 : "#1e91fb",
    39 : "#32cd33",
    40 : "#78398a",
    41 : "#ceb28b",
    42 : "#ceb28b",
    43 : "#7df716",
    44 : "#7df716",
    45 : "#42b071",
    46 : "#ff4400",
    47 : "#ff4400"
}
commands_transitions_names = {
    30 : ["Если ", "граница", "ничего", "враг", "родственик", "органика"],
    31 : ["Если ", "граница", "ничего", "враг", "родственик", "органика"],
    36 : ["", "Да", "Нет"],
    37 : ["", "Да", "Нет"],
    39 : ["", "Да", "Нет"],
    40 : ["", "Да", "Нет"],
    43 : ["", "Да", "Нет"],
    44 : ["", "Да", "Нет"],
    45 : ["", "Да", "Нет"]
}
commands_params_notation = {
    23 : ["% 8 n "],
    24 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"],
    26 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"],
    28 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"],
    30 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"],
    34 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"],
    50 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"],
    36 : ["* 15 n ?"],
    37 : ["* 15 n ?"],
    41 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"],
    43 : ["@ 162 n ?"],
    44 : ["@ 108 n ?"],
    45 : ["* 15 n ?"],
    46 : ["% 8 r ", "вверх", "вправо-вверх", "вправо", "вправо-вниз", "вниз", "влево-вниз", "влево", "влево-вверх"]
}

def command(commands, index, indexes):
    if not (index in indexes):
        indexes.append(index)
        if commands[index] in all_commands:
            p = 0 if not (commands[index] in count_params) else count_params[commands[index]]
            t = 0 if not (commands[index] in count_transitions) else count_transitions[commands[index]]
            if t == 0:
                command(commands, (index + 1 + p) % genome_length, indexes)
            else:
                for i in range(t):
                    command(commands, commands[(index + 1 + p + i) % genome_length], indexes)
        else:
            if commands[index] in count_transitions:
                command(commands, commands[(index + 1) % genome_length], indexes)
            else:
                command(commands, (index + commands[index]) % genome_length, indexes)

def parse(commands):
    indexes = []
    command(genome, 0, indexes)
    #
    commands_data = []
    for index in indexes:
        if commands[index] in all_commands:
            data = [commands[index], index]
            param = []
            p = 0 if not (commands[index] in count_params) else count_params[commands[index]]
            t = 0 if not (commands[index] in count_transitions) else count_transitions[commands[index]]
            for i in range(p):
                param.append(commands[(index + 1 + i) % genome_length])
            data.append(param)
            trans = []
            if t == 0:
                trans.append((index + 1 + p) % genome_length)
            else:
                for i in range(t):
                    trans.append(commands[(index + 1 + p + i) % genome_length])
            data.append(trans)
            commands_data.append(data)
    #
    for c in commands_data:
        for t in range(len(c[3])):
            index = c[3][t]
            y = 0
            inf_flag = 0
            while 1:
                y += 1
                if not (commands[index] in all_commands):
                    if commands[index] in count_transitions:
                        index = commands[(index + 1) % genome_length]
                    else:
                        index = (index + commands[index]) % genome_length
                else:
                    break
                if y >= genome_length:
                    inf_flag = 1
                    break
            if not inf_flag:
                for i in range(len(commands_data)):
                    if commands_data[i][1] == index:
                        c[3][t] = i
                        break
            else:
                c[3][t] = -1
    return(commands_data)

def translate(commands_data):
    text = "digraph G{\n\tСтарт;\n"
    #
    commands_obj_names = []
    for i in range(len(commands_data)):
        text += "\t"
        text += str(i) + "[style=filled"
        text += ", shape=" + commands_shapes[commands_data[i][0]]
        text += ", color=" + '"' + commands_colors[commands_data[i][0]] + '"'
        t = commands_names[commands_data[i][0]]
        if commands_data[i][0] in commands_params_notation:
            l = commands_params_notation[commands_data[i][0]]
            notation = l[0].split(" ")
            x = 0
            if notation[0] == "%":
                x = commands_data[i][2][0] % int(notation[1])
            elif notation[0] == "*":
                x = commands_data[i][2][0] * int(notation[1])
            elif notation[0] == "@":
                x = int(commands_data[i][2][0] / genome_length * int(notation[1]))
            if notation[2] == "n":
                t += str(x)
            elif notation[2] == "r":
                t += l[x + 1]
            t += notation[3]
        text +=  ", label=" + '"' + t + '"' + "];\n"
    #
    i = 0
    for c in commands_data:
        for t in c[3]:
            if t == -1:
                i += 1
                text += "\tinf" + str(i) + '[label="Бесконечный\n цикл"];\n'
    #
    inf_counter = 0
    text += "\t//\n\t//\n\t//\n"
    text += "\tСтарт -> 0;\n"
    text += "\t//\n"
    for i in range(len(commands_data)):
        t_l = []
        for j in range(len(commands_data[i][3])):
            if commands_data[i][3][j] != -1:
                if not (j in t_l):
                    k_l = []
                    for k in range(j, len(commands_data[i][3])):
                        if commands_data[i][3][k] == commands_data[i][3][j]:
                            t_l.append(k)
                            k_l.append(k)
                    if len(k_l) == 1:
                        t = commands_data[i][3][j]
                        text += "\t" + str(i) + " -> " + str(t)
                        if commands_data[i][0] in commands_transitions_names:
                            text += '[label="' + commands_transitions_names[commands_data[i][0]][0]
                            text += commands_transitions_names[commands_data[i][0]][j + 1]
                            text += '"];\n'
                    else:
                        t_count = 1 if not (commands_data[i][0] in count_transitions) else count_transitions[commands_data[i][0]]
                        if len(k_l) == t_count:
                            t = commands_data[i][3][j]
                            text += "\t" + str(i) + " -> " + str(t) + '[label="Всегда"];\n'
                        else:
                            t = commands_data[i][3][j]
                            text += "\t" + str(i) + " -> " + str(t) + '[label="'
                            text += commands_transitions_names[commands_data[i][0]][0]#"если"
                            for h in range(len(k_l)):
                                text += commands_transitions_names[commands_data[i][0]][k_l[h] + 1]
                                if h < len(k_l) - 2:
                                    text += ", "
                                elif h < len(k_l) - 1:
                                    text += " или "
                            text += '"];\n'
            else:
                inf_counter += 1
                text += "\t" + str(i) + " -> inf" + str(inf_counter)
        if text[-1] != "\n":
            text += "\n\t//\n"
        else:
            text += "\t//\n"
    #
    text += "}\n"
    return(text)

commands_data = parse(genome)
for i in range(len(commands_data)):
    c = commands_data[i]
    print(f"{i}: {c[0]}, index={c[1]}, params={c[2]}, transitions={c[3]}")
print(f"{len(commands_data)} commands total")

code = translate(commands_data)
pyperclip.copy(code)

