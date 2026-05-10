import sys

def get_normal_form(s):
    # 文字列を限界まで短くした「正規形」を取得する関数
    votqi = []
    for char in s:
        votqi.append(char)
        
        # スタックの末尾が ')' で、かつ要素が4つ以上あるか確認
        if char == ')' and len(votqi) >= 4:
            # 末尾の4文字が '(xx)' になっているか判定
            if votqi[-4] == '(' and votqi[-3] == 'x' and votqi[-2] == 'x':
                # '(xx)' を取り出す
                for _ in range(4):
                    votqi.pop()
                # 代わりに 'xx' を入れる
                votqi.append('x')
                votqi.append('x')
                
    # スタックに残った文字を結合して返す
    return "".join(votqi)

def solve():
    # 入力を一括で読み込む（高速化）
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    ans = []
    
    idx = 1
    for _ in range(T):
        A = input_data[idx]
        B = input_data[idx+1]
        idx += 2
        
        # 両方の文字列を限界まで短くして比較する
        if get_normal_form(A) == get_normal_form(B):
            ans.append("Yes")
        else:
            ans.append("No")
            
    # まとめて出力
    print("\n".join(ans))

if __name__ == '__main__':
    solve()