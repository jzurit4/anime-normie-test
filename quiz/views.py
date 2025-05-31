from django.shortcuts import render
from django.http import JsonResponse
from urllib.parse import quote
from .forms import NormieAnimeForm

def quiz_view(request):
    if request.method == 'POST':
        form = NormieAnimeForm(request.POST)
        if form.is_valid():
            score = sum(1 for answer in form.cleaned_data.values() if answer == 'yes')
            percentage = round((score / len(form.cleaned_data)) * 100)
            if percentage >= 80:
                message = "Eres un ultra normie. ¿Has visto algo más allá de los tops de YouTube?"
            elif percentage >= 50:
                message = "Eres normie, pero hay esperanza."
            else:
                message = "No eres normie, ¡felicidades!"

            share_text = f"Saqué un {percentage}% de normie en el test de anime. {message} ¡Haz el test tú también!"
            share_url = f"https://twitter.com/intent/tweet?text={quote(share_text)}"

            return JsonResponse({
                'percentage': percentage,
                'message': message,
                'share_url': share_url,
            })
        else:
            return JsonResponse({'error': 'Formulario inválido'}, status=400)

    # Si GET, mostrar la página HTML
    form = NormieAnimeForm()
    return render(request, 'quiz/quiz.html', {'form': form})
