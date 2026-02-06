from Bio import SeqIO

# Читаем FASTA одной командой
for record in SeqIO.parse("insulin.fasta", "fasta"):
    print(f"ID: {record.id}")
    print(f"Длина: {len(record.seq)}")
    print(f"Первые 10 нуклеотидов: {record.seq[:10]}")
    # Переводим ДНК в Белок (Трансляция)
    protein = record.seq.translate()
    print(f"Белковая последовательность: {protein[:10]}...")