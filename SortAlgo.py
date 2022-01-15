import random
import pygame
#screen stuffs
pygame.font.init()
screen = pygame.display.set_mode((590, 450))
pygame.display.set_caption("sort")
width = 600
length = 400
array = [0]*100
arr_clr = ([(0,204,102)]*110)
clr_ind = 0
clr = [(0, 0, 0), (255, 0, 0), 
(47,79,79), (128, 128, 128)]
fnt = pygame.font.SysFont("timesnewroman", 20)
fnt1 = pygame.font.SysFont("timesnewroman", 20)
#random array of 100 nums <= 100
def generate_arr():
    for i in range(1, 100):
        arr_clr[i]= clr[0]
        array[i]= random.randrange(1, 100)
generate_arr() 
#update screen
def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(20)
#draw on screen
def draw():
    element_width =(width-100)//100
    boundry_arr = 600 / 100
    boundry_grp = 350 / 100
    sorts = fnt.render("[1]:Insertion [2]:Bubble "\
        "[3]:Selection [4]:Cocktail [5]:Mergesort" , 1, (0, 0, 0))
    screen.blit(sorts, (15, 15))
    restart = fnt.render("[R]:New Array" , 1, (0, 0, 0))
    screen.blit(restart, (15, 35))
    #bar representation
    for i in range(1, 100):
        pygame.draw.line(screen, arr_clr[i],
            (boundry_arr * i-3, length+50),
            (boundry_arr * i-3, length - array[i]*boundry_grp+50),
            element_width)
class SortingAlgos:
    def insertionsort(self, arr):
        arrlen = len(arr)
        i = 1
        while i < arrlen:
            pygame.event.pump()
            refill()
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                arr_clr[j] = clr[1]
                arr[j-1], arr[j] = arr[j], arr[j-1]
                refill()
                arr_clr[j] = clr[3]
                j -= 1
            i += 1 
            refill()
            arr_clr[i] = clr[0] 
        for i in range(arrlen):
            arr_clr[i] = clr[2]
            refill()    
        print(arr)     

    def bubblesort(self, arr):
        arrlen = len(arr)
        for i in range(arrlen):
            pygame.event.pump()
            refill()
            for j in range(0, arrlen-1-i):
                if arr[j] > arr[j+1]:
                    arr_clr[j+1] = clr[1]
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    refill()
                    arr_clr[j+1] = clr[0]
                if j == arrlen-2-i:
                    arr_clr[j+1] = clr[3]
                    refill()
        for i in range(arrlen):
            arr_clr[i] = clr[2]
            refill()    
        print(arr)
    
    def selectionsort(self, arr):
        arrlen = len(arr)
        for i in range(arrlen):
            pygame.event.pump()
            arr_clr[i] = clr[0]
            refill()
            minidx = i
            refill()
            for j in range(i+1, arrlen):
                lastmin = minidx
                arr_clr[j] = clr[1]
                refill()
                arr_clr[j] = clr[0]
                if arr[j] < arr[minidx]:
                    arr_clr[j] = clr[1]
                    arr_clr[lastmin] = clr[0]
                    minidx = j
                    arr_clr[minidx] = clr[1]
                    refill()
            arr[minidx], arr[i] = arr[i], arr[minidx] 
            arr_clr[i] = clr[3]
            arr_clr[minidx] = clr[0]
            refill()  
        for i in range(arrlen):
            arr_clr[i] = clr[2]  
            refill()  
        print(arr)  

    def cocktailsort(self, arr):
        swap = True
        start = 0
        arrlen = len(arr)
        end = arrlen
        while swap == True:
            pygame.event.pump()
            refill()
            swap = False
            for i in range(start, end-1):
                if (arr[i] > arr[i+1]):
                    arr_clr[i+1]= clr[1]
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    refill()
                    arr_clr[i+1] = clr[0]
                    swap = True
            arr_clr[end] = clr[3]   
            refill()   
            if swap == False:
                break
            swap = False
            end -= 1
            for i in range(end,start,-1):
                if arr[i-1] > arr[i]:
                    arr_clr[i-1]= clr[1]
                    arr[i-1],arr[i] = arr[i],arr[i-1]
                    refill()
                    arr_clr[i-1] = clr[0]
                    swap = True        
            arr_clr[start] = clr[3]  
            refill()               
            start += 1  
        for i in range(arrlen):
            arr_clr[i] = clr[2]
            refill()        
        print(arr)
    def mergesort(self, array, l, r):
        mid =(l + r)//2
        if l<r:
            self.mergesort(array, l, mid)
            self.mergesort(array, mid + 1, r)
            self.merge(array, l, mid,
                mid + 1, r)
    def merge(self, array, x1, y1, x2, y2):
        i = x1
        j = x2
        temp =[]
        pygame.event.pump() 
        while i<= y1 and j<= y2:
            arr_clr[i]= clr[1]
            arr_clr[j]= clr[1]
            refill()
            arr_clr[i]= clr[0]
            arr_clr[j]= clr[0]
            if array[i]<array[j]:
                    temp.append(array[i])
                    i+= 1
            else:
                    temp.append(array[j])
                    j+= 1
        while i<= y1:
            arr_clr[i]= clr[2]
            refill()
            arr_clr[i]= clr[0]
            temp.append(array[i])
            i+= 1
        while j<= y2:
            arr_clr[j]= clr[2]
            refill()
            arr_clr[j]= clr[0]
            temp.append(array[j])
            j+= 1
        j = 0 
        for i in range(x1, y2 + 1): 
            pygame.event.pump() 
            array[i]= temp[j]
            j+= 1
            arr_clr[i]= clr[1]
            refill()
            if y2-x1 == len(array)-2:
                arr_clr[i]= clr[2]
            else: 
                arr_clr[i]= clr[0]

    #alternative mergesort, one function
    def mergesort2(self, arr):
        if len(arr) <= 1:
            return
        arrlen = len(arr)
        mid = arrlen // 2
        left = arr[0:mid]
        right = arr[mid:]
        self.mergesort2(left)
        self.mergesort2(right)
        lefti = 0
        righti = 0
        current = 0
        while lefti < mid and righti < arrlen-mid:
            if left[lefti] < right[righti]:
                arr[current] = left[lefti]
                lefti += 1
            else:
                arr[current] = right[righti]
                righti += 1
            current += 1
        while lefti < mid:
            arr[current] = left[lefti]
            lefti += 1
            current += 1
        while righti < arrlen-mid:
            arr[current] = right[righti]
            righti+=1
            current +=1
        print(arr)
def main():
    s1 = SortingAlgos()
    run = True
    while run:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_1:
                    s1.insertionsort(array)
                if event.key == pygame.K_2:
                    s1.bubblesort(array)
                if event.key == pygame.K_3:
                    s1.selectionsort(array)
                if event.key == pygame.K_4:
                    s1.cocktailsort(array)
                if event.key == pygame.K_5:
                    s1.mergesort(array, 1, len(array)-1)
        draw()
        pygame.display.update()    
    pygame.quit()

if __name__ == "__main__":  
    main()

