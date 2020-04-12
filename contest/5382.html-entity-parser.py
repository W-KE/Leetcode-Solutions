class Solution:
    def entityParser(self, text: str) -> str:
        output = text
        output = output.replace("&quot;", "\"")
        output = output.replace("&apos;", "'")
        output = output.replace("&amp;", "&")
        output = output.replace("&gt;", ">")
        output = output.replace("&lt;", "<")
        output = output.replace("&frasl;", "/")
        return output


s = Solution()
print(s.entityParser(text="&amp; is an HTML entity but &ambassador; is not."))
print(s.entityParser(text="and I quote: &quot;...&quot;"))
print(s.entityParser(text="Stay home! Practice on Leetcode :)"))
print(s.entityParser(text="x &gt; y &amp;&amp; x &lt; y is always false"))
print(s.entityParser(text="leetcode.com&frasl;problemset&frasl;all"))
