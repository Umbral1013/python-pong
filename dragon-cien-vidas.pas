{
Nombre del programador: Umbral1013
Nombre del programa: Derrota al dragon de las cien vidas.
Fecha de creacion: 08/02/2024.
Descripcion del programa: Juego sencillo que consiste en eliminar al
    dragon de las cien vidas con cuatro armas.
}

Program DragonCienVidas;

{ Aparentemente esto se usa para limpiar la pantalla. }

Uses Crt, Sysutils;


{ Regresa la probabilidad de acertar el golpe en funcion
del numero de golpe que se trate.
}
Function ProbAciertoSgTurno(ordGolpe: integer):   integer;

Var
    probabilidad:   integer;
Begin
    probabilidad := 0;
    Case ordGolpe Of
        0:   probabilidad := 80;
        1:   probabilidad := 70;
        2:   probabilidad := 60;
        3:   probabilidad := 50;
        4:   probabilidad := 40;
        5:   probabilidad := 30;
        Else
            Writeln('E: Orden de golpe recibido no valido.');
    End;
    ProbAciertoSgTurno := probabilidad;
End;



{ Calcula cuantos golpes van a atinar tomando en cuenta el numero
de golpe (o sea, el turno actual) y las veces que puede golpear el
arma.
}
Function GolpesAcertados(ordGolpe, vecGolpe: integer):   integer;

Var
    aciertos:   integer;
    semilla:   integer;
    i:   integer;
Begin
    aciertos := 0;
    i := 0;
    While (i < vecGolpe) Do
        Begin
            Randomize;
            semilla := random(101);
            If (semilla > 0) And (semilla < ProbAciertoSgTurno(ordGolpe)) Then
                aciertos := aciertos + 1;
            i := i + 1;
        End;
    GolpesAcertados := aciertos;
End;


{ Calcula el danno causado segun el arma en el turno actual.
Si se llama a GolpesAcertados por separado, la probabilidad
cambia.
}
Function DannoSgArmaGa(ataque, vecGolpe, ordGolpe: integer):   integer;

Var
    danno:   integer;
    acertados:   integer;
Begin
    acertados := GolpesAcertados(ordGolpe, vecGolpe);
    danno := acertados * ataque;
    DannoSgArmaGa := danno;
End;


Function DannoArma(idArma: integer):   integer;
{ Establece la cantidad de danno que puede hacer cada arma. }

Var
    ataque:   integer;
Begin
    Case idArma Of
        1:   ataque := 5;
        2:   ataque := 15;
        3:   ataque := 30;
        4:   ataque := 50;
        Else
            Writeln('E: Identificador de arma no valido.');
    End;
    DannoArma := ataque;
End;


Function GolPosArma(idArma: integer):   integer;
{ Establece la cantidad de golpes que puede hacer cada arma. }

Var
    golpesPosibles:   integer;
Begin
    Case idArma Of
        1:   golpesPosibles := 4;
        2:   golpesPosibles := 2;
        3:   golpesPosibles := 1;
        4:   golpesPosibles := 1;
        Else
            Writeln('E: Identificador de arma no valido.');
    End;
    GolPosArma := golpesPosibles;
End;


Procedure MostrarAyuda;
Begin
    Writeln('-- Informacion del juego --');
    Writeln('Tienes cuatro armas a tu disposicion.');
    Writeln('El arma mas debil es el monton de piedras, mientras que el arma mas');
    Writeln('poderosa es el arco sagrado. La primera arma que uses tiene solo el');
    Writeln('80% de probabilidades de acertar, en cambio, la ultima que uses');
    Writeln('tiene el 50% de probabilidad de acertar.');
    Writeln('Elige tus armas sabiamente.');
    Write('Oprime cualquier tecla para continuar...');
    Readln();
End;


Procedure MostrarInfo(salDragon, probGolpear, turnRes: integer);
Begin
    Writeln('@@@ SALUD DEL DRAGON: ', salDragon, ' @@@');
    Writeln('@@@ TURNOS RESTANTES: ', turnRes, ' @@@');
    Writeln('==========================');
    Writeln('@@@ ELIGE TU ARMA @@@');
    Writeln('[1] Monton de piedras');
    { Recuerdame alinear esto correctamente. }
    Writeln('05 danno');
    Writeln('Puede golpear 4 veces');
    Writeln(probGolpear, '% de acertar al menos un golpe');
    Writeln('------------------');
    Writeln('[2] Espada');
    Writeln('15 danno');
    Writeln('Puede golpear 2 veces');
    Writeln(probGolpear, '% de acertar al menos un golpe');
    Writeln('------------------');
    Writeln('[3] Explosivos');
    Writeln('30 danno');
    Writeln('Puede golpear 1 vez');
    Writeln(probGolpear, '% de acertar al menos un golpe');
    Writeln('------------------');
    Writeln('[4] Arco sagrado');
    Writeln('50 danno');
    Writeln('Puede golpear 1 vez');
    Writeln(probGolpear, '% de acertar al menos un golpe');
    Writeln('------------------');
End;


Procedure Jugar;

Var
    turTotales:   integer;
    turActual:   integer;
    turRestantes:   integer;
    eleArma:   integer;
    atqArma:   integer;
    golArma:   integer;
    salDragon:   integer;
    pronDanno:   integer;
    danno:   integer;
Begin
    turTotales := 5;
    salDragon := 100;
    turActual := 0;
    While ((turActual < turTotales) And (salDragon > 0)) Do
        Begin
            turRestantes := turTotales - turActual;
            pronDanno := ProbAciertoSgTurno(turActual);
            ClrScr;
            MostrarInfo(salDragon, pronDanno, turRestantes);
            Write('>>> Elige tu arma: ');
            Readln(eleArma);
            atqArma := DannoArma(eleArma);
            golArma := GolPosArma(eleArma);
            danno := DannoSgArmaGa(atqArma, golArma, turActual);
            salDragon := salDragon - danno;
            turActual := turActual + 1;

            Writeln('Le has quitado ', danno, ' vidas al dragon!!');

            { Son milisegundos en Pascal. }
            Sleep(3000);
        End;

    If (salDragon > 0) Then
        Begin
            Writeln('Agotado, te das cuenta de la verdad: Has usado todas tus');
            Writeln('herramientas y no has podido acabar con el dragon');
            Writeln('Decides correr, mejor prevenir que lamentar.');
            Writeln('DERROTA.');
        End
    Else
        Begin
            Writeln('Tras una ardua batalla, el dragon se retira indignado,');
            Writeln('haciendo notar que has interrumpido su suenno.');
            Writeln('- La gente ya no tiene respeto!, sobre todo usted,');
            Writeln(' amigo mio. Me voy, ire a un lugar mas tranquilo.');
            Writeln('VICTORIA');
        End;
    Writeln('Presiona cualquier tecla para continuar...');
    Readln();
End;


Var
    ejecutar:   integer;
    opcion:   integer;
Begin   { Main }
    ejecutar := 1;
    While (ejecutar <> 0) Do
        Begin
            ClrScr;
            Writeln('DERROTA AL DRAGON DE LAS CIEN VIDAS');
            Writeln('Menu principal');
            Writeln('[1] Jugar');
            Writeln('[2] Ayuda');
            Writeln('[3] Creditos');
            Writeln('[4] Salir del juego');
            Write('Elige una opcion: ');
            Readln(opcion);

            Case opcion Of
                1:   Jugar();
                2:   MostrarAyuda();
                3:
                     Begin
                         Writeln('Escrito por Umbral1013.');
                         Writeln('26 de marzo del 2024.');
                         Writeln('Presiona una tecla para continuar...');
                         Readln();
                     End;
                4:
                     Begin
                         Writeln('Hasta pronto, aventurero!');
                         ejecutar := 0;
                     End;
                Else
                    Begin
                        Writeln('Esa opcion no existe.');
                        Sleep(3000);
                    End;
            End;
        End;
    Writeln('El programa ha terminado. Presiona una tecla para continuar.');
    Readln();
End. { Main }


{ NOTAS:
Recuerda que es mejor designar buenos nombres, y observar la logica con
cuidado.  Usa los tipos de datos mas adecuados para cada caso, un monton de
cosas en este programa son enteros, cuando no es necesario que lo sean.

Las funciones deben llamarse por lo que producen, los procedimientos deben
llamarse por lo que hacen.

Ademas, la historia en esta cosa es un chiste mal contado, ni siquiera da risa
XD. Pensare en algo mejor. Probablemente deberia haber hecho eso primero.

Tambien hay que corregir los problemas de la version original:

Quiza para hacerlo mas dificil podria reducir el danno que hacen las armas, o
cambiar la probabilidad de ciertos ataques... No se, quiza despues veo eso.
Falta implementar lo del numero de usos maximos de las armas.

28/03/2024
Bueno, ahora nada le hace danno al dragon.
Actualizacion: Era porque habia olvidado hacer return en la funcion ProbGolpear
XDDD.
}
