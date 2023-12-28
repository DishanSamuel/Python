import prettytable

table = prettytable.PrettyTable()

table.add_column("pokemon name",["pik","squ","char"])
table.add_column("type",["electric","water","fire",])
table.align = "l"

print(table)