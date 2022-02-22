htmlSource = """

    paste source here
  
  """

import webbrowser
  
counter = htmlSource.count('magnet:')

indexStart = 0
i = 1

while i <= counter:
    
    indexStart = htmlSource.find("magnet:", indexStart + 1)
    indexEnd = htmlSource.find('"', indexStart)
    url = htmlSource[indexStart:indexEnd]
    webbrowser.open(url, new=0, autoraise=True)
    print(url)

    i += 1
