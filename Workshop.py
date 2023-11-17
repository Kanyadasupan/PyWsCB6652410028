import os
print("1.สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
print("2.เลือกวิชาและเพิ่มข้อมูลต่อท้าย")
print("3.เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล")
print("4.เลือกวิชาและลบไฟล์")
print("0.จบการทำงาน")

try:
    userInput = input("กรุณาเลือกเมนู : ")
    if userInput not in ["0","1","2","3","4"] :
        print("กรุณาเลือกเมนู 1, 2, 3, 4 และ 0 เท่านั้น")
    if userInput == "1" :
        print("สร้างไฟล์ใหม่เพื่อเพิ่มข้อมูล")

        nameTheSubject = input("กรุณาตั้งชื่อไฟล์เป็นชื่อวิชาเรียนภาษาอังกฤษ(.txt) : ")
        
        if not ".txt" in nameTheSubject :
                print("ชื่อ-สกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่")
        
        else :
            newFile = open(f"{nameTheSubject}.txt", "w", encoding="utf-8")
            studentName = input("กรุณาป้อน ชื่อ-สกุล : ")
            midTermExamScores = input("กรุณาป้อนคะแนนกลางภาค : ")
            finalExamScore = input("กรุณาป้อนคะแนนสอบปลายภาค : ")
            collectPoints = input("กรุณาป้อนคะแนนเก็บ : ")
            totalScore = int(midTermExamScores)+int(finalExamScore)+int(collectPoints)
            
        if totalScore >= 50 :
            result = "ผ่าน"
            newFile.write(f"นักศึกษา {studentName} คะแนนกลางภาค: {midTermExamScores} \nคะแนนปลายภาค: {finalExamScore} \nคะแนนเก็บ: {collectPoints} \nคะแนนรวม: {totalScore} \n \n")
            print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
            newFile.close()

        else :
            result = "ไม่ผ่าน"
            newFile.write(f"นักศึกษา {studentName} คะแนนกลางภาค: {midTermExamScores} \nคะแนนปลายภาค: {finalExamScore} \nคะแนนเก็บ: {collectPoints} \nคะแนนรวม: {totalScore} \n\n")
            print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
            newFile.close()

    elif userInput == "2" :
        print("เลือกวิชาและเพิ่มข้อมูลต่อท้าย")
        fileName = os.listdir()
        if not  fileName:
            print("ไม่มีไฟล์ใดๆอยู่เลย")
            exit
        else :
            for file in fileName:
                if file.endswith(".txt"):
                    print(file)

        print("เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์")
        select = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ").strip()
        if select not in fileName:
            print("คุณพิมพ์ชื่อไฟล์ผิด")

        elif select in fileName :
            subjectAdd = open(f"{select}", "a+", encoding="utf-8")
            studentName = input("กรุณาป้อน ชื่อ-สกุล : ")
            midTermExamScores = input("กรุณาป้อนคะแนนกลางภาค : ")
            finalExamScore = input("กรุณาป้อนคะแนนสอบปลายภาค : ")
            collectPoints = input("กรุณาป้อนคะแนนเก็บ : ")
            totalScore = int(midTermExamScores)+int(finalExamScore)+int(collectPoints)

        if totalScore >= 50 :
            result = "ผ่าน"
            subjectAdd.write(f"นักศึกษา {studentName} คะแนนกลางภาค: {midTermExamScores} \nคะแนนปลายภาค: {finalExamScore} \nคะแนนเก็บ: {collectPoints} \nคะแนนรวม: {totalScore} \n \n")
            print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
            subjectAdd.close()

        else :
            result = "ไม่ผ่าน"
            subjectAdd.write(f"นักศึกษา {studentName} คะแนนกลางภาค: {midTermExamScores} \nคะแนนปลายภาค: {finalExamScore} \nคะแนนเก็บ: {collectPoints} \nคะแนนรวม: {totalScore} \n\n")
            print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
            subjectAdd.close()
    
    if userInput == "3" :
        fileName = os.listdir()
        if not fileName:
            print("ไม่มีไฟล์ใดๆอยู่เลย")
            exit

        else :
            for file in fileName :
                print(file)
            print("อ่านข้อมูลในไฟล์")

            if select not in fileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif select in fileName :
                readData = open(f"{select}","r", encoding="utf-8")
                rData = readData.read()
                print(rData)
    if userInput == "4" :  
        print("เลือกวิชาและลบไฟล์")
        fileName = os.listdir()
        if not fileName :
            print("ไม่มีไฟล์ใดๆอยู่เลย")
            exit
        else :
            for file in fileName :
                print(file)
        select = input("เลือกไฟล์โดยการป้อนชื่อไฟล์ : ")
        
        if select not in fileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

        elif select in fileName :
                os.remove(f"{select}")
                print("ลบไฟล์เรียบร้อย")
    if select == "0" :
        exit                    
except ValueError:
            print("กรุณาป้อนตัวเลข")
            