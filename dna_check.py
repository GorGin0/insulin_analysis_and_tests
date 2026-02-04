def filter_dna(sequences, threshold=0.1):
    clean_data = []
    for seq in sequences:
        n_count = seq.upper().count('N')
        n_ratio = n_count / len(seq)
        
        if n_ratio <= threshold:
            clean_data.append(seq)
            print(f"Годно: {seq} (ошибок: {n_ratio:.1%})")
        else:
            print(f"Брак: {seq} (слишком много N: {n_ratio:.1%})")
    return clean_data

raw_reads = [
    "ATGCGTACGTAGCT",
    "ATGANNNNGGGTAT", 
    "GCTANCGTTAGCTA",  
    "NNNNNNNNNNNNNN"  
]

print("--- Запуск фильтрации ---")
filtered = filter_dna(raw_reads)
print(f"\nИтог: Сохранено {len(filtered)} из {len(raw_reads)} последовательностей.")