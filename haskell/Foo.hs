import Data.List.Split
import Data.Array
import qualified Data.Map as Map

main :: IO ()
main = run >>= print

-- run :: IO (Params, Int, [Int])
run =
  do f <- lines <$> readFile "../mother_of_all_warehouses.in"
     let
         (params':numprodtypes':weights':numWares':f1) = f
         [a,b,c,d,e] = read <$> words params' :: [Int]
         params = Params a b c d e
         numProdTypes = read numprodtypes' :: Int
         weights = read <$> words weights' :: [Int] -- assert lenght w == numP
         numWares = read numWares' :: Int
         (wares', f2) = splitAt (2*numWares) f1
         wares = map mkWare $ chunksOf 2 wares' :: [Warehouse]
         (numOrders':f3) = f2
         numOrders = read numOrders' :: Int
         (orders', f4) = splitAt (3*numOrders) f3
         orders = map mkOrder $ chunksOf 3 orders' :: [Order]

     return (params, numProdTypes, weights, wares, orders)

mkOrder :: [String] -> Order
mkOrder [coord', numItems', ptypes] =
  let [x, y] = read <$> words coord' :: [Int]
      numItems = read numItems' :: Int
      stock = read <$> words ptypes :: [Int]
  in
    Order (x, y) numItems stock

mkOrder _ = error "Bork! Expected thre length list"

data Order = Order
  { ordCoords :: (Int, Int)
  , ordNumItems :: Int
  , ordProdTypes :: [Int]
  } deriving (Show)

mkWare :: [String] -> Warehouse
mkWare [coord', prodFoo'] =
  let [x, y] = read <$> words coord' :: [Int]
      prodFoo = read <$> words prodFoo' :: [Int]
      stock = Map.fromAscList $ zip [0..] prodFoo
  in
    Warehouse 99 (x, y) stock
mkWare _ = error "Bork! Expected two length list"

data Params = Params
  { numRows :: Int -- 1 to 10,000
  , numCols :: Int -- 1 to 10,000
  , numDrones :: Int -- 1 to 1000
  , deadline :: Int -- 1 to 1,000,000
  , maxLoad :: Int -- 1 to 10,000
  } deriving (Show)

data Warehouse = Warehouse
 { wareId :: Int
 , wareCoord :: (Int, Int)
 , wareProdStock :: Map.Map Int Int -- prod stuff
 } deriving (Show)

-- lb, ub :: Int
-- lb = 0
-- ub = 9

-- grid :: Array Int Cell
-- grid =
--   listArray (lb, ub) (repeat emptyCell)

-- data Cell = Cell
--   { cellWare :: Maybe Warehouse
--   } deriving (Show)

-- emptyCell :: Cell
-- emptyCell = Cell Nothing
