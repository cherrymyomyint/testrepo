authenticator = IAMAuthenticator('your_api_key')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url('https://gateway.watsonplatform.net/language-translator/api')
