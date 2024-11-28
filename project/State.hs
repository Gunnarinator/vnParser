module State (State, get, put, modify, runState, evalState, execState) where
import Control.Monad (ap, liftM, liftM2)

newtype State s a = S (s -> (a,s))

runState :: State s a -> (s -> (a,s)) 
runState (S f) = f 

instance Monad (State s) where
    -- return :: a -> State s a
    return :: a -> State s a
    return x = S (\s -> (x, s))

    -- (>>=)
    (>>=) :: State s a -> (a -> State s b) -> State s b
    st >>= f = S (\s -> let (x,s') = runState st s in runState (f x) s') 

instance Functor (State s) where
    -- fmap :: (a -> b) -> (State s a) -> (State s b)
    fmap :: (a -> b) -> State s a -> State s b
    fmap f st = S (\s -> 
        let (a,s') = runState st s in (f a, s')) 

instance Applicative (State s) where
    -- pure :: a -> State s a
    pure :: a -> State s a
    pure = return
    (<*>) :: State s (a -> b) -> State s a -> State s b
    -- (<*>) :: State s (a->b) -> State s a -> State s b
    (<*>) = ap

evalState :: State s a -> s -> a
evalState st s = fst (runState st s)

execState :: State s a -> s -> s
execState st s = snd (runState st s)

-- Since our notion of state is generic, it is useful to write get 
-- and put functions with which one can access and modify the state. 
-- We can easily get the current state via

get :: State s s
get = S $ \s -> (s, s)

-- That is, get denotes an action that leaves the state unchanged 
-- but returns the state itself as a value. Note that although get 
-- does not have a function type (unless you peek under the covers 
-- of State), we consider it a monadic "action".

-- Dually, to update the state to some new value s' we can write the function

put :: s -> State s ()
put s = S $ const ((),s)

modify :: (s -> s) -> State s ()
modify f = get >>= \s -> put (f s) -- do 
    -- s <- get 
    -- put (f s)

-- Modified from a lecture by Stephanie Weirich
