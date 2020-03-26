#Run it w/ python2!
from yattag import Doc

generateXML = "example.html"

doc, tag, text = Doc().tagtext()

'''
with tag('html'):
    with tag('body', id = 'hello'):
        with tag('h1'):
            text('Hello world!')
            text('Hi there!')
        with tag('h2'):
            text('siemanko')
'''

with tag('GPRDane'):
    with tag('Punkt', nr_punktu="04076", kategoria_drogi='DK', nr_drogi='5', odcinek="Szubin-Żnin",  miejscowosc="Wąsosz", jezdnie_dodatkowe="0", klasyfikacja="GPR"):
        with tag('Kierunek', kierunek="L", kier_miejsc="Szubin", pikietaz="81.070", wspol_x="20.333", wspol_y="50.333"):
            with tag('Dzien', data="2020-01-23"):
                with tag('utrudnienia', czas_start="06:10", czas_stop="06:30"):
                    text('ogromna burza')
                with tag('AN_5min', czas="06:00"):
                    text('1;123;23;23;23;3;1;197;0')
                with tag('AN_5min', czas="06:05"):
                    text('1;124;23;24;23;3;1;199;1')
                with tag('AN_5min', czas="06:10"):
                    text('1;123;22;23;22;2;1;194;1')
                with tag('AN_5min', czas="06:15"):
                    text('2;123;23;23;23;3;1;198;2')
                with tag('AN_5min', czas="06:20"):
                    text('1;124;23;23;23;3;1;198;1')     
    with tag('Punkt', nr_punktu="04076", kategoria_drogi='DK', nr_drogi='5', odcinek="Szubin-Żnin",  miejscowosc="Wąsosz", jezdnie_dodatkowe="0", klasyfikacja="GPR"):
        with tag('Kierunek', kierunek="R", kier_miejsc="Szubin", pikietaz="81.070", wspol_x="20.333", wspol_y="50.333"):
            with tag('Dzien', data="2020-01-23"):
                with tag('AN_5min', czas="09:00"):
                    text('1;123;23;23;23;3;1;197;0;10;11;12;13;14;15;16;17;18;19')
                with tag('AN_5min', czas="09:05"):
                    text('1;124;23;24;23;3;1;199;1;10;11;12;13;14;15;16;17;18;19')
                with tag('AN_5min', czas="09:10"):
                    text('1;123;22;23;22;2;1;194;1;10;11;12;13;14;15;16;17;18;19')
                with tag('AN_5min', czas="09:15"):
                    text('2;123;23;23;23;3;1;198;2;10;11;12;13;14;15;16;17;18;19')
                with tag('AN_5min', czas="09:20"):
                    text('1;124;23;23;23;3;1;198;1;10;11;12;13;14;15;16;17;18;19')



#open file for writing
f = open(generateXML, "w")

#write 1st line
f.write('<?xml version="1.0" encoding="utf-8"?>\n')   #new line at the end
f.write(doc.getvalue())
f.close()