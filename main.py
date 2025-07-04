from translator import translate_line as translate_python_line
from java_translator import translate_java_line
from llm_translate import explain_with_gpt

USE_LLM = False
LANGUAGE = "java"  # or "python"

translate = translate_java_line if LANGUAGE == "java" else translate_python_line

lines = []
print("💬 Code to English — type 'END' to finish input\n")
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

print("\n🧠 Translation:\n")
for i, line in enumerate(lines, 1): 
    if USE_LLM:
        simple = explain_with_gpt(line)
        explanation = "Generated by GPT-4" 
    else:
        simple, explanation = translate(line)

    print(f"{i}. {line.strip()} → {simple}")
    print(f"   Explanation: {explanation}\n")
