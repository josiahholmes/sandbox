# Find common dictionary items

def find_commons(data):
    d1 = data[0]
    commons = set(d1.items())

    for d in data[1:]:
        commons &= set(d.items())
    commons = dict(commons)

    return commons

data = [
    {
        'id': 101,
        'status': 'active',
        'role': 'user',
        'is_verified': True,
        'last_login': '2025-11-14'
    },
    {
        'id': 102,
        'status': 'active',
        'role': 'user',
        'is_verified': True,
        'department': 'engineering' # Extra key
    },
    {
        'id': 103,
        'status': 'active',
        'role': 'admin',             # Different value for 'role'
        'is_verified': True,
        'last_login': '2025-11-13'  # Different value for 'last_login'
    },
    {
        'id': 104,
        'status': 'inactive',        # Different value for 'status'
        'role': 'user',
        'is_verified': True,
        'department': 'sales'       # Extra key
    }
]

commons = find_commons(data)
print(f"Common Items: {commons}")