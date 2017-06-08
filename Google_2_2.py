def answer(x, y):
      arr = [1]
      trows = y
      tcols = x
      while trows > 1:
          trows -= 1
          tcols += 1
      while len(arr) < tcols - 1:
          arr.append(arr[-1] + (len(arr) + 1))
      return arr[-1] + x

if __name__=="__main__":
    x=int(input())
    y=int(input())
    print(answer(x,y))
    
