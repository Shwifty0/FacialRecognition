from face_recognition import Recognise
recognize = Recognise()
user_input = input("Who are you?")

if user_input:
    recognize.is_person(user_input=user_input)