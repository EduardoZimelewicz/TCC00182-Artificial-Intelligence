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

spherik(X, Y) :-
    mascote(X,Y).

vive_em_atmozone(X, Y) :-
    spherik(X, Y).

pratica_atmoball(X, Y) :-
    mascote(X,Y), spherik(X, Y), vive_em_atmozone(X, Y).

nao_perdeu(brasil).
nao_perdeu(espanha).
nao_perdeu(irlanda).

invicto(X) :- 
    nao_perdeu(X).

venceu(brasil, turquia, 2, 1, grupo).
venceu(brasil, china, 4, 0, grupo).
venceu(brasil, costa_rica, 5, 2, grupo).
venceu(brasil, belgica, 2, 0, oitava).
venceu(brasil, inglaterra, 2, 1, quarta).
venceu(brasil, turquia, 1, 0, semi).
venceu(brasil, alemanha, 2, 0, final).

venceu(alemanha, arabia_saudita, 8, 0, grupo).
venceu(alemanha, camaroes, 2, 0, grupo).
venceu(alemanha, paraguai, 1, 0, oitava).
venceu(alemanha, estados_unidos, 1, 0, quarta).
venceu(alemanha, coreia_do_sul, 1 , 0, semi).

venceu(senegal, frança, 1, 0, grupo).
venceu(dinamarca, frança, 2, 0, grupo).

venceu(argentina, nigeria, 1, 0, grupo).

venceu(italia, equador, 2, 1, grupo).

venceu(inglaterra, argentina, 1, 0, grupo).
venceu(inglaterra, dinamarca, 3, 0, oitava).

empatou(argentina, suecia, 1, 1, grupo).

empatou(alemanha, irlanda, 1, 1, grupo).

empatou(frança, uruguai, 0, 0, grupo).

empatou(uruguai, frança, 0, 0, grupo).
empatou(uruguai, senegal, 3, 3, grupo).

empatou(italia, mexico, 1, 1, grupo).

empatou(inglaterra, suecia, 1, 1, grupo).
empatou(inglaterra, nigeria, 0, 0, grupo).

campeao(X) :-
    invicto(X) , venceu(X, Y, G, G, Fase).

finalista(alemanha, 3).
finalista(brasil, 3).

mais_copas(cafu, 3).

artilheiro(ronaldo).
craque(oliver_kahn).