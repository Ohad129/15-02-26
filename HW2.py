_id = []
voting_tries = 0

while True:
    _id.append(input("enter ID of voter "))
    voting_tries += 1
    if _id[-1] == '999':
        voting_tries -= 1
        _id.remove('999')
        break
voters = set(_id)
print(voters)
invalid_voters = set()
for x in _id:
    if _id.count(x) > 1:
        invalid_voters.add(x)

print(invalid_voters)
voters -= invalid_voters
print(f"the valid voters are: {voters}, the invalid ones are: {invalid_voters}, and people tried to vote {voting_tries} times")