class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] arr = new char[26];

            for (char c : s.toCharArray()) {
                arr[c - 'a']++;
            }

            String normalized = Arrays.toString(arr);

            map.computeIfAbsent(
                normalized, 
                k -> new ArrayList<String>()
            ).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
