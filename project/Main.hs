module Main (main) where
  
import System.IO
import Tokens ( alexScanTokens )

main :: IO ()
main = do
  s <- readFile "singleScript.rpy"
  print (alexScanTokens s)