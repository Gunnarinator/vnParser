module Utils where 
    import Data 
    import Control.Exception

    --checks whether two vars have the same type
    typeEq :: Var -> Var -> Bool 
    typeEq (IntVar _ _) (IntVar _ _) = True 
    typeEq (BoolVar _ _) (BoolVar _ _) = True 
    typeEq (StringVar _ _) (StringVar _ _) = True
    typeEq _ _ = False 

    --returns the name of a var
    varName :: Var -> String 
    varName v = case v of 
        (IntVar name _) -> name
        (BoolVar name _) -> name
        (StringVar name _) -> name 

    --returns the val of a var
    varVal :: Var -> Val 
    varVal v = case v of 
        (IntVar _ val) -> Int val
        (BoolVar _ val) -> Bool val
        (StringVar _ val) -> String val 

    --check if two vars have the same name
    nameEq :: Var -> Var -> Bool 
    nameEq x y = varName x == varName y

    
    --replaces the value of a var in the var environment
    setVar :: Var -> Val -> VarEnv -> VarEnv
    setVar x _ [] = throw (NotInEnv (varName x))
    setVar x val (v:vs) = 
        if nameEq x (fst v)
            then if typeEq x (fst v) 
                then (fst v, val):vs
                else throw (TypeMisMatch x (fst v))
            else v : setVar x val vs

    --returns True if the var is in the environment
    findVar :: Var -> VarEnv -> Bool
    findVar x [] = False
    findVar x vs = foldr ((||) . nameEq x . fst) False vs

    --add a var to the environment. If it's already there, just update the value.
    addVar :: Var -> Val -> VarEnv -> VarEnv
    addVar v val venv = 
        if not (findVar v venv)
            then (v, val) : venv 
            else setVar v val venv