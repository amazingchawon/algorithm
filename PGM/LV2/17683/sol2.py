def check_length(notes):
    result = []
    idx = 0
    while idx < len(notes):
        if idx == len(notes) - 1 or notes[idx + 1] != '#':
            result.append(notes[idx])
            idx += 1
        else:
            result.append(notes[idx].lower())
            idx += 2

    return result


def solution(m, musicinfos):
    answer = ['(None)', 0]

    musics = []

    # STEP 0. m에 # 들어있다면 바꾸기
    tmp = []
    idx = 0
    while idx < len(m):
        if idx == len(m) - 1 or m[idx + 1] != '#':
            tmp.append(m[idx])
            idx += 1
        else:
            tmp.append(m[idx].lower())
            idx += 2
    m = ('').join(tmp)

    for musicinfo in musicinfos:
        # STEP 1. musicinfos에 들어있는 음악 길이 재기
        musicinfo = musicinfo.split(',')
        notes = check_length(musicinfo[-1])
        length = len(notes)

        # STEP 2. 재생시간 구하기
        start_hour, start_min = int(musicinfo[0][:2]), int(musicinfo[0][3:])
        end_hour, end_min = int(musicinfo[1][:2]), int(musicinfo[1][3:])
        play_time = (end_hour - start_hour) * 60 + end_min - start_min

        # STEP 3. 재생된 노래 악보 구하기
        tmp = play_time % length
        notes = notes * (play_time // length) + notes[0:tmp]
        notes = ('').join(notes)

        # STEP 4. 새로운 배열에 제목, 악보, 재생시간만 저장
        musics.append([musicinfo[2], notes, play_time])

    # STEP 5. 네오가 기억한 멜로디와 악보 비교
    for music in musics:
        if m in music[1] and music[2] > answer[1]:
            answer = [music[0], music[2]]

    return answer[0]