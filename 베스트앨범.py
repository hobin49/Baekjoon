from collections import Counter, defaultdict
def solution(genres, plays):
    #Counter 함수를 사용
    genre_counter = Counter()
    #defaultdict는 딕셔너리를 만드는 dict클래스의 서브클래스이다. 인자로 주어진 객체의 기본값을 딕셔너리의 초기값(0)으로 담을 수 있다.
    play_counter = defaultdict(Counter)
    #enumerate 함수를 사용해서 인덱스와, 요소를 동시에 접근, genres의 값들도 인덱스로 접근 가능하다
    for i, play in enumerate(plays):
        #classic, pop, classic, classic, pop
        genre = genres[i]
        #Counter({'pop': 3100, 'classic': 1450})
        genre_counter[genre] += play
        #이따 우리가 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하기 위한 작업으로 value가 높은 순으로 정렬되어있다. 
        #{'classic': Counter({3: 800, 0: 500, 2: 150}), 'pop': Counter({4: 2500 , 1: 600})})
        play_counter[genre][i] = play
    
    #정답을 넣을 값
    result = []    

    #most_common는 많이 나타난 것을 반환한다.
    #pop 3100, classic 1450
    for gnr, playing in genre_counter.most_common():
        #장르별로 가장 많이 재생된 노래를 두 개씩 모아 앨범을 출시하기 위해서 pop에서 2개 classic 2개를 뽑아서
        for idx, album in play_counter[gnr].most_common(2):
            #리스트에 그 값들 넣어주고 
            result.append(i)

    # 출력
    return result
    


