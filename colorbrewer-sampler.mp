prologues := 3;
outputtemplate := "%j%c.eps";

input colorbrewer-cmyk

beginfig(1);

    x = 0; y = 0; bx = 8; by = 13; path box; box = unitsquare shifted -(1/2,1/2) xscaled bx yscaled by;
    forsuffixes gamut = 
        Blues, Greens, Greys, Oranges, Purples, Reds,
        BuGn, BuPu, GnBu, OrRd, PuBu, PuBuGn,
        PuRd, RdPu, YlGn, YlGnBu, YlOrBr, YlOrRd,
        BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral,
        Accent, DarkTwo, Paired, PastelOne, PastelTwo, SetOne, SetTwo, SetThree:

        for i=3 upto 9:
            if known gamut[i][1]:
                label.lft((str gamut & decimal i) infont "phvr8r", (x,y));
            fi
            for j = 1 upto i:
                if known gamut[i][j]:
                    fill box shifted (x+j*bx, y) withcolor gamut[i][j];
                fi
            endfor
            x := x + i*bx + 72;
        endfor
        y := y + by + 4;
        x := 0;
    endfor
endfig;
end.

