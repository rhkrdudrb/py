def solution(N, stages):
    answer = []
    stage2cnt = {}
    previous_clear= 0
    for i in range(len(stages),0,-1):
        if i <= N:
            # print(N-i+1,"번 스테이지 실패율",stages.count(N-i+1),"/",len(stages) - previous_clear)
            stage2cnt[N-i+1] = stages.count(N-i+1) / (len(stages) - previous_clear)
            previous_clear += stages.count(N-i+1)
    #내림차순 정렬
    for i in sorted(stage2cnt.items(), key=lambda x: x[1], reverse=True):
        answer.append(i[0])
    return  answer