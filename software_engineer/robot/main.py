from software_engineer.robot import robot

if __name__ == '__main__':
    pos, heading = robot.exec_command(input())
    heading_text = {
        0: "North",
        90: "East",
        180: "South",
        270: "West",
    }
    print(f"X: {pos[0]} Y: {pos[1]} Direction: {heading_text[heading]}")
