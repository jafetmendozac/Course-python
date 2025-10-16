
import emoji

name_emoji = input("Input: ")

print("Output:", emoji.emojize(name_emoji))

#Clean code

# import emoji

# def main():
#     name_emoji = input("Input: ")
#     # Handle aliases like ":thumbsup:" and ensure unknown codes are not broken
#     output = emoji.emojize(name_emoji, language="alias")
#     print("Output:", output)

# if __name__ == "__main__":
#     main()