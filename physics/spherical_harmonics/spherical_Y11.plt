# 波動関数の正負を青赤で表す
ii = {0,1}          # 虚数単位 i を定義
set parametric      # 媒介変数表示を用いる
set urange [0:pi]   # 媒介変数u (=θ) の描画範囲
set vrange [0:2*pi] # 媒介変数v (=φ) の描画範囲
set isosample 40    # 描画する時の細かさ，数字が大きい程細かい
set ticslevel 0     # 3dプロット時にz軸が浮き上がらないようにする
set view equal xyz  # 3dプロット時に画像の縦横比が均一に見えるよう調整
#set depthorder
set hidden3d

set xtics 0.5
set ytics 0.5
set ztics 0.2

set view 70,120      # surface plotの視点設定

set xlabel "x"; set ylabel "y"; set zlabel "z"

# 描画用のx, y, z関数を定義
fx(u,v) = sin(u) * cos(v)
fy(u,v) = sin(u) * sin(v)
fz(u,v) = cos(u)

set term postscript color enhanced

## 描画する球面調和関数を定義
Y(u,v) = sqrt(3.0/(4*pi)) * cos(u)  #Ylm = Y_10

realY(u,v) = sqrt(2) * real(Y(u,v)) 
# C言語の二項演算子と同じ演算子が使える
# realY(u,v) が負だったらゼロ，正だったら realY を返す
posp(u,v) = realY(u,v) < 0 ? 0 : realY(u,v)
# realY(u,v) が正だったらゼロ，負だったら realY を返す
negp(u,v) = realY(u,v) > 0 ? 0 : -realY(u,v)

set output "pxpypz.eps"
# 描画
set multiplot layout 1,3
splot posp(u,v)*fx(u,v), posp(u,v)*fy(u,v), posp(u,v)*fz(u,v) \
	      lc rgb "blue" ti "p_z>0", \
      negp(u,v)*fx(u,v), negp(u,v)*fy(u,v), negp(u,v)*fz(u,v) \
			  lc rgb "red" ti "p_z<0"

px(u,v) = sqrt(3.0/(4*pi)) * sin(u) * cos(v)  # px
posp(u,v) = px(u,v) < 0 ? 0 : px(u,v)
negp(u,v) = px(u,v) > 0 ? 0 : -px(u,v)
#set output "px.eps"
# 描画
splot posp(u,v)*fx(u,v), posp(u,v)*fy(u,v), posp(u,v)*fz(u,v) \
	      lc rgb "blue" ti "p_x>0", \
      negp(u,v)*fx(u,v), negp(u,v)*fy(u,v), negp(u,v)*fz(u,v) \
			  lc rgb "red" ti "p_x<0"

py(u,v) = sqrt(3.0/(4*pi)) * sin(u) * sin(v)  # py
posp(u,v) = py(u,v) < 0 ? 0 : py(u,v)
negp(u,v) = py(u,v) > 0 ? 0 : -py(u,v)
#set output "py.eps"
# 描画
splot posp(u,v)*fx(u,v), posp(u,v)*fy(u,v), posp(u,v)*fz(u,v) \
	      lc rgb "blue" ti "p_y>0", \
      negp(u,v)*fx(u,v), negp(u,v)*fy(u,v), negp(u,v)*fz(u,v) \
			  lc rgb "red" ti "p_y<0"
