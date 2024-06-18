import emoji
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}
print("Emojis disponíveis:")
for simbolo, codigo in emojis_disponiveis.items():
    print(f"{simbolo} - {codigo}")
frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")
frase_emojizada = emoji.emojize(frase_codificada)
print("\nFrase emojizada:")
print(frase_emojizada)