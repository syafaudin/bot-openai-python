import openai

openai.api_key =""

while True:
    model_engine = "text-davinci-003"
    prompt = input("Masukkan kata kunci")
    if "keluar" in prompt or "tutup" in prompt:
        break
    pengaturan = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_token = 1024,
        n = 1, 
        stop = none,
        temperatur = 0.5  
        )
    response = pengaturan.choise[0].text
    print(response)
