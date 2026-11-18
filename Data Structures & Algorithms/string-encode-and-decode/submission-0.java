class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for(String s : strs){
            sb.append(Integer.toString(s.length()));
            sb.append("#");
            sb.append(s);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();   

        int p = 0; 
        while(p < str.length()){
            int lengthEnd = str.indexOf('#', p);
            int nextLength = Integer.parseInt(str.substring(p, lengthEnd));
            p = lengthEnd + 1 + nextLength;
            res.add(str.substring(lengthEnd + 1, p));
        }

        return res;
    }
}
