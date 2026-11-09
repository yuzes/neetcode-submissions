class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> paren = {
             {')', '('},
             {']','['},
             {'}', '{'},
        };

        for(const auto& c : s){
            if(paren.find(c) != paren.end()){
                if(stk.empty()){
                    return false;
                }
                if(paren[c] != stk.top()){
                    return false;
                }
                stk.pop();
            }else{
                stk.push(c);
            }

        }
        return stk.empty();
    }
};
