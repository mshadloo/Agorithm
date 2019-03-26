arr = [-2, -3, 4, 0, -2, -1, 5, -3, 8]
m_all = 1
m_first = 1
m_last = 1
negative_No = 0
best = 0
for i in range(len(arr)):

     if(arr[i] == 0):
          if(negative_No % 2 == 0):
               if(m_all > best):
                    best = m_all
          else:
               if(max(m_all / (first_neg * m_first), m_all / (last_neg * m_last)) > best):
                    best = max(m_all / (first_neg * m_first), m_all / (last_neg * m_last))
          m_all = 1
          m_first = 1
          m_last = 1
          negative_No = 0
     else:
          m_last = m_last * arr[i]
          if(arr[i] < 0):
               negative_No = negative_No + 1
               if(negative_No == 1):
                    m_first = m_all
                    first_neg = arr[i]

               if (negative_No % 2 == 1):
                    last_neg = arr[i]
                    m_last = 1
          m_all = m_all * arr[i]
if(negative_No % 2 == 0):
     if(m_all > best):
          best = m_all
else:
     if(max(m_all / (first_neg * m_first), m_all / (last_neg * m_last)) > best):
          best = max(m_all / (first_neg * m_first), m_all / (last_neg * m_last))
print(best)
