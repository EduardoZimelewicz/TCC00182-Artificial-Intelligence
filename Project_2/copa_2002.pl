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
venceu(alemanha, coreia_do_sul, 1, 0, semi).

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
    invicto(X) , venceu(X, Y, G_X, G_Y, Fase).

finalista(alemanha, 3). %numero de finais
finalista(brasil, 3). 

mais_copas(cafu, 3). %numero de copas

artilheiro(X) :-
	gols(X,Y),
	gols(Z,W),
	Y > W,
	jogador_team(X,T),
	format('~w foi o artilheiro da copa pelo time ~w', [X,T]).

craque(oliver_kahn).

gols(ronaldo,8).
gols(batistuta,1).
gols(vieri,4).
gols(klose,5).
gols(owen,2).

/*Tive que colocar team pq time é palavra reservada*/
jogador_team(ronaldo,brasil).
jogador_team(klose,alemanha).
jogador_team(oliver_kahn,alemanha).
jogador_team(batistuta,argentina).
jogador_team(vieri,italia).
jogador_team(owen,inglaterra).

mais_defesa_jogo(Y) :- 
	defesa_jogo(Y,X),
	defesa_jogo(Z,W),
	X > W,
	format('~w foi o goleiro com mais defesa/jogo', [Y]).

defesa_jogo(dabanovic,8). 
defesa_jogo(majdan,5). 
defesa_jogo(rustu,5). 
defesa_jogo(dudek,9 rdiv 2).
defesa_jogo(shorunmu,9 rdiv 2).
defesa_jogo(simeunovic,9 rdiv 2). 

read_question :- 
    write('escreva sua pergunta: '),
    	read(X),
    (X = 'Quem é o campeão?' -> campeao(Y), write(Y));
    (X = 'Quem foi o artilheiro das campeãs?' -> artilheiro(W)).
