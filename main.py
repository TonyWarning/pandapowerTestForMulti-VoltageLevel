import pandapower as pd
import pandapower.networks as pn

if __name__ == '__main__':
    net = pn.case9241pegase()

    pd.runpp(net)

    print(net.res_bus)


