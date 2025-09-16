import subprocess

def calculate_ea(xA, yA, vA, hA, lA, wA, xB, yB, vB, hB, lB, wB):
    """
    Call ea_tool.exe to compute the Evasive Acceleration (EA) value.

    Parameters
    ----------
    Road user A:
        xA, yA : float
            Absolute coordinates in meters.
        vA : float
            Speed in meters per second.
        hA : float
            Heading angle in radians, within [-pi, pi] (e.g. 1.57 is 90 degrees).
        lA : float
            Vehicle length in meters.
        wA : float
            Vehicle width in meters.

    Road user B:
        xB, yB : float
            Absolute coordinates in meters.
        vB : float
            Speed in meters per second.
        hB : float
            Heading angle in radians, within [-pi, pi].
        lB : float
            Vehicle length in meters.
        wB : float
            Vehicle width in meters.

    Returns
    -------
    float or None
        EA value if successfully computed, otherwise None.
    """
    command = [
        "ea_tool.exe",
        str(xA), str(yA), str(vA), str(hA),
        str(lA), str(wA), str(xB), str(yB),
        str(vB), str(hB), str(lB), str(wB)
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('gbk', errors='ignore')
    for line in output.splitlines():
        if 'EA =' in line:
            return float(line.split('=')[1].split()[0])
    return None


if __name__ == "__main__":
    # Example real-time parameters for Vehicle A (ego vehicle)
    # Absolute coordinates (m), speed (m/s), heading angle (rad), vehicle size (m)
    xA = 0.0       # x position
    yA = 0.0       # y position
    vA = 0.1       # speed
    hA = 0.0       # heading angle, [-pi, pi]
    lA = 10.0      # length
    wA = 2.5       # width

    # Example real-time parameters for Vehicle B (surrounding vehicle)
    xB = -2.0
    yB = 8.0
    vB = 5.0
    hB = -1.0
    lB = 4.8
    wB = 1.8

    ea_value = calculate_ea(xA, yA, vA, hA, lA, wA,
                            xB, yB, vB, hB, lB, wB)

    if ea_value is not None:
        print(f"EA = {ea_value}")
    else:
        print("Failed to compute EA value. Please check the input or ea_tool output.")
