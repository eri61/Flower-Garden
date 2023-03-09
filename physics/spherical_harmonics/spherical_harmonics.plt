ii = {0,1}          # 虚数単位 i を定義
set parametric      # 媒介変数表示を用いる
set urange [0:pi]   # 媒介変数u (=θ) の描画範囲
set vrange [0:2*pi] # 媒介変数v (=φ) の描画範囲
set isosample 20    # 描画する時の細かさ，数字が大きい程細かい
set ticslevel 0     # 3dプロット時にz軸が浮き上がらないようにする
set view equal xyz  # 3dプロット時に画像の縦横比が均一に見えるよう調整

# 表面を色付けする場合は以下を設定する
set pm3d            # 3dプロットで表面を色付け
set pm3d depthorder # 3dプロット時の陰影処理
unset sur           # 表面の線を消す
set view 50,50      # surface plotの視点設定

# colormap変更
# 水色～緑～赤へと変化する色づけを設定する
set palette model RGB
set palette file "-"
1 0.8 0.8
1 0 0
0 1 0
0 0 1
0 1 1
e

set xlabel "x"; set ylabel "y"; set zlabel "z"

## 描画する球面調和関数を定義
#Y(u,v) = -sqrt(3.0/(8*pi)) * sin(u) * exp(ii * v)  #Ylm = Y_11
Y(u,v) = sqrt(3.0/(4*pi)) * cos(u)  #Ylm = Y_10

# 描画用のx, y, z関数を定義
fx(u,v) = sin(u) * cos(v) * abs(Y(u,v))
fy(u,v) = sin(u) * sin(v) * abs(Y(u,v))
fz(u,v) = cos(u) * abs(Y(u,v))

# 画面に描画
splot fx(u,v), fy(u,v), fz(u,v)

# 画像をファイル出力
set term postscript color enhanced
set output "Y10.eps"
splot fx(u,v), fy(u,v), fz(u,v)

# Y_11を定義
Y(u,v) = -sqrt(3.0/(8*pi)) * sin(u) * exp(ii * v)  #Ylm = Y_11
fx(u,v) = sin(u) * cos(v) * abs(Y(u,v))
fy(u,v) = sin(u) * sin(v) * abs(Y(u,v))
fz(u,v) = cos(u) * abs(Y(u,v))

set output "Y11.eps"
# 画像をファイル出力
splot fx(u,v), fy(u,v), fz(u,v)
