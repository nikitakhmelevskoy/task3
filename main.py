def merge_segments(segments):
    sorted_segments = sorted(segments, key=lambda x: x[0])

    # инициализируем
    merged_segments = []

    # обработка каждого отрезка
    for seg in sorted_segments:
        if not merged_segments:
            merged_segments.append(seg)
        else:
            # проверяем не пересекается ли текущий отрезок с верхним в стеке
            top_seg = merged_segments[-1]
            if seg[0] <= top_seg[1]:
                # объеденяем два отрезка
                merged_segments[-1] = (top_seg[0], max(top_seg[1], seg[1]))
            else:
                #Текущий отрезок не пересекается с верхним, помещаем в стек
                merged_segments.append(seg)

    return merged_segments


segments = []
with open('input.txt', 'r') as f:
    for line in f:
        start, end = map(int, line.strip().split())
        segments.append((start, end))

merged_segments = merge_segments(segments)
with open('output.txt', 'w') as f:
    for seg in merged_segments:
        f.write(f"{seg[0]} {seg[1]}\n")