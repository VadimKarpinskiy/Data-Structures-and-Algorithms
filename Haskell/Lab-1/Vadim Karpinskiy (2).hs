-- ex8
isItTheAnswer :: String -> Bool
isItTheAnswer s =
    case s of
        "Love" -> True
        _      -> False

not' :: Bool -> Bool
not' b = case b of
    True  -> False
    False -> True

or' :: (Bool, Bool) -> Bool
or' (a, b) = 
    case a of
        True -> True
        False -> case b of
            True -> True
            False -> False

and' :: (Bool, Bool) -> Bool
and' (a, b) = 
    case a of
    False -> False
    True -> case b of
        True -> True
        False -> False

nand' :: (Bool, Bool) -> Bool
nand' (a, b) = 
    case a of
    True -> False
    False -> case b of
        False -> True
        True -> False

xor' :: (Bool, Bool) -> Bool
xor' (a,b) =
    case a of
        True -> case b of
            False -> True
            True -> False
        False -> case b of
            True -> True
            False -> False

-- ex9
unitVec2D :: (Double, Double) -> (Double, Double)
unitVec2D (a,b) = ( (a/l), (b/k) )
    where l = abs(a)
          k = abs(b) --komentarz! ^_^

-- ex10
unitVec2D :: (Double, Double) -> (Double, Double)
unitVec2D (a,b) = 
    let l = abs(a)
        k = abs(b)
    in ( (a/l), (b/k) )

-- ex11
roots :: (Double, Double, Double) -> (Double, Double)
roots (a, b, c) = ( (-b - d) / e, (-b + d) / e )
   where {
       d = sqrt (b * b - 4 * a * c);
       e = 2 * a ;
        }

--ex12
let f1 (x,y,z) = if x > y then x/z else y/z
:t f1

let f2 (a) = False
:t f2

let f3 (a,b,c,d) = (a > b) && (c > d)
:t f3

let f4 (z,x,c) = (z^x)^c
:t f4

let f5 (a,b) = a * b
:t f5

