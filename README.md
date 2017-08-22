# freshRAT
Remote Administration Tool

I am studing multiprocessing, sockets, and I figured this would be a fun
project!<br>I am stemming this off from freShell. This is only to be used
for Educational Purposes,<br>not for illegal purposes. <br>


Current Update: 8/21/2017
- Been busy because of irl stuff, other projects, & ctfs.<br>
- Now able to close all processes properly before opening the next.
(Below is a seperate module, mp.py. Needs to be implemented.)
- Interactive Shell now works and its fugly. 
- had problems with original thread executing before worker but "stdout" shows in order. 
(Don't want to use time())
- I'm most likely going to have to REWRITE all this code because of what I learned in
mp.py. Yay!

Current Bugs 8/22/2017
- Interactive shell process makes the Original "main()" processes <defunct>
- Pool.Close() & Pool.Join() not working as planned. Why?
- Lock.acquire() & Lock.release() not working as planned. Why?

Menu: (Under Construction)

1. Shows All Targets (Done)
2. Choose Target (Done)
    - Interactive Shell (Currently Under Construction)
3. Download File (Module Completed, needs implementation)
4. Upload File (Module completed, needs implementation)
5. Exit


Note* - I am currently only using the client for debugging purposes. Haven't fleshed it out<br>
I have been trying to write this same code on C side by side, having a hard time.<br>
Mainly, because everything I code is unsafe and I can buffer overflow it!<br> And the mistakes
on python + C on processing/threading is doubling my time consumption to just finish 1 project to
have a good template to start in C. I think it's a better idea to focus on this and finish, 
THEN move to C. <br>

