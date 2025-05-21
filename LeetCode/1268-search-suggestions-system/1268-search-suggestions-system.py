from collections import defaultdict
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        dic = defaultdict(list)
        for product in products:
            x = ''
            for p in product:
                x += p
                dic[x].append(product)
        
        answer = []
        x = ''
        for c in searchWord:
            x += c
            candid = list(dic[x])
            answer.append(candid[:3])
        return answer