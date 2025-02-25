
# 💡 **Bonus Challenge (Optional) **  

# If you want an extra challenge, modify the same program to print words in reverse order!   

#  **Example:**  
#  **Input:** "I love Python"  
#  **Output:** "Python love I"  


# Bonus challenge

sentence = "I Love You"
words = sentence.split()
reserved_words = words[::-1]
result = " ".join(reserved_words)
print(result)



sentence = "This is a Python program"
reversed_sentence = " ".join(sentence.split()[::-1])
print(reversed_sentence)