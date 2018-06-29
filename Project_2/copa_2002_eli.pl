jogo(brasil, turquia, 2, 1, grupo, [ronaldo, rivaldo]).
jogo(brasil, china, 4, 0, grupo, [roberto_carlos, rivaldo, ronaldinho_gaucho, ronaldo]).
jogo(brasil, costa_rica, 5, 2, grupo, [ronaldo, ronaldo, edmilson, rivaldo, junior]).
jogo(brasil, belgica, 2, 0, oitava, [rivaldo, ronaldo]).
jogo(brasil, inglaterra, 2, 1, quarta, [rivaldo, ronaldinho_gaucho]).
jogo(brasil, turquia, 1, 0, semi, [ronaldo]).
jogo(brasil, alemanha, 2, 0, final, [ronaldo, ronaldo]).

verificaMarcador(J1, J2, G) :-
    J1 = J2,
    G is 1.

verificaMarcador(J1, J2, G) :-
    J1 \= J2,
    G is 0.

qtd_gols(Jogador, [], Total).
qtd_gols(Jogador, [Head], Total) :-
    verificaMarcador(Jogador, Head, G),
    X is Total + G,
    format('~w', [X]).

qtd_gols(Jogador, Marcadores, Total) :-
    /* verificaMarcador(Jogador, Head, G),*/
    findall(Jogador, Marcadores, Total),
    length(Total, TT),
    format('~w', [TT]).

gols_feitos(Jogador, Fase) :-
    jogo(_, _, _, _, Fase, Marcadores),
    findall(Jogador, Marcadores, Total),
    length(Total, TT),
    format('~w fez ~w gols ', [Jogador, TT]).