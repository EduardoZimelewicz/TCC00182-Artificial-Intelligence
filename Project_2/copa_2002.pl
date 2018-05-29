sede(japão).
sede(coreia_do_sul).

ultima_campea(frança).

vaga_concedida(X) :- 
    sede(X) ; ultima_campea(X).

campea_antiga(brasil).
campea_antiga(argentina).
campea_antiga(uruguai).
campea_antiga(alemanha).
campea_antiga(italia).
campea_antiga(inglaterra).

classificada(X) :-
    campea_antiga(X) ; ultima_campea(X) ; sede(X).

mascote(kaz, roxo).
mascote(ato, laranja).
mascote(nik,azul).

spherik(X) :-
    mascote(X,Y).

vive_em_atmozone(X) :-
    spherik(X).

pratica_atmoball(X) :-
    mascote(X,Y), spherik(X), vive_em_atmozone(X).

nao_perdeu(brasil).

invicto(X) :- 
    nao_perdeu(X).

venceu(brasil, turquia, 2, 1, grup).
venceu(brasil, china, 4, 0, grupo).
venceu(brasil, costa_rica, 5, 2, grupo).
venceu(brasil, belgica, 2, 0, oitava).
venceu(brasil, inglaterra, 2, 1, quarta).
venceu(brasil, turquia, 1, 0, semi).
venceu(brasil, alemanha, 2, 0, final).

venceu(senegal, frança, 1, 0, grupo).
venceu(dinamarca, frança, 2, 0, grupo).
empatou(uruguai, frança, 0, 0, grupo).

campeao(X) :-
    invicto(X) , venceu(X, Y, G_1, G_2, Fase).

artilheiro(ronaldo).
craque(oliver_kahn).



