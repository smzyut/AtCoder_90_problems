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
    
    
import sys

# 入力を一括取得
input_data = sys.stdin.read().split()
if not input_data:
    exit()

T = int(input_data[0])
idx = 1
ans = []

for _ in range(T):
    s_target = input_data[idx]
    idx += 1
    
    # 正規化処理をループ内で直接実行（またはスタック管理）
    stack = []
    for char in s_target:
        stack.append(char)
        # 末尾が '(xx)' になった瞬間に 'xx' へ置換
        if char == ')' and len(stack) >= 4:
            if stack[-4] == '(' and stack[-3] == 'x' and stack[-2] == 'x':
                # 4文字消して 'xx' を追加
                for _ in range(4):
                    stack.pop()
                stack.append('x')
                stack.append('x')
    
    # 比較対象の処理（2つ目の文字列）
    s_target_2 = input_data[idx]
    idx += 1
    
    stack_2 = []
    for char in s_target_2:
        stack_2.append(char)
        if char == ')' and len(stack_2) >= 4:
            if stack_2[-4] == '(' and stack_2[-3] == 'x' and stack_2[-2] == 'x':
                for _ in range(4):
                    stack_2.pop()
                stack_2.append('x')
                stack_2.append('x')
    
    if "".join(stack) == "".join(stack_2):
        ans.append("Yes")
    else:
        ans.append("No")

# まとめて出力
print('\n'.join(ans))