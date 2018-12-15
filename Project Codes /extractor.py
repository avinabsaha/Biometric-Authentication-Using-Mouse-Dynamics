import time
import numpy as np
import math

def features(n,location):
    def find_theta_sum(dtheta_t):
        theta_sum = 0
        for dtheta in dtheta_t:
            theta_sum += dtheta
        return theta_sum

    def fit_theta(dtheta):
        if not (-(math.pi) < dtheta < math.pi):
            if dtheta < -(math.pi):
                p = 1
                while not -(math.pi) < dtheta:
                    term = 2 * p * math.pi
                    dtheta = dtheta + term
                    p += 1
            if dtheta > math.pi:
                q = 1
                while not dtheta > math.pi:
                    term = 2 * -1 * q * math.pi
                    dtheta = dtheta + term
                    q += 1
        return dtheta

    i = 1
    x = [0]
    y = [0]
    same_xy = 0
    time_instant = []
    dtime = []
    s = []
    vx = []
    vy = []
    v = []
    vdot = []
    vdd = []
    theta_t = []
    dtheta_t = [0]
    theta = []
    c = []
    delta_c = [0]
    w = []
    strokes = []
    time = 0
    dtimei = 0
    si = 0
    vxi = 0
    vyi = 0
    vi = 0
    vdoti = 0
    vddi = 0
    theta_ti = 0
    thetai = 0
    dtheta_ti = 0
    ci = 0
    delta_ci = 0
    wi = 0
    MC_count = 0
    distance = 0
    path_length = 0
    while i < n+1:
        #time.sleep(10)
        name = location+str(i) + '.txt'
        file = open(name, 'r')
        lines = file.readlines()
        startfrom = 7
        j = 0
        for line in lines:
            if j > 6:
                values = line.split(',')
                if values[0] == 'MM':
                    if int(values[3]) != 0:
                        if int(values[1]) != x[-1] or int(values[2]) != y[-1]:
                            x.append(int(values[1]))
                            y.append(int(values[2]))
                            delay = int(values[3])
                            time += delay
                            time_instant.append(time)
                            if len(x) > 2:
                                a = x[-1] - x[-2]
                                b = y[-1] - y[-2]
                                distance = math.sqrt(pow(a,2)+pow(b,2))
                                s.append(distance)
                                if a == 0:
                                    theta_ti = math.pi/2
                                else:
                                    theta_ti = np.arctan(b/a)
                                path_length += distance
                                theta_t.append(theta_ti)
                                delta_t = time_instant[-1] - time_instant[-2]
                                vxi = a/delta_t
                                vyi = b/delta_t
                                vi = math.sqrt(pow(vxi,2)+pow(vyi,2))
                                vx.append(vxi)
                                vy.append(vyi)
                                v.append(vi)
                                theta_sum = find_theta_sum(dtheta_t)
                                thetai = theta_t[0] + theta_sum
                                theta.append(thetai)
                            if len(time_instant) > 1:
                                dtimei = time_instant[-1] - time_instant[-2]
                                dtime.append(dtimei)
                            if len(theta) > 1:
                                ci = (theta[-1] - theta[-2])/distance
                                c.append(ci)
                                wi = (theta[-1] - theta[-2])/delta_t
                                w.append(wi)
                            if len(theta_t) > 1:
                                dtheta_ti = theta_t[-1] - theta_t[-2]
                                dtheta_ti = fit_theta(dtheta_ti)
                                dtheta_t.append(dtheta_ti)
                            if len(c) > 1:
                                delta_ci = c[-1] - c[-2]
                                delta_c.append(delta_ci)
                            if len(v) > 1:
                                dv = v[-1] - v[-2]
                                vdoti = dv/delta_t
                                vdot.append(vdoti)
                            if len(vdot) > 1:
                                dvdot = vdot[-1] - vdot[-2]
                                vddi = dvdot/delta_t
                                vdd.append(vddi)
                            #print(x, y, time_instant, vxi, vyi, vi, vdoti, vddi, distance, theta_ti)
                if values[0] == 'MC':
                    MC_count += 1
                if MC_count == 1:
                    x = [0]
                    y = [0]
                    time_instant = []
                    vx = []
                    vy = []
                    v = []
                    vdot = []
                    vdd = []
                    theta_t = []
                    dtheta_t = [0]
                    theta = []
                    c = []
                    delta_c = [0]
                    w = []
                if values[0] == 'MC' and len(vdd) > 2 and MC_count != 1:
                    delay = int(values[2])
                    time += delay
                    x = x[1:]
                    x_mean = np.mean(x)
                    x_std = np.std(x)
                    x_min = min(x)
                    x_max = max(x)
                    x_diff = max(x) - min(x)
                    #print('%.2f \t %.2f \t %.2f \t %.2f \t %.2f' %(x_mean, x_std, x_min, x_max, x_diff))
                    y = y[1:]
                    y_mean = np.mean(y)
                    y_std = np.std(y)
                    y_min = min(y)
                    y_max = max(y)
                    y_diff = max(y) - min(y)
                    #print('%.2f \t %.2f \t %.2f \t %.2f \t %.2f' %(y_mean, y_std, y_min, y_max, y_diff))
                    vx_mean = np.mean(vx)
                    vx_std = np.std(vx)
                    vx_min = min(vx)
                    vx_max = max(vx)
                    vx_diff = max(vx) - min(vx)
                    #print('%.2f \t %.2f \t %.2f \t %.2f \t %.2f' %(vx_mean, vx_std, vx_min, vx_max, vx_diff))
                    vy_mean = np.mean(vy)
                    vy_std = np.std(vy)
                    vy_min = min(vy)
                    vy_max = max(vy)
                    vy_diff = max(vy) - min(vy)
                    #print('%.2f \t %.2f \t %.2f \t %.2f \t %.2f' %(vy_mean, vy_std, vy_min, vy_max, vy_diff))
                    v_mean = np.mean(v)
                    v_std = np.std(v)
                    v_min = min(v)
                    v_max = max(v)
                    v_diff = max(v) - min(v)
                    #print('%.2f \t %.2f \t %.2f \t %.2f \t %.2f' %(v_mean, v_std, v_min, v_max, v_diff))
                    vdot_mean = np.mean(vdot)
                    vdot_std = np.std(vdot)
                    vdot_min = min(vdot)
                    vdot_max = max(vdot)
                    vdot_diff = max(vdot) - min(vdot)
                    #print('%.2f \t %.2f \t %.2f \t %.2f \t %.2f' %(vdot_mean, vdot_std, vdot_min, vdot_max, vdot_diff))
                    vdd_mean = np.mean(vdd)
                    vdd_std = np.std(vdd)
                    vdd_min = min(vdd)
                    vdd_max = max(vdd)
                    vdd_diff = max(vdd) - min(vdd)
                    #print('%.2f \t %.2f \t %.2f \t %.2f \t %.2f' %(vdd_mean, vdd_std, vdd_min, vdd_max, vdd_diff))
                    theta_mean = np.mean(theta)
                    theta_std = np.std(theta)
                    theta_min = min(theta)
                    theta_max = max(theta)
                    theta_diff = max(theta) - min(theta)
                    #print('%.3f \t %.3f \t %.3f \t %.3f \t %.3f' %(theta_mean, theta_std, theta_min, theta_max, theta_diff))
                    c_mean = np.mean(c)
                    c_std = np.std(c)
                    c_min = min(c)
                    c_max = max(c)
                    c_diff = max(c) - min(c)
                    #print('%.3f \t %.3f \t %.3f \t %.3f \t %.3f' %(c_mean, c_std, c_min, c_max, c_diff))
                    delta_c_mean = np.mean(delta_c)
                    delta_c_std = np.std(delta_c)
                    delta_c_min = min(delta_c)
                    delta_c_max = max(delta_c)
                    delta_c_diff = max(delta_c) - min(delta_c)
                    #print('%.3f \t %.3f \t %.3f \t %.3f \t %.3f' %(delta_c_mean, delta_c_std, delta_c_min, delta_c_max, delta_c_diff))
                    w_mean = np.mean(w)
                    w_std = np.std(w)
                    w_min = min(w)
                    w_max = max(w)
                    w_diff = max(w) - min(w)
                    #print('%.3f \t %.3f \t %.3f \t %.3f \t %.3f' %(w_mean, w_std, w_min, w_max, w_diff))
                    critical_count = 0
                    for index, value in enumerate(delta_c):
                        if value == 0 or abs(c[index]) > math.pi/10:
                            critical_count += 1
                    t = time - time_instant[0]
                    l = path_length
                    click_time = time - time_instant[-1]
                    pause_count = 0
                    for value in dtime:
                        if value > 100:
                            pause_count += 1
                    total_pause_time = sum(dtime)
                    pause_time_ratio = total_pause_time/t
                    label = 1
                    #strokes_limit = 500
                    #if len(strokes)-label*strokes_limit == 0:
                        #label += 1
                    x = [0]
                    y = [0]
                    time_instant = []
                    vx = []
                    vy = []
                    v = []
                    vdot = []
                    vdd = []
                    theta_t = []
                    dtheta_t = [0]
                    theta = []
                    c = []
                    delta_c = [0]
                    w = []
                    path_length = 0
                    stroke = [x_mean, x_std, x_min, x_max, x_diff,
                              y_mean, y_std, y_min, y_max, y_diff,
                              vx_mean, vx_std, vx_min, vx_max, vx_diff,
                              vy_mean, vy_std, vy_min, vy_max, vy_diff,
                              v_mean, v_std, v_min, v_max, v_diff,
                              vdot_mean, vdot_std, vdot_min, vdot_max, vdot_diff,
                              vdd_mean, vdd_std, vdd_min, vdd_max, vdd_diff,
                              theta_mean, theta_std, theta_min, theta_max, theta_diff,
                              c_mean, c_std, c_min, c_max, c_diff,
                              delta_c_mean, delta_c_std, delta_c_min, delta_c_max, delta_c_diff,
                              w_mean, w_std, w_min, w_max, w_diff,
                              t, l, critical_count, click_time, pause_count,
                              total_pause_time, pause_time_ratio, label]
                    strokes.append(stroke)
                    #print(stroke)
            j += 1
        #print('File Completed - ' + str(i))
        i += 1

    feature = np.array(strokes)
    return feature





