from hello.models import  Mention, Recom

def score(price):
    
    global number
    number=price
    if(int(price)==1):
            try:
                key=Recom.objects.get(num=price)
                if (key):
                    cancel=Recom.objects.get(num=price)
                    cancel.delete()
                    Recom.objects.create(
                    img1="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20220607121008994_SB1Z0W715.png%2F20220607120237_Y.png%3Ftype%3Dm1500"
                    ,img2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_9%2F20230427140615174_HEPMRICSR.png%2F20230427135751_U.png%3Ftype%3Dm1500"
                    ,link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=26457170&qvt=0&query=2023%20%EB%AA%A8%EB%8B%9D%20%EC%A0%95%EB%B3%B4"
                    ,link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=31462784&qvt=0&query=2023%20%EC%BA%90%EC%8A%A4%ED%8D%BC%20%ED%8F%AC%ED%86%A0"
                    ,num=1
                    ) 
            except:
                    Recom.objects.create(
                    img1="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20220607121008994_SB1Z0W715.png%2F20220607120237_Y.png%3Ftype%3Dm1500"
                    ,img2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_9%2F20230427140615174_HEPMRICSR.png%2F20230427135751_U.png%3Ftype%3Dm1500"
                    ,link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=26457170&qvt=0&query=2023%20%EB%AA%A8%EB%8B%9D%20%EC%A0%95%EB%B3%B4"
                    ,link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=31462784&qvt=0&query=2023%20%EC%BA%90%EC%8A%A4%ED%8D%BC%20%ED%8F%AC%ED%86%A0"
                    ,num=1
                    ) 
            
    if(int(price)==2):
            try:
                key=Recom.objects.get(num=price)
                if (key):
                    cancel=Recom.objects.get(num=price)
                    cancel.delete()
                    Recom.objects.create(
                        img1="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_9%2F20230503101115446_TA16KL152.png%2F20230503100610_t.png%3Ftype%3Dm1500"        
                        ,img2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20221114125621183_IOQGN0BH1.png%2F20221114124905_u.png%3Ftype%3Dm1500"        
                        ,link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=30909221&qvt=0&query=2024%20%EC%8F%98%EB%82%98%ED%83%80"        
                        ,link2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20221114125621183_IOQGN0BH1.png%2F20221114124905_u.png%3Ftype%3Dm1500"    
                        ,num=2
                    )
            except:
                 Recom.objects.create(
                        img1="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_9%2F20230503101115446_TA16KL152.png%2F20230503100610_t.png%3Ftype%3Dm1500"        
                        ,img2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20221114125621183_IOQGN0BH1.png%2F20221114124905_u.png%3Ftype%3Dm1500"        
                        ,link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=30909221&qvt=0&query=2024%20%EC%8F%98%EB%82%98%ED%83%80"        
                        ,link2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20221114125621183_IOQGN0BH1.png%2F20221114124905_u.png%3Ftype%3Dm1500"    
                        ,num=2
                    )
                 
                    

    if(int(price)==3):
            try:
                key=Recom.objects.get(num=price)
                if (key):
                    cancel=Recom.objects.get(num=price)
                    cancel.delete()
                    Recom.objects.create(
                img1="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_9%2F20230519100509466_BXPT00L9G.png%2F20230519100404_w.png%3Ftype%3Dm1500",
                img2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20221123141115449_2SBMMQ36D.png%2F20221123140845_x.png%3Ftype%3Dm1500",
                link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=31541627&qvt=0&query=2023%20G70%20%EC%8A%88%ED%8C%85%EB%B8%8C%EB%A0%88%EC%9D%B4%ED%81%AC%20%EC%A0%95%EB%B3%B4",
                link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29273068&qvt=0&query=2023%20GV80%20%EC%A0%95%EB%B3%B4"
                ,num=3
            )
            except:
                  Recom.objects.create(
                img1="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_9%2F20230519100509466_BXPT00L9G.png%2F20230519100404_w.png%3Ftype%3Dm1500",
                img2="https://search.pstatic.net/common?quality=75&direct=true&ttype=input&src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F5662_000_8%2F20221123141115449_2SBMMQ36D.png%2F20221123140845_x.png%3Ftype%3Dm1500",
                link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=31541627&qvt=0&query=2023%20G70%20%EC%8A%88%ED%8C%85%EB%B8%8C%EB%A0%88%EC%9D%B4%ED%81%AC%20%EC%A0%95%EB%B3%B4",
                link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29273068&qvt=0&query=2023%20GV80%20%EC%A0%95%EB%B3%B4"
                ,num=3
            )
                  


    if(int(price)==4):
            try:
                key=Recom.objects.get(num=price)
                if (key):
                    cancel=Recom.objects.get(num=price)
                    cancel.delete()
                    Recom.objects.create(
                        img1="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20220929_12%2Fauto_1664423409474IlUU3_JPEG%2F20220929125001_VrQM8dlP.jpg",
                        img2="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20230126_260%2Fauto_1674709425969JU6GY_JPEG%2F20230126140343_vWPKYvT3.jpg",
                        link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=28852060&qvt=0&query=2023%20BMW%20Z4%20%EC%A0%95%EB%B3%B4",
                        link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29699720&qvt=0&query=2023%20%EC%95%84%EC%9A%B0%EB%94%94%20SQ5"
                        ,num=4
                    )
            except:
                Recom.objects.create(
            
                img1="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20220929_12%2Fauto_1664423409474IlUU3_JPEG%2F20220929125001_VrQM8dlP.jpg",
                img2="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20230302_146%2Fauto_1677732157775O7wim_JPEG%2F20230302134234_qeAYxRKz.jpg",
                link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29021668&qvt=0&query=2023%20%EB%9E%8C%EB%B3%B4%EB%A5%B4%EA%B8%B0%EB%8B%88%20%EC%9A%B0%EB%A3%A8%EC%8A%A4%20S%20%EC%A0%95%EB%B3%B4",
                link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29836745&qvt=0&query=2023%20%EB%B2%A4%ED%8B%80%EB%A6%AC%20%ED%94%8C%EB%9D%BC%EC%9E%89%20%EC%8A%A4%ED%8D%BC%20%EC%A0%95%EB%B3%B4"
                ,num=4
            )
                

    if(int(price)==5):
            try:
                key=Recom.objects.get(num=price)
                if (key):
                    cancel=Recom.objects.get(num=price)
                    cancel.delete()
                    Recom.objects.create(            
                img1="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20221114_5%2Fauto_1668387986627P3NyW_JPEG%2F20221114100622_NILPYaVa.jpg",
                img2="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20230302_146%2Fauto_1677732157775O7wim_JPEG%2F20230302134234_qeAYxRKz.jpg",
                link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29021668&qvt=0&query=2023%20%EB%9E%8C%EB%B3%B4%EB%A5%B4%EA%B8%B0%EB%8B%88%20%EC%9A%B0%EB%A3%A8%EC%8A%A4%20S%20%EC%A0%95%EB%B3%B4",
                link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29836745&qvt=0&query=2023%20%EB%B2%A4%ED%8B%80%EB%A6%AC%20%ED%94%8C%EB%9D%BC%EC%9E%89%20%EC%8A%A4%ED%8D%BC%20%EC%A0%95%EB%B3%B4"
                ,num=5
            )
            except:
                   Recom.objects.create(
            
                img1="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20221114_5%2Fauto_1668387986627P3NyW_JPEG%2F20221114100622_NILPYaVa.jpg",
                img2="https://search.pstatic.net/common?type=b&size=240&quality=75&direct=true&ttype=input&src=https%3A%2F%2Fimgauto-phinf.pstatic.net%2F20230302_146%2Fauto_1677732157775O7wim_JPEG%2F20230302134234_qeAYxRKz.jpg",
                link1="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29021668&qvt=0&query=2023%20%EB%9E%8C%EB%B3%B4%EB%A5%B4%EA%B8%B0%EB%8B%88%20%EC%9A%B0%EB%A3%A8%EC%8A%A4%20S%20%EC%A0%95%EB%B3%B4",
                link2="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29836745&qvt=0&query=2023%20%EB%B2%A4%ED%8B%80%EB%A6%AC%20%ED%94%8C%EB%9D%BC%EC%9E%89%20%EC%8A%A4%ED%8D%BC%20%EC%A0%95%EB%B3%B4"
                ,num=5
            )              
    return()

def Userprice():
     return number