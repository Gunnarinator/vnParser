module Main (main) where
  
import System.IO
import Tokens ( alexScanTokens )

main :: IO ()
main = do
  s <- readFile "../scripts/ch_1/basement_1/.rpy"
  print (alexScanTokens s)


-- 