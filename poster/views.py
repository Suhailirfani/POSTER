from django.shortcuts import render, redirect, get_object_or_404
from .models import Program
from .forms import ProgramForm, ResultForm

def home(request):
    """Home page: List all created programs."""
    programs = Program.objects.all().order_by('-id')
    return render(request, 'poster/home.html', {
        'programs': programs,
    })

def create_program(request):
    """Create a new program."""
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('poster:home')
    else:
        form = ProgramForm()
    return render(request, 'poster/program_form.html', {'form': form})

def program_detail(request, pk):
    """View to select item and template for a specific program."""
    program = get_object_or_404(Program, pk=pk)
    form = ResultForm(program=program)
    templates_range = range(1, 22)  # 1 to 21
    return render(request, 'poster/program_detail.html', {
        'program': program,
        'form': form,
        'templates_range': templates_range,
    })

def preview(request, pk):
    """Render poster preview with submitted data combined with program data."""
    program = get_object_or_404(Program, pk=pk)
    
    if request.method == 'POST':
        form = ResultForm(request.POST, program=program)
        if form.is_valid():
            data = form.cleaned_data
            
            # Combine program data with form data
            combined_data = {
                'program_name': program.name,
                'event_date': program.date,
                'place': program.place,
                'authority': program.authority,
                **data
            }
            
            template_id = combined_data.get('template_id', 1)
            if template_id < 1 or template_id > 21:
                template_id = 1
            template_name = f'poster/templates/template_{template_id:02d}.html'
            
            return render(request, 'poster/preview.html', {
                'program': program,
                'data': combined_data,
                'template_id': template_id,
                'template_name': template_name,
            })
        else:
            form = ResultForm(request.POST, program=program)
    else:
        form = ResultForm(program=program)

    templates_range = range(1, 22)
    return render(request, 'poster/program_detail.html', {
        'program': program,
        'form': form,
        'templates_range': templates_range,
        'errors': True,
    })

def edit_program(request, pk):
    """Edit an existing program."""
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect('poster:program_detail', pk=program.pk)
    else:
        form = ProgramForm(instance=program)
    return render(request, 'poster/program_form.html', {'form': form, 'is_edit': True, 'program': program})

def delete_program(request, pk):
    """Delete a program."""
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('poster:home')
    return render(request, 'poster/program_confirm_delete.html', {'program': program})
