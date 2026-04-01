import codecs
import re

# ABRIL DATA
abril_evening = [
    (1, 1, "azul", "LP162<br>CRISTIANA"),
    (2, 3, "cinza", "Sem<br>Aula"),
    (6, 7, "azul", "LP162<br>CRISTIANA"),
    (8, 8, "azul", "CIP18<br>FELLIPE"),
    (9, 10, "azul", "FEA80<br>JORGE"),
    (13, 14, "azul", "LP162<br>CRISTIANA"),
    (17, 18, "azul", "FEA80<br>JORGE"),
    (20, 20, "azul", "LP162<br>CRISTIANA"),
    (21, 21, "cinza", "Feriado"),
    (23, 23, "azul", "FEA80<br>JORGE"),
    (24, 24, "cinza", "Sem<br>Aula"),
    (27, 27, "azul", "LP162<br>CRISTIANA"),
    (28, 29, "azul", "CIP18<br>FELLIPE"),
    (30, 30, "azul", "FEA80<br>JORGE")
]
abril_morning = [(11, 11, "azul", "LP162<br>CRISTIANA")]

# MAIO DATA
maio_evening = [
    (1, 1, "cinza", "Feriado"),
    (4, 5, "azul", "LP162<br>CRISTIANA"),
    (7, 8, "azul", "FEA80<br>JORGE"),
    (11, 12, "azul", "LP162<br>CRISTIANA"),
    (15, 15, "azul", "FEA80<br>JORGE"),
    (18, 19, "azul", "LP162<br>CRISTIANA"),
    (20, 20, "azul", "CIP18<br>FELLIPE"),
    (21, 22, "azul", "FEA80<br>JORGE"),
    (25, 26, "azul", "LP162<br>CRISTIANA"),
    (28, 29, "azul", "FEA80<br>JORGE")
]
maio_morning = [(9, 9, "azul", "LP162<br>CRISTIANA"), (30, 30, "azul", "LP162<br>CRISTIANA")]

# JUNHO DATA
junho_evening = [
    (1, 3, "azul", "LP162<br>CRISTIANA"),
    (4, 4, "cinza", "Sem<br>Aula"),
    (5, 5, "azul", "FEA80<br>JORGE"),
    (8, 9, "azul", "LP162<br>CRISTIANA"),
    (10, 10, "azul", "CIP18<br>FELLIPE"),
    (12, 12, "azul", "FEA80<br>JORGE"),
    (15, 17, "azul", "LP162<br>CRISTIANA"),
    (18, 18, "azul", "FEA80<br>JORGE"),
    (19, 19, "cinza", "Sem<br>Aula"),
    (22, 22, "azul", "LP162<br>CRISTIANA"),
    (23, 24, "cinza", "Sem<br>Aula"),
    (25, 25, "azul", "CIP18<br>FELLIPE"),
    (29, 30, "azul", "LP162<br>CRISTIANA")
]
junho_morning = []

# JULHO DATA
julho_evening = [
    (1, 1, "azul", "LP162<br>CRISTIANA"),
    (2, 2, "cinza", "Sem<br>Aula"),
    (3, 3, "azul", "FEA80<br>JORGE"),
    (6, 8, "azul", "LP162<br>CRISTIANA"),
    (10, 10, "azul", "FEA80<br>JORGE"),
    (31, 31, "cinza", "Sem<br>Aula")
]
julho_morning = []

def text_to_name(text):
    text = text.replace("<br>", " ")
    if "LP162" in text: return ("Lógica de Programação | LP162", "Prof. Cristiana Pereira Bispo", "glow-blue")
    if "FEA80" in text: return ("Fund. de Eletroeletrônica | FEA80", "Prof. Jorge Luiz dos Santos", "glow-purple")
    if "CIP18" in text: return ("Criatividade e Ideação | CIP18", "Prof. Fellipe Bina Barros", "glow-yellow")
    if "Sem" in text or "Feriado" in text: return ("Sem Aulas Programadas", "", "empty")
    return (text, "", "glow-blue")

def build_month(month_id, month_name, days_count, start_day_offset, morning_blocks, evening_blocks):
    day_names = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    short_mb = month_name[:3].upper()
    
    # Unfold blocks to specific days
    schedule = { d: [] for d in range(1, days_count + 1) }
    
    for start, end, cls, text in morning_blocks:
        for d in range(start, end + 1):
            schedule[d].append({'time': '09:00 - 12:00', 'text': text})
            
    for start, end, cls, text in evening_blocks:
        for d in range(start, end + 1):
            schedule[d].append({'time': '18:40 - 21:40', 'text': text})
            
    output = []
    output.append(f'<div id="{month_id}" class="tab-content" style="{"display: block; opacity: 1; transform: translateY(0);" if month_id=="abril" else "display: none; opacity: 0; transform: translateY(20px);" }">')
    output.append(f'<div class="month-title-modern">{month_name} / 2026</div>')
    
    for d in range(1, days_count + 1):
        weekday = day_names[(d - 1 + start_day_offset) % 7]
        is_weekend = weekday in ["Sábado", "Domingo"]
        
        blocks = schedule[d]
        
        # Determining if it is empty day
        is_empty = len(blocks) == 0 or (len(blocks)==1 and "Sem" in blocks[0]['text']) or (len(blocks)==1 and "Feriado" in blocks[0]['text'])
        
        cls_card = "bento-card fade-up empty-day" if is_empty else "bento-card fade-up"
        
        output.append(f'  <div class="{cls_card}">')
        output.append(f'      <div class="bento-date">')
        output.append(f'         <span class="day">{d:02d}</span>')
        output.append(f'         <span class="month">{short_mb}</span>')
        output.append(f'         <span class="weekday">{weekday}</span>')
        output.append(f'      </div>')
        output.append(f'      <div class="bento-classes">')
        
        if is_empty:
             msg = "Sem Aulas Programadas - Final de Semana" if is_weekend else "Sem Aulas Programadas"
             if len(blocks) == 1 and "Feriado" in blocks[0]['text']:
                 msg = "Feriado Escolar"
             output.append(f'         <div class="class-item empty hover-track">')
             output.append(f'             <span>{msg}</span>')
             output.append(f'         </div>')
        else:
            for b in blocks:
                name, prof, g_cls = text_to_name(b['text'])
                if g_cls == "empty": continue
                output.append(f'         <div class="class-item {g_cls} hover-track">')
                output.append(f'             <div class="class-time">{b["time"]}</div>')
                output.append(f'             <div class="class-name">{name}</div>')
                output.append(f'             <div class="class-prof"><i class="icon-user"></i> {prof}</div>')
                output.append(f'         </div>')
             
        output.append(f'      </div>')
        output.append(f'  </div>')
        
    output.append('</div>')
    return "\n".join(output)

months_html = []
months_html.append(build_month("abril", "Abril", 30, 2, abril_morning, abril_evening))
months_html.append(build_month("maio", "Maio", 31, 4, maio_morning, maio_evening))
months_html.append(build_month("junho", "Junho", 30, 0, junho_morning, junho_evening))
months_html.append(build_month("julho", "Julho", 31, 2, julho_morning, julho_evening))

combined_html = "\n".join(months_html)

injection = f'''
                        <!-- TIMELINE TOOLBAR (FILTRO DE VISIBILIDADE) -->
                        <div class="timeline-toolbar">
                            <span class="toolbar-label">Visualização do Mês:</span>
                            <label class="toggle-switch">
                                <input type="checkbox" id="toggle-empty-days" checked>
                                <span class="slider"></span>
                            </label>
                            <span class="toolbar-status">Apenas Dias de Aula</span>
                        </div>
                        
{combined_html}
'''


# Update index.html
with codecs.open("index.html", "r", "utf-8") as f:
    html = f.read()

start_marker = '<div class="timeline-feed hide-empty-days">'
start_idx = html.find(start_marker)

end_marker = '</div>\n                </div>\n\n                <script>'
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # Inject directly
    new_html = html[:start_idx] + '<div class="timeline-feed hide-empty-days">\n' + injection + '\n                ' + html[end_idx:]
    with codecs.open("index.html", "w", "utf-8") as f:
        f.write(new_html)
    print("timeline feed sucessfully updated in index.html")
else:
    print("error: markers not found. Did the HTML structure change?")
