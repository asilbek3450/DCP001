import heapq
from collections import defaultdict

# 1️⃣ Harflarning chastotasi asosida tree tuzish
def build_huffman_tree(text):
    frequency = defaultdict(int)  # Chastota hisoblagich
    for char in text:
        frequency[char] += 1  # Har bir belgi uchun chastotani oshirish
    
    # Priority queue (heap) yaratish, bu tree qurish uchun kerak
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)  # Heapsort yordamida yig'ish

    while len(heap) > 1:
        low = heapq.heappop(heap)  # Eng kichik ikkita elementni olib tashlash
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]  # Kichik elementga '0' qo'shish
        for pair in high[1:]:
            pair[1] = '1' + pair[1]  # Katta elementga '1' qo'shish
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])  # Yangi tugun yaratish

    return heap[0][1:]  # Kodlash jadvali

# 2️⃣ Huffman kodini yaratish
def huffman_encoding(text):
    huff_tree = build_huffman_tree(text)
    huff_dict = {char: code for char, code in huff_tree}
    encoded_text = ''.join(huff_dict[char] for char in text)
    return encoded_text, huff_dict  # Kodlangan matn va jadvalni qaytarish

# 3️⃣ Huffman kodini dekodlash
def huffman_decoding(encoded_text, huff_dict):
    reverse_dict = {code: char for char, code in huff_dict.items()}
    current_code = ''
    decoded_text = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_dict:
            decoded_text += reverse_dict[current_code]
            current_code = ''
    return decoded_text

# 4️⃣ Test qilish
text = input("Huffman kodlash uchun matn kiriting: ")  # Foydalanuvchidan matn olish
if not text:
    text = "Hello, Huffman encoding!"  # Agar matn kiritilmasa, default matn
encoded_text, huff_dict = huffman_encoding(text)  # Matnni kodlash
decoded_text = huffman_decoding(encoded_text, huff_dict)  # Matnni dekodlash

# Natijalar
print(f"✅ Original Matn: {text}")
print(f"🔍 Harflarning chastotasi: {dict(huff_dict)}")
print(f"🔒 Kodlangan Matn: {encoded_text}")
print(f"🔓 Dekodlangan Matn: {decoded_text}")
print(f"📜 Huffman Kodlari: {huff_dict}")
print(f"📏 Original Matn uzunligi: {len(text)} ta belgi")
print(f"📏 Kodlangan Matn uzunligi: {len(encoded_text)} ta bit")
print(f"📉 Siqilish koeffitsiyenti: {len(encoded_text) / len(text):.2f}x")