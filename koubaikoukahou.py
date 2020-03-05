#勾配
def numerical_gradient(f,x):
    h = 1e-4 #0.0001
    grad = np.zerous_like(x)

    for index in range(x.size):
     tmp_val = x[idx]
     #f(x+h)の計算
     x[idx] = tmp_val+h
     fxh1 = f(x)
    
     #f(x-h)の計算
     x[idx] = tmp_val-h
     fxh2 = f(x)
    
     grad[idx] = (fxh1-fxh2)/(2*h)
     x[idx] = tmp_val  #値を元に戻す
    
    return grad

#勾配降下法
def gsradient_descent(f, init_x,lr=0.01,step_num=100):　　　#fは最適化したい関数、初期値、lrは学習率、step_numは繰り返しの数
    x = init_x　
    
    for i in numerical_gradient(f,x):
        x = lr*grad
        return x 