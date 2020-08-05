def solution(participant, completion):
    for val in completion:
        participant.pop(participant.index(val))
    print(participant)

participant = ["marina", "marina", "nikola", "vinko", "filipa"]
completion = ["marina", "filipa", "marina", "nikola"]
solution(participant,completion)