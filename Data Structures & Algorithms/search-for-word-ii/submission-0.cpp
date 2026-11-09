class TrieNode{
public:
    unordered_map<char, TrieNode*> children;
    string word;

    TrieNode() : word("") {}
};

class Solution {

private:
    vector<vector<char>> _board;
    vector<string> _result;

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // 1. construct trie
        TrieNode* root = new TrieNode();
        for(string& word : words){
            TrieNode* node = root;
            for(char letter : word){
                if(node->children.find(letter) != node->children.end()){
                    node = node->children[letter];
                }else {
                    TrieNode* newNode = new TrieNode();
                    node->children[letter] = newNode;
                    node = newNode;
                }
            }
            node->word = word;
        }
        this->_board = board;

        for(int row = 0; row < board.size(); row++){
            for(int col = 0; col < board[0].size(); col++){
                if(root->children.find(board[row][col]) != root->children.end()){
                    backtrack(row, col, root);
                }
            }
        }
        return this->_result;
    }

    void backtrack(int row, int col, TrieNode* parent) {
        char letter = this->_board[row][col];
        TrieNode* node = parent->children[letter];
        if(node->word != ""){
            this->_result.push_back(node->word);
            node->word = "";
        }

        int d_row[] = {-1, 0, 1, 0};
        int d_col[] = {0, 1, 0, -1};
        this->_board[row][col] = '#';
        for(int i = 0; i < 4; i++){
            int nr = row + d_row[i];
            int nc = col + d_col[i];
            if(nr < 0 || nr >= this->_board.size() || nc < 0 || nc >= this->_board[0].size()){
                continue;
            }
            if(node->children.find(this->_board[nr][nc]) != node->children.end()){
                backtrack(nr, nc, node);
            }
        }
        this->_board[row][col] = letter;
    }
};