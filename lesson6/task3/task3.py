from lesson6.task3.Position import Position

admin_position = Position("Super", "User", "admin", {"wage": 200000, "bonus": 300000})

print(admin_position.get_full_name())
print(admin_position.get_total_income())
print(vars(admin_position))
