class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def parse(expr, i):
            # returns (set_of_words, next_index)
            groups = [[]]  # list of lists (each inner list = one comma-separated term, holds sets to concatenate)

            while i < len(expr) and expr[i] != '}':
                if expr[i] == '{':
                    inner_set, i = parse(expr, i + 1)
                    groups[-1].append(inner_set)
                elif expr[i] == ',':
                    groups.append([])
                    i += 1
                else:
                    # lowercase letter(s) - read the full word
                    j = i
                    while j < len(expr) and expr[j].islower():
                        j += 1
                    groups[-1].append({expr[i:j]})
                    i = j

            # skip the closing '}'
            i += 1

            # union of concatenations across each comma-separated group
            result = set()
            for term in groups:
                # cartesian product / concatenation within a term
                current = {""}
                for s in term:
                    current = {a + b for a in current for b in s}
                result |= current

            return result, i

        result, _ = parse(expression, 0)
        return sorted(result)