from rich.console import Console
from rich.table import Table


def display(departure, buses):     
    table = Table(title="Buses")
    table.add_column("Time", style="magenta")
    for bus in buses:
        if bus == "x":
            continue
        table.add_column("Bus {}".format(bus), style="green")
   
    wait = 50
    for i in range(departure, departure+wait):
        bus_row = []
        for bus in buses:   
            if bus == "x":
                continue
            line = "D" if i % int(bus) == 0 else "."
            bus_row.append("[bold]{}".format(line) if i == departure or i == (departure + (len(buses) - 1)) else line )

        time = "[bold]{}".format(str(i)) if i == departure or i == (departure + (len(buses) - 1)) else str(i)
        table.add_row(time, *bus_row)
    console = Console()
    console.print(table)

def display_tstp(buses, start, end):
    table = Table(title="Buses")
    table.add_column("Time", style="magenta")
    for bus in buses:
        if bus == "x":
            continue
        table.add_column("Bus {}".format(bus), style="green")
    
    for i in range(start, end):
        bus_row = []
        for bus in buses:   
            if bus == "x":
                continue
            line = str(i) if i % int(bus) == 0 else "."
            bus_row.append(line)            
        table.add_row(str(i), *bus_row)        

    console = Console()
    console.print(table)
