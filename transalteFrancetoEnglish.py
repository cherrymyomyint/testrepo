translation = language_translator.translate(
    text='Hello', model_id='fr-en').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))
