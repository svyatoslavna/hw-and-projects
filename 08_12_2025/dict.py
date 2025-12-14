# 0 (три способа задать словарь)
users = {
    "alice2005": [20, "female", "London"],
    "rob_1": [43, "male", "Washington"],
    "m_kate": [33, "female", "Moscow"],
}

users = dict(
    alice2005=[20, "female", "London"],
    rob_1=[43, "male", "Washington"],
    m_kate=[33, "female", "Moscow"],
)

users = dict(
    [
        ("alice2005", [20, "female", "London"]),
        ("rob_1", [43, "male", "Washington"]),
        ("m_kate", [33, "female", "Moscow"]),
    ]
)


# 1
print(users["alice2005"])
print(users.get("rob_1"))
print(users.get("m_kate", "no such user"))
print(users.get("noname1", "no such user"))


# 2
users["xen1a01"] = [29, "female", "Pskov"] # добавляю
users["rob_1"] = [18, "male", "Los Angeles"] # измению

print(users)


# 3
banned_user = users.pop("alice2005")
del users["m_kate"]

print(users)
print(banned_user)