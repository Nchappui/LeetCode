class Solution:
    def simplifyPath(self, path: str) -> str:
        currentDirectory = []
        currentString = ""
        ans = ""
        for i in range(1, len(path)):
            if path[i] == '/':
                match currentString:
                    case "":
                        continue
                    case ".":
                        pass
                    case "..":
                        if len(currentDirectory)>0:
                            currentDirectory.pop()
                    case _:
                        currentDirectory.append(currentString)
                        
                currentString = ""
            else:
                currentString += path[i]
        if currentString != "":
            if currentString == "..":
                if len(currentDirectory)>0:
                    currentDirectory.pop()
            elif currentString == ".":
                pass
            else:
                currentDirectory.append(currentString)
        
        for elem in currentDirectory:
            ans+="/"+elem
        if ans == "" : ans += "/"
        return ans

    
Solution().simplifyPath("/home//foo/")
Solution().simplifyPath("/.../a/../b/c/../d/./")
