sede(japão).
sede(coreia_do_sul).

ultima_campea(frança).

campea_antiga(brasil).
campea_antiga(argentina).
campea_antiga(uruguai).
campea_antiga(alemanha).
campea_antiga(italia).
campea_antiga(inglaterra).

nao_perdeu(brasil).
nao_perdeu(espanha).
nao_perdeu(irlanda).

venceu(alemanha, arabia_saudita, 8, 0, grupo).
venceu(alemanha, camaroes, 2, 0, grupo).
venceu(alemanha, paraguai, 1, 0, oitava).
venceu(alemanha, estados_unidos, 1, 0, quarta).
venceu(alemanha, coreia_do_sul, 1, 0, semi).

venceu(brasil, turquia, 2, 1, grupo).
venceu(brasil, china, 4, 0, grupo).
venceu(brasil, costa_rica, 5, 2, grupo).
venceu(brasil, belgica, 2, 0, oitava).
venceu(brasil, inglaterra, 2, 1, quarta).
venceu(brasil, turquia, 1, 0, semi).
venceu(brasil, alemanha, 2, 0, final).

venceu(senegal, frança, 1, 0, grupo).
venceu(dinamarca, frança, 2, 0, grupo).
venceu(argentina, nigeria, 1, 0, grupo).
venceu(italia, equador, 2, 0, grupo).
venceu(croacia, italia, 2, 1, grupo).
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

finalista(alemanha, 3). %numero de finais
finalista(brasil, 3). 

mais_copas(cafu, 3).
mais_copas(buffon, 4).
mais_copas(rafa_marquez, 5).
mais_copas(maldini, 4).
mais_copas(ronaldo, 3).

defesa_jogo(shorunmu,9 rdiv 2).
defesa_jogo(majdan,5). 
defesa_jogo(dudek,9 rdiv 2).
defesa_jogo(dabanovic,8). 
defesa_jogo(rustu,5).
defesa_jogo(simeunovic,9 rdiv 2). 

gols(batistuta,1).
gols(vieri,4).
gols(klose,5).
gols(owen,2).
gols(ronaldo,8).

/*Tive que colocar team pq time é palavra reservada*/
jogador_team(ronaldo,brasil).
jogador_team(klose,alemanha).
jogador_team(oliver_kahn,alemanha).
jogador_team(batistuta,argentina).
jogador_team(vieri,italia).
jogador_team(owen,inglaterra).

invicto(X) :- 
    nao_perdeu(X).

vaga_concedida(X) :- 
    sede(X) ; ultima_campea(X).

classificada(X) :-
    campea_antiga(X) ; ultima_campea(X) ; sede(X).

campeao(X) :-
    invicto(X), 
    venceu(X,_,_,_,_),
    format('~w', [X]).

disputas(X) :-
    mais_copas(X, Y),
    not((
        mais_copas(_,W),
        W > Y
       )),
    format('~w', [X]).
    
artilheiro(X) :-
	gols(X,Y),
    not((
		gols(_,W),
		W > Y
       )),
	jogador_team(X,T),
	format('~w foi o artilheiro da copa pelo time ~w', [X,T]).

mais_defesa_jogo(Y) :- 
	defesa_jogo(Y,X),
    not((
		defesa_jogo(_,W),
		W > X
       )),
	format('~w foi o goleiro com mais defesa/jogo', [Y]).

time_gols(X, []) :-
    findall(Y, venceu(X,_,Y,_,_), GVenceu),
    sumlist(GVenceu, G1),
    findall(Z, empatou(X,_,Z,_,_), GEmpatou1),
    sumlist(GEmpatou1, G2),
    findall(U, empatou(_,X,_,U,_), GEmpatou2),
    sumlist(GEmpatou2, G3),
    findall(U, venceu(_,X,_,U,_), GPerdeu),
    sumlist(GPerdeu, G4),
    G is G1 + G2 + G3 + G4,
    format('~w', [G]).

len([],0). 
len([_|T],N)  :-  
    len(T,X),  N  is  X+1.

n_vitorias(X, V) :-
    findall(X, venceu(X,_,_,_,_), GV1),
    nth0(0,GV1,X),
    len(GV1, V).

resposta(X) :-
	X == 'Quem é o campeão?' -> campeao(_);
	X == 'Quem foi o artilheiro das campeãs?' -> artilheiro(_);
	X == 'Qual goleiro fez mais defesa/jogo?' -> mais_defesa_jogo(_);
	X == 'Qual jogador tem mais copas disputadas?'-> disputas(_);
    X == 'Quantos gols fez a Alemanha?'-> time_gols(alemanha, []).

read_question :- 
    read(X),
    resposta(X).