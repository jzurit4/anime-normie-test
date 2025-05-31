from django import forms

class NormieAnimeForm(forms.Form):
    YES_NO = [('yes', 'Sí'), ('no', 'No')]

    question_1 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="¿El género de peleas es tu favorito?")
    question_2 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="¿Prefieres ver anime doblado al español?")
    question_3 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="¿Solo ves anime en Netflix?")
    question_4 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="¿Tu anime/manga favorito es Jujutsu Kaisen, CSM, One Piece, Naruto o Boku no hero?")
    question_5 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="No sabes qué es un fansub")
    question_6 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="Solo das notas altas")
    question_7 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="Piensas que todos los isekais son iguales")
    question_8 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="No has jugado una visual novel")
    question_9 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="¿Tu seinen favorito es Vinland Saga, Berserk o Vagabond?")
    question_10 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="No sabes quien es Ozamu Tezuka")
    question_11 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="No sabes diferenciar género de demografia")
    question_12 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="¿Evitas ver animes antiguos?")
    question_13 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="No has leido una novela ligera")
    question_14 = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="¿Tu pelicula de anime favorita es Koe no Katachi, I wanna eat your pancreas o Your Name?")
