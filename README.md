# tiny-chess
chess ai using tinygrad

## plan

### training

 - input:
   - chess dataset
     - take from highest elo available
     - this inherently selects for strongest genes, no need for rl later

 - system:
   - chess board
     - find some python package or smth
   - take board state
     - encode board state
     - chess algebriac notation
   - basically predict the next board state from previous state
     - e.g. if we have a string "wpe4"
     - we just predict the next chars ( or tokens ) in the string
     - e.g. "wpe4" -> "wpe4bpe6"

 - output:
   - neural net which outputs most probable chess move from training set

### sampling

 - input:
   - chess string

 - system:
   - inference from neural net

 - output:
   - most probable move from training set

potential problems i see so far:
 - if we are doing char prediction, it could output some illegal move
   - if this is the case, we could just run the computation again, until a valid move is generated
   - this problem could be lessened with token prediction instead of char prediction
   - but doesnt remove the problem outright


## notes

i could introduce some RL finetuning to respond to 'strongest' moves
  - i could also just train directly on some dataset which encodes strongest moves
    - perhaps some synthetic data from a bot, which always plays the strongest moves

shoutout joey diaz


## installation

clone repo, enter directory, and install requirements with:
```
pip install -r requirements.txt
```

