class TrieNode:
    def __init__(self):
        self.children=[None]*26;
        self.word='';
class Trie:
    def __init__(self):
        self.root=TrieNode();
    def insert(self,key):
        currentNode=self.root;
        for c in key:
            if(currentNode.children[ord(c)-ord('a')] is None):
                currentNode.children[ord(c)-ord('a')]=TrieNode();

            currentNode=currentNode.children[ord(c)-ord('a')];
        currentNode.word=key;
    def delete(self,key):
        currentNode=self.root;
        for c in key:
            if(currentNode.children[ord(c)-ord('a')] is None):
                print('There is no such a word in Trie')
                return;
            currentNode=currentNode.children[ord(c)-ord('a')];
        currentNode.word='';
    def search(self,key):
        currentNode=self.root;
        for c in key:
            if(currentNode.children[ord(c)-ord('a')] is None):
                print('There is no such a word in Trie')
                return False;
            currentNode=currentNode.children[ord(c)-ord('a')];
        return currentNode.word is not '';
# Find all (english word) substrings of a given string . (every = every, ever, very)
def indexOfchar(c):
    return ord(c)-ord('a')

trie=Trie();
trie.insert('ev');
trie.insert('very');
trie.insert('evsal');
trie.insert('salam')
trie.insert('sa')
trie.insert('salamaleikom')
str='every'
currentNodes=[];
nextNodes=[];
nextNodes.append(trie.root)


for c in str:
    currentNodes=nextNodes;
    nextNodes=[];
    nextNodes.append(trie.root)
    for node in currentNodes:
        if(node.children[indexOfchar(c)] is not None):
            nextNodes.append(node.children[indexOfchar(c)])
            if(node.children[indexOfchar(c)].word is not ''):
                print(node.children[indexOfchar(c)].word)



# print(trie.search('salam'))
# print(trie.search('sa'))
# trie.delete('sa')
# print(trie.search('salam'))
# print(trie.search('sa'))
