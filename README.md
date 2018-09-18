# metapost-colorbrewer

An implementation of the colour palettes from http://colorbrewer2.org for Metapost

The Colorbrewer palettes are copyright (c) Cynthia Brewer, Mark Harrower and The Pennsylvania State University.

This implementation that makes them available for Metapost is copyright (c) 2018 Toby Thurston.

Toby Thurston -- 18 Sept 2018

## Provides

- A Python script that reads "cb.csv" from https://github.com/axismaps/colorbrewer/
  and creates a Metapost include-file that includes all the Colorbrewer definitions as
  Metapost colors (cmyk or rgb, as you please)

- colorbrewer-cmyk.mp
- colorbrewer-rgb.mp
- colorbrewer-sampler.mp

![Colorbrewer Sampler](colorbrewer-sampler.png)

## Usage

(Assumes you are on osx, adapt as needed for windows, or linux).

- git clone http://github.com/thruston/metapost-colorbrewer
- mkdir -p ~/Library/texmf/metapost
- cp metapost-colorbrewer/colorbrewer-cmyk.mp ~/Library/texmf/metapost
- cp metapost-colorbrewer/colorbrewer-rgb.mp ~/Library/texmf/metapost

and then look at metapost-colorbrewer/colorbrewer-sampler.mp for an example of
how to use them.  Once they are in your local texmf tree you just need to include
them with "include colorbrewer-rgb" or "include colorbrewer-cmyk"

## Licence

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
