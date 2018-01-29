# RuinWorld

Notes:
- Game is made for Finnish Game Jam/Global Game Jam 2018
- We used about 17hrs to coding with no previous experience of cocos2d and the Python
- We noticed that we are not using "good conventions" of the Python when naming stuff
- Codes should be placed here in the root folder (cannot access parent folder in Python? blah no time to investigate)
- 'assets' is a submodule for RuinWorld-Assets repo


## Required SDL dll's
You need to download v1.2 version of these dll's

[SDL](https://www.libsdl.org/download-1.2.php)
* SDL.dll


[SDL_mixer 1.2](https://www.libsdl.org/projects/SDL_mixer/release-1.2.html)
* libvorbis-0.dll
* libvorbisfile-3.dll
* smpeg.dll
* libFLAC-8.dll
* libmikmod-2.dll
* libogg-0.dll

## TODOish
What we had in list to do to get the minimum viable product going on. Not in particular order:

1. sounds, musics and effects to the game

2. events -> when pressing the "Purhcase" buttons, event will be send to different layer to do the actions (Buy unit if enough money, show unit on the screen etc).

3. AI for enemy player. Simple AI that will purchase random unit when available funds.

4. Increasing resources every second and after getting enemy damaged

5. Units and their properties

6. Win & Lose condition -> showing end screen and then back to main menu

7. Power vs other units™ -table

|            | Many tanks | Missile | Nuke | Few tanks |
|------------|------------|---------|------|-----------|
| Many tanks |      0     |    +    |   x  |     -     |
|    Missile |      -     |  minor  |   x  |     +     |
|       Nuke |      x     |    x    |   x  |     x     |
|  Few tanks |      +     |    -    |   x  |     0     |
