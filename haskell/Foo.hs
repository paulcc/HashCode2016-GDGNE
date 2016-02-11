import Data.Array

main :: IO ()
main = run >>= print

run :: IO (Params, Int, [Int])
run =
  do f <- lines <$> readFile "../mother_of_all_warehouses.in"
     let
         (params':numprodtypes':weights':f1) = f
         [a,b,c,d,e] = read <$> words params' :: [Int]
         params = Params a b c d e
         numProdTypes = read numprodtypes' :: Int
         weights = read <$> words weights' :: [Int] -- assert lenght w == numP
     return (params, numProdTypes, weights)


lb, ub :: Int
lb = 0
ub = 9

data Params = Params
  { numRows :: Int -- 1 to 10,000
  , numCols :: Int -- 1 to 10,000
  , numDrones :: Int -- 1 to 1000
  , deadline :: Int -- 1 to 1,000,000
  , maxLoad :: Int -- 1 to 10,000
  } deriving (Show)

grid :: Array Int Cell
grid =
  listArray (lb, ub) (repeat emptyCell)

data Cell = Cell
  { cellWare :: Maybe Warehouse
  } deriving (Show)

emptyCell :: Cell
emptyCell = Cell Nothing

data Warehouse = Warehouse
 { wareId :: Int
 } deriving (Show)
