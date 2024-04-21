# *Welcome! stackNqueue*
This packages includes *Stack.py*, *Queue.py*, *DoublyCircularLinkedList.py*
*Stack.py* and *Queue.py* inherit the **DoublyCircularLinkedList class** from *DoublyCircularLinkedList.py*

## **structure of packages**
![stackNqueue구조](https://github.com/dudasdaily/stackNqueue/assets/66531025/e5165028-ab00-49b1-b488-899d5a27f96b)

## **inital states**
![stackNqueue초기상태](https://github.com/dudasdaily/stackNqueue/assets/66531025/24080ce2-1e27-4000-8f0e-b3dfb68b50e1)


## **DoublyCircularLinkedList Methods**
|Method|works|
|------|-----|
|append(x)|리스트 끝에 x를 추가한다.|
|getNode(i: int)| i번째 인덱스의 노드를 반환한다.|
|printList()|리스트를 출력한다.|
|pop(i: int)|i번째 인덱스의 노드를 삭제하고 반환한다. 인자를 주지 않거나 -1을 줬을경우, 끝노드를 삭제하고 반환한다.|
|insert(i: int, x)|i번째 인덱스에 item으로 x를 가진 노드를 삽입한다.|

## **Stack Methods**
*Stack클래스는 DoublyCircularLinkedList클래스를 상속받는다*
|Method|works|
|------|-----|
|push(x)|x값을 가진 노드를 리스트 끝에 추가한다.|
|pop()|리스트의 끝 노드를 삭제하고 반환한다.|
|top()|리스트의 끝 노드를 반환한다|

## **Queue Methods**
*Queue클래스는 DoublyCircularLinkedList클래스를 상속받는다*
|Method|works|
|------|-----|
|enqueue(x)|x를 리스트의 첫번 째 front에 추가한다.|
|dequeue()|rear노드 즉, 리스트의 끝 노드를 삭제하고 반환한다.|
|rear()|첫번째로 추가된 리스트의 끝 노드 rear의 값을 반환한다.|
