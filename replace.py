
path = "ಚ.txt"
# Open the input file in read mode and output file in write mode
with open(path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace ¾ with ಱ
content = content.replace("¾", "ಱ")
content = content.replace("¿Â", "ೞಿ")
content = content.replace("ಱÂ", "ಱಿ")
content = content.replace("¿õï", "ೞ್")
content = content.replace("¿õÉ", "ಱೆ")
content = content.replace('0', '೦')
content = content.replace('1', '೧')
content = content.replace('2', '೨')
content = content.replace('3', '೩')
content = content.replace('4', '೪')
content = content.replace('5', '೫')
content = content.replace('6', '೬')
content = content.replace('7', '೭')
content = content.replace('8', '೮')
content = content.replace('9', '೯')
content = content.replace("-","–")
content = content.replace("¿","ೞ")
content = content.replace("A","ಂ")
# content = content.replace("್ರ","ç")
# Save the modified content to a new file or overwrite the existing file
with open(path, "w", encoding="utf-8") as file:
    file.write(content)

print("Replacement complete. Check output.txt.")
