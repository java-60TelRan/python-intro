from sortedcontainers import SortedKeyList
# used for lists/arrays with  frequent add/remove operaions

# method add has complexity O[LogN]
sortedList: SortedKeyList[str] = SortedKeyList(key=str.casefold) # case insensitive comparing
sortedList.add("AbCd")
sortedList.add("aBc")
sortedList.add("abcd")
sortedList.add("ac")


print(sortedList) # aBc, AbCd, abcd, ac
    