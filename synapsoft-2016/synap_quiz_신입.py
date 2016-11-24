class Graph:
    
    def __init__(self):
        # adj_list means adjacent list
        self.adj_list = {}
        self.already_seen = {}
    
    
    def addLink(self, link):
        if self.isAlreadySeen(link): return
        # link between A and B
        (A, B) = link
        if not A in self.adj_list:
            self.adj_list[A] = []
        if not B in self.adj_list:
            self.adj_list[B] = []
        
        self.adj_list[A].append(B)
        self.adj_list[B].append(A)
        
        
    # function for preventing for replica link, (A, B) = (B, A)
    def isAlreadySeen(self, link):
        (A, B) = link
        if A > B: link.reverse()
        hash_key = ' '.join(link)
        
        if hash_key in self.already_seen:
            return True
        self.already_seen[hash_key] = True
        return False
    
    
    def printFriends(self, name):
        if name not in self.adj_list: return
        print(' '.join(self.adj_list[name]))
        
        
    def printRecommendedFriends(self, name):
        if name not in self.adj_list: return
        friends = self.adj_list[name]
        recommend = set()
        for friend in friends:
            recommend = recommend | set(self.adj_list[friend])
        # except me and my friend from recommend
        recommend = recommend - set(friends)
        recommend = recommend - set([name])
        print(' '.join(recommend))
        
        
        
def main():
    # construct graph from textfile
    graph = Graph()
    fd = open('sns-friends.txt', 'r')
    line = fd.readline()
    while line:
        link = line.split()
        graph.addLink(link)
        line = fd.readline()
    
    print('== 사용자 이름을 입력 해주세요. (프로그램 종료 시 q! 입력) ==')
    name = input()
    while name != 'q!':
        print('= 내 친구 목록 =')
        graph.printFriends(name)
        print('= 내 친구의 친구 목록 =')
        graph.printRecommendedFriends(name)
        print()
        name = input()
        
main()