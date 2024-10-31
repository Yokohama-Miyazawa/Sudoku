# Sudoku

与えられた数独の盤面(9x9)について、[MiniSAT](http://minisat.se) を用いて求解する  
MiniSAT は自分でコンパイルした物を README.md と同じディレクトリに配置すること  
Mac の Homebrew で入る cryptominisat はオプションの書き方と出力結果の形式が異なるので、そのままでは動かない  
cryptominisat を使う際は`-cm5`, `--cryptominisat5`オプション(後述)を使用すること

## 構成物

- solve_sudoku.py 数独を解くプログラム
- boards 数独の初期盤面ファイル(.txt)の例が入ったディレクトリ

## 初期盤面の書き方

埋まっているマスはその値を、空のマスは-1 を書く  
詳細は boards ディレクトリの例を参照すること

## 使い方

### 初期盤面

初期盤面へのパスをコマンドライン引数で与える

求解する初期盤面が`./boards/board.txt`の場合

```
python3 solve_sudoku.py ./boards/board.txt
```

### オプション

#### `-cm5`, `--cryptominisat5`

SAT ソルバに cryptominisat5 を使用する

```
python3 solve_sudoku.py -cm5 ./boards/board.txt
```

実行後、以下のファイルが生成される

- result.txt 答えの盤面
- sudoku.cnf MiniSAT および cryptominisat5 に入力される DIMACS CNF
- output.txt (MiniSAT を使う場合のみ) MiniSAT の出力結果
