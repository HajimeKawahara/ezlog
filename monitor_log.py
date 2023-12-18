"""monitoring log generated by numpyro NUTS.

    in your shell 
    $ nohup python -u fit.py >& log & 
    $ python monitor_log.py log

"""


def count_steps(logfile):
    """count the number of the steps in numpyro/log.

    Args:
        log: log or steps.dat generated by (grep steps log > steps.dat)

    Returns:
        step array, comp time
    """
    import numpy as np

    step = []
    ctime = []
    f = open(logfile, "r")
    w = f.read().split("\n")
    for i in w:
        j = i.split(",")
        if len(j) == 3:
            try:
                istep = int(j[2].split("steps")[0])
                step.append(istep)
                itime = float(j[1].replace("s/it", "").replace("it/s", ""))
                ctime.append(itime)
            except:
                print("Some error when reading")
    f.close()
    step = np.array(step, dtype=int)

    return step, ctime


if __name__ == "__main__":
    import sys
    import terminalplot
    import numpy as np

    step, ctime = count_steps(sys.argv[1])
    if True:
        print("# STEP ############################################")
        terminalplot.plot(list(range(len(step))), list(step))
        print("# TIME (sec) ######################################")
        terminalplot.plot(list(range(len(ctime))), list(ctime))
        print("# TIME/STEP (sec) ############################################")
        terminalplot.plot(list(range(len(step))), list(ctime / step))

    print("# summary ######################################")
    print("Total steps:", np.sum(step))
    print("# of chain:", len(step))
    print("median/chain:", np.median(step), "|min-max", np.min(step), "-", np.max(step))
    print(
        "total time=",
        round(np.sum(ctime) / 3600, 3),
        "h / ",
        round(np.sum(ctime) / 60, 1),
        "min",
    )

