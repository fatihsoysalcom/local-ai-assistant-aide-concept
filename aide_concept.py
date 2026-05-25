import sys

# Simulate a local AI assistant that processes user input without sending data externally.
# This is a simplified demonstration of the Aide concept.

def local_ai_assistant(prompt):
    """Processes a user prompt locally and returns a response."""
    prompt_lower = prompt.lower()

    # Basic keyword matching to simulate AI understanding
    if "merhaba" in prompt_lower or "selam" in prompt_lower:
        return "Merhaba! Size nasıl yardımcı olabilirim?"
    elif "saat kaç" in prompt_lower:
        # In a real scenario, this might access system time, but for demo, we'll hardcode.
        return "Üzgünüm, şu anki saati belirleyemiyorum. Bu özellik yerel olarak geliştirilmelidir."
    elif "hava durumu" in prompt_lower:
        return "Hava durumu bilgisi için harici bir servise bağlanmak gerekir. Aide, bu tür verileri cihazınızda güvenli tutar."
    elif "nasilsin" in prompt_lower:
        return "Ben bir yapay zeka asistanıyım, bu yüzden duygularım yok. Ama size yardımcı olmak için buradayım!"
    elif "görüşürüz" in prompt_lower or "hoşça kal" in prompt_lower:
        return "Görüşmek üzere!"
    else:
        return "Anlamadım. Lütfen farklı bir şekilde ifade eder misiniz?"

if __name__ == "__main__":
    print("Aide Yerel Yapay Zeka Asistanı Konsepti")
    print("----------------------------------------")
    print("Bu, verilerinizi cihazınızda tutan bir yapay zeka asistanının temel bir simülasyonudur.")
    print("Çıkmak için 'çıkış' yazın.")
    print("----------------------------------------")

    while True:
        user_input = input("Siz: ")
        if user_input.lower() == "çıkış":
            print("Aide: Hoşça kalın!")
            sys.exit(0)

        # The core concept: processing happens locally.
        response = local_ai_assistant(user_input)
        print(f"Aide: {response}")
