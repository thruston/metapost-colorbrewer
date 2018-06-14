prologues := 3;
outputtemplate := "%j.eps";

input colorbrewer-cmyk

beginfig(1);
    defaultfont := "phvr8r";
    x = 0; y = 0; bx = 8; by = -13; path box; box = unitsquare shifted -(1/2,1/2) xscaled bx yscaled by;
    forsuffixes gamut = 
        Reds, Oranges, Greens, Blues, Purples, Greys,
        Skip,
        OrRd, YlOrRd, YlOrBr, YlGn, BuGn, PuBuGn, YlGnBu, GnBu, PuBu, RdPu, PuRd, BuPu, 
        Skip,
        PRGn, PiYG, BrBG, PuOr, RdGy, RdBu, RdYlBu, RdYlGn, Spectral,
        Skip,
        Accent, DarkTwo, PastelTwo, SetTwo, 
        PastelOne, SetOne, SetThree, Paired:

        for i=3 upto 12:
            if known gamut[i][1]:
                label.lft(decimal i & ":", (x,y));
                if i=3:
                    label.lft(str gamut, (x-15,y));
                fi
            fi
            for j = 1 upto i:
                if known gamut[i][j]:
                    fill box shifted (x+j*bx, y) withcolor gamut[i][j];
                fi
            endfor
            x := x + i*bx + 32;
        endfor
        y := y + by * 17/13;
        x := 0;
    endfor
    label.rt("Single hue, single range",(560,-42));
    label.rt("Multi-hue, single range", (560,-202));
    label.rt("Assortments",             (560,-552));
    label.rt("Multi-range", (780,-402));
    path b; b = unitsquare shifted -(1/2,1/2) yscaled 34 xscaled 233 shifted (720, -120);
    fill b withcolor Paired[4][1]; draw b withcolor Paired[4][2];
    label("Colorbrewer for Metapost" infont "phvb8r" scaled 1.414, center b shifted down);
endfig;
end.
