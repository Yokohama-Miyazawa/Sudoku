# Sudoku  
与えられた数独の盤面(9x9)について、MiniSATを用いて求解する  
MiniSATは自分でコンパイルした物をREADME.mdと同じディレクトリに配置すること  
MacのHomebrewで入るcryptominisatはオプションの書き方と出力結果の形式が異なるので、そのままでは動かない  
cryptominisatを使う際は`solve_sudoku.py`を修正すること  

## 構成物  
- solve_sudoku.py 数独を解くプログラム
- boards 数独の初期盤面ファイル(.txt)の例が入ったディレクトリ

## 初期盤面の書き方  
埋まっているマスはその値を、空のマスは-1を書く  
詳細はboardsディレクトリの例を参照すること  

## 使い方  
求解する初期盤面が`./boards/board.txt`の場合  
`python3 solve_sudoku.py ./boards/board.txt`  

実行後、以下の3つのファイルが生成される
- result.txt 答えの盤面
- sudoku.cnf MiniSATに入力されるDIMACS CNF
- output.txt MiniSATの出力結果
